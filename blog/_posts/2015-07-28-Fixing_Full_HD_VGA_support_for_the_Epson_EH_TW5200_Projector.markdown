---
layout: post
title:  "Fixing Full-HD VGA support for the Epson EH-TW5200 Projector"
date:   2015-07-28 22:05:36 +0000
categories: ['Hardware', 'Linux']
author: devsnd
legacy_permalink: http://fomori.org/blog/?p=1209
---


If you happen to own an Epson EH-TW5200 projector, you might have experienced problems setting Full-HD (1920×1080) resolution using a VGA connection under linux. When I set the resolution to Full-HD, the whole screen would stay completely black. This is just a quick fix for the other 4 people that might have this problem.

```
# Create a new full-hd modeline setting using cvt
cvt 1920 1080 60
# copy the cvt output after the Modeline and add it to xrandr
xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
# make the mode available to the VGA output, in my case VGA-0
xrandr --addmode VGA-0 "1920x1080_60.00"
# now set the mode for the VGA output
xrandr --output VGA-0 --mode 1920x1080_60.00
```

The difference between the original modeline and the new one is the vertical refresh rate: The projector proposed 60.02 Hz via [EDID](https://en.wikipedia.org/wiki/Extended_Display_Identification_Data), and the new modeline is just a tad slower, using 59.94 Hz. I was connecting a ThinkPad T60 to the projector, so the problem might also be the [RAMDAC](https://en.wikipedia.org/wiki/RAMDAC) of the laptop, something about [blank phases](https://en.wikipedia.org/wiki/Video_Graphics_Array#Signal_timings), who knows.

 

  

	