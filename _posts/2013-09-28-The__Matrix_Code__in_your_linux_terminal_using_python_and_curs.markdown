---
layout: post
title:  "The “Matrix Code” in your linux terminal using python and curs"
date:   2013-09-28 17:50:31 +0000
categories: ['Linux', 'Programming', 'Python', 'Software', 'Useless']
legacy_permalink: http://fomori.org/blog/?p=648
---


The “Matrix Code” in your linux terminal using python and curses
================================================================

Everybody knows the code on the screens in the movie *the matrix*. You can see it for example when the character “cypher” talks to “neo” somewhen in the night, and the green letters fall down on those second-hand dell screens behind them. Funky. I want that too.

[![cypher_neo_code](/assets/2013-09-28-The__Matrix_Code__in_your_linux_terminal_using_python_and_curs/cypher_neo_code-300x168.png)](http://fomori.org/blog/?attachment_id=649)

I’ve written a python program that uses [curses](http://docs.python.org/2/library/curses.html) to create a similar looking animation and just now cleaned up the code a bit and made sure it runs in python 2 and 3. You can [get the source code on github](http://github.com/devsnd/matrix-curses) and there’s a screenshot and a short explaination after the break…

Here’s a screenshot of it in action:

[![screenshot](/assets/2013-09-28-The__Matrix_Code__in_your_linux_terminal_using_python_and_curs/screenshot.jpg)](http://fomori.org/blog/?attachment_id=651)

It uses funny looking characters I found somewhere in the vast Unicode tables. Unfortunately those work only if you’re using python 3. In python 2 it resorts to ASCII letters and doesn’t look as good.

At the top of the script there are a few variables you can tune to your content, like the number of letters dropping or the speed of the characters. By default it uses the colors of your terminal, but you can also activate *USE\_COLORS* to force the green-on-black as in the movie.

Now you can finally run the matrix code anywhere! Your server farm, your mobile, your router and maybe even in DOS or OS/2. Since the program exits in when you press any key, you can use it as something like a screensaver. You get extra points if you put it in your *.bashrc*. I guess something like 15 years after the film came out, this can be considered retro.

  

	