---
layout: post
title:  "PyLint and Pep8 validation in geany"
date:   2013-04-06 13:39:29 +0000
categories: ['Linux', 'Programming', 'Python', 'Software']
author: devsnd
legacy_permalink: http://fomori.org/blog/?p=548
---


PyLint and Pep8 validation in geany
===================================

If you’re into python, but don’t know about [PEP8](http://www.python.org/dev/peps/pep-0008/) or [PyLint](http://www.pylint.org/), you should find out right now. And because pep8 and pylint are great, but it’s hard to force yourself to use them all the time, lets integrate them into [geany](http://www.geany.org), a fast and lightweight IDE.

First download the packages containing pylint and pep8. For arch linux, they’re called *pep8-python3* and *pylint* respectively. The names may differ for other distributions.

```
$ sudo pacman -S pep8-python3 pylint
```

Now start geany and open the *Build* menu. Open *Set Build Commands.*

Click on the button next to the number *2*. and give it a proper name, e.g. *pep8lint*. Now put the following command next to it:

```
pep8 "%f" & pylint -f parseable -r n "%f"
```

This basically calls both programs and prints their output into the compiler panel at the bottom  of the screen. Now, to highlight all lines that don’t validate, we need to set up a regular expression like so:

```
^(.+?):([0-9]+):.+
```

This regular expression matches the output of pep8 and pylint. Geany interprets the first group as the name of the source file and the second group as the line number.

[![This is how your configuration should look like](/assets/images/geanypylintpep8.png)](http://fomori.org/blog/?attachment_id=549)This is how your configuration should look like

To valiate, just press *F9*, since that launches the second build command.

Everything is red now. Great.

[![sourceallred](/assets/images/sourceallred.png)](http://fomori.org/blog/?attachment_id=550)

  

	