---
layout: post
title:  "Using a Raspberry Pi to connect a third display over LAN"
date:   2013-03-31 18:29:24 +0000
categories: ['Raspberry Pi']
author: devsnd
legacy_permalink: http://fomori.org/blog/?p=530
---


Using a Raspberry Pi to connect a third display over LAN
========================================================

I’ve received my rPi a while ago, but never wound up doing much with it. Recently I have received another screen which is a little older, but still features a DVI input. Since developers can’t have enough screen space and my laptop has only one VGA output, I decided to use the raspberry pi as my ethernet-to-DVI adapter.

[![IMG_20130331_200140](/assets/images/IMG_20130331_200140.jpg)](http://fomori.org/blog/?attachment_id=538)

This how-to is composed of two parts, first I explain how to get *synergy* up and running, and then how to set up your *VNC* to help the illusion that everything is happening on the same computer.

install synergy on laptop and Pi
================================

```
$ sudo apt-get install synergy
```

Now we need to edit the configuration file in */etc/synergy.conf* on the laptop (i.e. server). My configuration boils down to this:

```
# third screen raspberry pi 
section: screens
        raspberrypi:
        laptop:
end
 
section: links
        raspberrypi:
                right = laptop
        laptop:
                left = raspberrypi
end
 
section: aliases
end
```

**IMPOTRTANT: the names »raspberrypi« and »laptop« have to be replaced by the hostnames of the computers involved. If unsure, open a terminal and type *hostname***

This basically instructs synergy to create two synergy screens, and redirects the mouse and keyboard input of the server to on of those computers, depending on where I left the screen with the mouse. This setup says, the rPi-screen is left of the laptop; If I leave the laptop screen to the left, the raspberry pi will receive the input of mouse and keyboard and vice-versa.

Now we can start the synergy server on the laptop:

```
$ synergys -f
```

The *-f* switch keeps synergy in the foreground, so we can see any errors on startup. You can leave it out once the setup works.

Now on the rPi

```
$ synergyc -f 192.168.1.10
```

You have to substitute the IP with the IP of your server, of course. Now you should be able to move your mouse between the two screens, yaay.

Setting up VNC
==============

First, you need to install tightvnc on laptop and Pi (or any VNC client/server for that matter, but later on I’ve got sometricks, I didn’t try out using other software)

```
$ apt-get install tightvnc
```

now we need to set up the X server, that will later be displayed on the rPi-screen. To do so, edit **~/.vnc/xstartup**

```
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
DISPLAY=:99 xfwm4 &
DISPLAY=:99 xfdesktop &
```

As you can see, I am starting another window manager and launching a desktop as well on X-display **:99**, note the colon in front of the 99. You can of course replace xfwm4 by any window manager of your choice.

Now we need  to setup a password for the vnc server. This is only due to a bug in tightvnc, so you can skip this part if your VNC client supports standard UNIX authentification. Just start vncpasswd and enter some password.

```
$ vncpaswd
```

Now wecan finally start our VNC server:

```
$ vncserver :99 -geometry 900x1400
```

As you can see, I’m starting the server on the same display (:99) as previously set up in the *~/.vnc/xstartup*. The *-geometry* switch lets me specify the size of the display of this X server. This should be the same resolution as the display connected to the raspberry pi. The resolution I’m using only looks weird, because I’ve rotated the display by 90 degrees, because I’m planning on looking at PDFs and the like on that screen.

Now we can start the vncviewer on the raspberry Pi:

```
$ vncviewer 192.168.1.10:99
```

Again, you need to replace the IP  with the IP of your laptop/server. Basically, that’s it. You should now be able to use your third screen. But I encountered some problems, like the keyboard focus not working properly in fullscreen mode and the ‘d’ key not working properly, I’ve prepared some workarounds for that; But depending on your setup, maybe it works for you out of the box.

Some Workarounds
================

Getting the keyboard to work in fullscreen mode
-----------------------------------------------

install the program *xrdb*

```
$ sudo apt-get install x11-xserver-utils
```

Now we need to set the option *grabKeyboard* inthe ~/.Xresources file and the apply the configuration using xrdb:

```
$ echo "Vncviewer*grabKeyboard: true" >> ~/.Xresources
$ xrdb -merge ~/.Xresources
```

Now you should be able to use your keyboard in fullscreen mode.

pressing the key ‘d’ results in showing the desktop instead of typing the character ‘d’
---------------------------------------------------------------------------------------

This seems to be a problem using the keyboard shortcuts, which are predefined in XFCE in combination with VNC. To work around thi issue, just set the show desktop command to some other hotkey.

```
$ xfwm4-settings
```

Go to the *keyboard* tab and change the *show desktop* hotkey to something different.

  

	