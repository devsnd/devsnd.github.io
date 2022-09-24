import sys
import os
import re
from html import unescape
import markdownify
import shutil
from bs4 import BeautifulSoup

from markdownify import MarkdownConverter

class ImageBlockConverter(MarkdownConverter):
#	def convert_pre(self, el, text, convert_as_inline):
#		print(text)
#		return '```\n' + re.sub('(\xa0+)', lambda m: len(m.group(0))*' ' + '\n', text) + '\n```'
	pass
		


basedir = '/home/tom/data/fomori-blog/devsnd.github.io/wayback/websites/fomori.org/blog/'
output_folder = '/home/tom/data/fomori-blog/devsnd.github.io/_posts/'
asset_base_folder = '/home/tom/data/fomori-blog/devsnd.github.io/assets/'

for file in sorted(os.listdir(basedir)):
	if not file.startswith('__p'):
		continue
	match = re.findall('__p=(\\d+)$', file)
	if not match:
		continue 
	
	post_id = match[0]
	post_name = 'post_' + post_id
	index_file = os.path.join(basedir, file, 'index.html')
	with open(index_file, 'r') as fh:
		index_data = fh.read()

	title = unescape(re.findall('<title>([^<]+)</title>', index_data)[0][:-len('| fomori blog')]).strip()
	
	content = re.findall('<article.+?>(.+?)<\\/article', index_data, re.DOTALL)[0]
	def repl_func(match):
		soup = BeautifulSoup(match.groups()[0], features="lxml")
		
		all_crayon_lines = soup.find_all(lambda tag: tag.name == 'div' and 'crayon-line' in tag['class'])
		lines = [
			td.get_text()
			for i, td in enumerate(all_crayon_lines)
		]
		joined_lines = "\n".join(lines)
		retval = f'<pre><code>{joined_lines}<code></pre>'
		# print(retval)
		return retval
	content = re.sub('<table class="crayon-table">(.+?)</table>', repl_func, content, flags=re.DOTALL)
	# convert to markdown
	content = ImageBlockConverter().convert(content)
	# remove wordpress stuff
	content = re.sub('\nPosted on.+\n', '', content)
	content = re.sub('This entry was posted in.+\n', '', content, re.DOTALL)
	content = content.replace('\xa0', ' ')
	content = re.sub('\n\n+', '\n\n', content)
	
	datetime = re.findall('<time.+? datetime="(.+?)"', index_data)[0].replace('T', ' ').replace('+00:00', ' +0000')
	date = datetime.split(' ')[0]
	
	author = re.findall('rel="author">(.+?)<\\/a', index_data)[0]

	categories = re.findall('rel="category">(.+?)<', index_data)
	tags = re.findall('rel="tag">(.+?)<', index_data)
	permalink = re.findall('Bookmark the <a href="([^"]+)', index_data)[0]

	images = [
		(src, basedir + src.replace('http://fomori.org/blog/', ''))
		for src in re.findall('<img .+?src="([^"]+)', index_data)
	]

	normalized_title = re.sub("\\W", "_", title)
	filename = f'{date}-{normalized_title}.markdown'
	post_asset_folder = f'images'
	
	output_path = os.path.join(output_folder, filename)
	for src_url, src in images:
		image_file_name = src.rsplit('/', 1)[1]
		post_asset_path = os.path.join(asset_base_folder, post_asset_folder)
		try:
			os.mkdir(post_asset_path)
		except:
			pass
		dst = os.path.join(post_asset_path, image_file_name)
		dst_url = os.path.join('/assets/' + post_asset_folder, image_file_name)
		try:
			shutil.copy(src, dst)
		except:
			print(f'Missing Image! {src}')
		# print(dst)
		content = content.replace(src_url, dst_url)
		# print(dst_url)

	post = f'''---
layout: post
title:  "{title}"
date:   {datetime}
categories: {categories}
author: {author}
legacy_permalink: {permalink}
---
{content}
	'''
	
	with open(output_path, 'w', encoding='utf-8') as w:
		w.write(post)
	# sys.exit(0)