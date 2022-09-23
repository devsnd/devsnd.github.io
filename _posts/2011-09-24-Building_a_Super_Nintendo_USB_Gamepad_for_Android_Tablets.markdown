---
layout: post
title:  "Building a Super Nintendo USB Gamepad for Android Tablets"
date:   2011-09-24 11:37:06 +0000
categories: ['Android', 'Hack', 'Hardware', 'Mod']
legacy_permalink: http://fomori.org/blog/?p=10
---


Building a Super Nintendo USB Gamepad for Android Tablets
=========================================================

[![](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/android-snes-usb-in-action.jpg)](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/android-snes-usb-in-action.jpg)I recently build a little USB-SNES-Gamepad for my Android Tablet, because I didn’t like using the on screen controls of the emulators. It just wasn’t fun playing the games of my childhood without the original controller in my hands. Luckily my Tablet has a standard USB port with host capability and supports thumbdrives, keyboards and mice out-of-the-box. So I figuered I could easily put the controllerboard of a usb keyboard inside the spare original SNES gamepad i had liying around.

So I grabbed a cheap usb keyboard at a fleamarket for 3€ or something and tore it apart.[![](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes-usb_android-7.jpg)](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes-usb_android-7.jpg) Inside a normal keyboard these days is little more than the usb controller board and two matrices made of plastic. So I first I had to find out how those matrices actually worked to make them fulfill my purpose and was happy to find an [incredibly good website about everything there is to know about keyboard matrices](http://www.dribin.org/dave/keyboard/one_html/ "Keyboard Matrix Help").

The principle of those matrices is quite simple: If a button is pressed, it will short one vertical line with a horizontal line inside the matrix. If you now apply some current to one of the lines (e.g. the 3rd horizontal line), and a button is pressed, the current will flow through a vertical line (maybe the 2nd) and now the controller board knows that which button was pressed (perhaps the letter ‘a’).

[![](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes-usb_android-1.jpg)](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes-usb_android-1.jpg)

The Android SNES emulator I was using allowed for assigning every all keyboard buttons freely. And now that I read this incredibly interesting website, I knew I could increase the amount of buttons that could be pressed simultaniously by trying to put all buttons on one line in the matrix. But I also wanted to map the arrow buttons of the keyboard to the d-pad of the gamepad, so i could also navigate using gamepad. At first I tried to “decrypt” the matrix, to find out what button belonged to what contacts on the usb-controller, but this wasn’t fun. So i just scratched off this halfway conductive plastic stuff from all the contacts, plugged the controller in my computer and started [xev](http://www.x.org/archive/X11R7.5/doc/man/man1/xev.1.html "xev").

Then I mapped all the outcomings of those shortcuts in the matrix and drew them inside [dia](http://projects.gnome.org/dia/ "Dia a drawing program") for an overview. Here you can see my ugly “wiring” diagram.

[![](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/keyboardmatrix.png)](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/keyboardmatrix.png)

All the blocks on the outside represent a pin on the controller and all the blocks in the middle a button on the keyboard. Sometimes I used the matrix to find out what buttons also were on the same line to speed up the process. but as I didn’t  want to map all the buttons. I stopped when I had all those I needed.

[![](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes-usb_android-2.jpg)](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes-usb_android-2.jpg)So I disassabled the gamepad and the first thing I did was making a terrible mistake: I started cutting all the lines on PCB, thinking that i would just wire up each button with the appropriate pins on the usb-controller. But actually you can just use most of the printed wiring on the PCB of the gamepad and thereby avoid a lot of hassle.

[![](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes_wiring.png)](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes_wiring.png)

So I compared the wirings of the matrix and the gamepad to solder as little as possible. I just cut the ground wire of the controller at some points so that multiple buttons on the gamepad that had a common ground would have the same line inside the keyboard matrix.

[![](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes-usb_android-5.jpg)](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes-usb_android-5.jpg)Still it looked like a mess, but that wasn’t a big deal, because it looked all clean and tidy once I put the gamepad back together.

 

 

 

Now I can finally be completely nostalgic, playing the games of my childhood, as they meant to be played.[![](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes_usb_android-8.jpg)](/assets/2011-09-24-Building a Super Nintendo USB Gamepad for Android Tablets/snes_usb_android-8.jpg)

 

  

	