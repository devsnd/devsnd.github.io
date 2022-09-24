---
layout: post
title:  "QCAD – Symbols, special characters and font styles in dimension labels"
date:   2014-08-20 16:19:20 +0000
categories: ['Hack', 'Linux', 'Software']
author: 6arms1leg
legacy_permalink: http://fomori.org/blog/?p=1005
---


QCAD – Symbols, special characters and font styles in dimension labels
======================================================================

[![Cover - QCAD with Alpha and l_ABz dimensions](/assets/images/Cover-QCAD-with-Alpha-and-l_ABz-dimensions.png)](/assets/images/Cover-QCAD-with-Alpha-and-l_ABz-dimensions.png)

[QCAD](http://www.qcad.org/en/ "qcad.org") is a great free and open source [CAD](https://en.wikipedia.org/wiki/Computer-aided_design "en.wikipedia.org - Computer-aided_design") software. Although limited to 2D design, it is my favorite tool for drafting, construction and simple sketches. It is [well documented](http://www.qcad.org/en/qcad-documentation "qcad.org/en - qcad-documentation") overall, but one issue I could not find a solution for, was how to label dimensions with symbols, special characters or certain font styles (bold, italic, super-/subscript).

This blog post provides a simple trick to get it done.

If you try to label the dimension of an angle with a symbol (like “α” or “β”) for example, QCAD will only show a question mark (“?”) as a place holder:

[![QCAD with ? dimension](/assets/images/QCAD-with-dimension.png)](/assets/images/QCAD-with-dimension.png)

To get QCAD to display symbols, special characters or certain font styles (bold, italic, super-/subscript) in dimension labels, the desired label in the label text field must be provided in a certain text format:

```
\fFONT|b0|i0|c0|p0;LABELTEXT
```

FONT – desired font; LABELTEXT – text (or symbols, etc.) to label the dimension with; “|b0|i0|c0|p0;” – each entry takes “0” or “1” to switch font styles (bold, italic, etc.)

For example (α in italic monospace for an angle dimension label):

```
\fMonospace|b0|i1|c0|p0;α
```

[![QCAD with Alpha dimension](/assets/images/QCAD-with-Alpha-dimension.png)](/assets/images/QCAD-with-Alpha-dimension.png)

Super- and subscript font styles are also possible by using:

```
\SSUPERSCRIPT^;
```

or

```
\S^SUBSCRIPT;
```

SUPERSCRIPT – text in superscript; SUBSCRIPT – text in subscript

E.g., for the italic “*lABz*” length dimension label in the above illustration that would be:

```
\fMonospace|b0|i1|c0|p0;l\S^ABz;
```

It may not be the most user friendly way to format text (the normal text tool in QCAD does a far better job), but it works.

  

	