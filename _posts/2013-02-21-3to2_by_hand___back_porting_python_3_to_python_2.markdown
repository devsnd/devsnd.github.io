---
layout: post
title:  "3to2 by hand – back porting python 3 to python 2"
date:   2013-02-21 11:03:03 +0000
categories: ['Programming', 'Python']
author: devsnd
legacy_permalink: http://fomori.org/blog/?p=486
---


As mentioned in an earlier post, I’m currently writing a [music streaming server](http://fomori.org/cherrymusic "CherryMusic – A Music Streaming server for your browser") in python. As I wanted to go with the newest thing available, I wrote it in python 3. Unfortunately the application server we rely on, [cherrypy](http://cherrypy.org), is only packaged for python 2 in most distributions! Even worse, even if the packages were installed for python 3, it would not run, since I relied on python 3.3 features.

Since this keeps my program from being used in the world, I decided to backport it to python 2. For me it was very important, that the code would not get any uglier by doing so, so I started writing a replacement module.

Here’s a collection of useful code snippets to help you making your software python 2 / 3 compatible.

Let’s jump in the code. You can check which version is running like so:

checking the version
--------------------

```
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=3, micro=0, releaselevel='final', serial=0)
```

As you see, I’m running python 3.3 on my laptop. Fortunately you can compare the version\_info object with tuples, so you can easily check if a version is below or above:

```
>>> sys.version_info > (3,0)
True
```

But watch out, you can not check for equality in this way.

Well, let’s go to the nice, ugly or hackish gems I have prepared.

setting unicode strings as standard
-----------------------------------

works in python 2.7+

```
from __future__ import unicode_literals
```

This is the most important change between python 2 and 3. In python 2 stings are just byte arrays. Python 2 relied on those strings being ASCII encoded. It supplied a special type *unicode* that could contain characters outside the ASCII range. This option enables, that all strings are understood as *unicode* objects.

```
>>> 'hello'
'hello'
>>> from __future__ import unicode_literals
>>> 'world'
u'world'
```

Do you see the *u* in front of the string? That is how unicode strings are represented in python 2. This means, that all your static string variables are now in unicode!

type() checking strings
-----------------------

Since all strings in python 3 are unicode strings, there is no need anymore for the *unicode* object. But here comes the tricky part: In python 2, all our strings are now *unicode* objects, but there is no such object in python 3. So how can we now check for type equality in both versions?

Simple! In python 2:

```
foo = 'bar'
type(foo) == str      #checks if we have an old 8bit style string
type(foo) == type('') #checks if we have a unicode string
```

In python 3:

```
foo = 'bar'
type(foo) == str      # checks if it's a unicode string
type(foo) == type('') # checks if it's a unicode string
```

You might say, »that is neat, but why should I care«? And I’m telling you, because you will encounter 8bit strings in your python 2 version. And this is how you can handle them:

Converting strings to unicode
-----------------------------

```
>>> from __future__ import unicode_literals
>>> str('foo')
'foo'             #old style string
>>> str('foo')+''
u'foo'            #unicode string
```

Adding this empty unicode string to your string, will cast the other stirng automatically to a *u’string’*! The great thing about it is, that this will not change your strings in python 3, since all strings are of the class *str* and will therefore just be appended with the empty string. So if you’re now sure about the encoding of the string, and don’t know if it’s unicode or not, you can simply add the empty string.

You can also put this inside a function that will convert all your strings:

```
def unistr(val):
    if type(val) == str:
        return val+''     # '' is implicitly unicode
    return val
```

If you’re program doesn’t handle many strings, or performance is not your thing, then you can call this method each time you use a string.

print
-----

You can import the python 3 printing function into python 2 as well. This works for python 2.6+

```
from \_\_future\_\_ import print\_function
```

This will give you all the same function arguments as in python 3, e.g. the *end* argument, which can be very handy. Since python 2 also natively supports the *print(‘foo’)* syntax (with the strings in parenthesis), there should be nothing else to change for backwards compability.

input and raw\_input
--------------------

The *input* statement has changed in python 3; *input* used to be something like the exec statement, and has changed to just receive user input as strings. You can just override the input method with the *raw\_input* statement.

```
if sys.version_info < (3,0):
    input = raw_input
else:
    input = input
```

I don’t know if there are any other side effects by doing so, but it worked well enough for me.
argparse and optparse
---------------------

Python 3.3 introduced a new very handy module called *argparse.* The main difference between *optparse* and *argparse* is, that *argparse* supports also switches with multiple inputs. So be aware that the code below might break your command line interface. It should however work for the most part.

```
if sys.version_info < (3,2):
    # import the old module with the name of the new one
    import optparse as argparse
    # make sure the class name is available like in python 3.3
    argparse.ArgumentParser = argparse.OptionParser
    # same for the add methods:
    argparse.ArgumentParser.add_argument = argparse.ArgumentParser.add_option
    # save a reference to the old parse method
    argparse.ArgumentParser.__parse_args__ = argparse.ArgumentParser.parse_args
    # override the parse method:
    def parseargs(self):
        return self.__parse_args__()[0]
    argparse.ArgumentParser.parse_args = parseargs
else:
    import argparse
```

Enjoy this code with caution.

configparser:
-------------

The config parse module didn’t change to much, so all you need to do is to change the letter casing:

```
if sys.version_info < (3,0):
    from ConfigParser import ConfigParser
else:
    from configparser import ConfigParser
```

Code encoding:
--------------

Since you might have unicode literals in your code, make sure, that you set the encoding in your source files!

```
#!/usr/bin/python3
# -*- coding: utf-8 -*-
```

 Some more info I found very helpful:
-------------------------------------

[Supporting Python 2 and 3 without 2to3 conversion](http://python3porting.com/noconv.html "Supporting Python 2 and 3 without 2to3 conversion")

Update:
-------

Just found this piece of code inside cherrypy, pure gold.

[\_cpcompat.py in cherrypy](https://bitbucket.org/cherrypy/cherrypy/src/01b6adcb3849b2ff4fa31e3298b494f6b136369e/cherrypy/_cpcompat.py)

Update 2
--------

```
>>> 2/3
0
>>> from __future__ import division
>>> 2/3
0.6666666666666666
```

This will handle all your calculations as you expect them to (at least from a python 3 point of view)

 

 

 

Happy porting!

 

  

	