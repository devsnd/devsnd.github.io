---
layout: post
title:  "Indexing large tar files for fast access using python"
date:   2012-05-24 12:20:26 +0000
categories: ['Programming', 'Python', 'Software']
author: devsnd
legacy_permalink: http://fomori.org/blog/?p=391
---


[![](/assets/images/tarindexer-150x150.png "tarindexer")](/assets/images/tarindexer.png)I recently needed to get some data out of a large tar file, about 5gb in size, that I didn’t want to extract, as it contained many thousands of small files. Unfortunately the tar format was not designed to be indexed, since it was meant for backups on magnetic tapes (*tar* stands for *ta**pe archive*). The gnu [tar](http://www.linuxmanpages.com/man1/tar.1.php) has a command for retrieving single files, but it needs to go through the whole tar each time, which was just too slow.

So I decided to write a little tool, that would index all files inside the archive and write that index to another file. Now I can access each file within the tar in just a second, instead of 15 minutes. Introducing the tarindexer!

**UPDATE: The project is now up on github under GPL v3**  

[**https://github.com/devsnd/tarindexer**](https://github.com/devsnd/tarindexer "https://github.com/devsnd/tarindexer")

For everyone who just wants to get on with their lives, here is the download:

~~[Download: tarindexer.tar.gz](http://fomori.org/blog/wp-content/uploads/2012/05/tarindexer.tar.gz)~~

**Usage:**  

*create index file:*  

tarindexer -i tarfile.tar indexfile.index  

*lookup file using indexfile (prints file to stdout):*  

tarindexer -l tarfile.tar indexfile.index lookuppath

Now something on how it works; The tarindexer uses python’s tarfile module to crawl through the files (a.k.a. members, as they can be symlinks or folders as well). I looked inside the source or the tarfile module to find out where the current reading position was (TarInfo.offset\_data). and writing that number along with the name and the filesize of that member into the index file. No magic here.

Later, when looking up a file, the program just tries to find the path inside the index file, finds out the position and size of that file, and then seeks to the position inside the tar.

But as I went along I noticed that the tarfile module ate all my RAM. It took only few seconds for the swap to burst… A short search on the internet revealed, that it could be fixed easily by [throwing away the references to the members](http://blogs.oucs.ox.ac.uk/inapickle/2011/06/20/high-memory-usage-when-using-pythons-tarfile-module/), e.g.:

```
for tarinfo in tarfile.open(tarfilepath, 'r'):
    #do something ...
    #free RAM:
    tarinfo.members = []
```

Now the RAM usage was back to normal, I could finally access the data from the tar rapidly and everybody’s happy.

  

	