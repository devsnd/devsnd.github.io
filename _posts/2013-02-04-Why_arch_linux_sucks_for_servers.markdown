---
layout: post
title:  "Why arch linux sucks for servers"
date:   2013-02-04 21:52:56 +0000
categories: ['Arch Linux', 'Linux', 'Server']
author: devsnd
legacy_permalink: http://fomori.org/blog/?p=468
---


Why arch linux sucks for servers
================================

[![archlogo](/assets/images/archlogo.png)](http://fomori.org/blog/?attachment_id=472)Yes, you heard correctly. Installing arch linux on a server is the biggest mistake you could make as admin. And I made that mistake.

Let me explain: I love arch linux. I love it so much, that I dared to put it onto just about any machine I own. Arch linux is genius, because you get all the latest updates of all the software you use and because you can install software packaged by the community in a split second without worrying about *make install* ruining your system. I’ve been running arch linux on my personal laptop now for some years and I was able to fix whatever problem came across, because I know what’s going on under the hood and because of the great help of the arch linux community.

The problem is, that you need to *pacman -Syu* regularly, because if you don’t, you don’t have any chances of getting your remotly installed server back in shape. This is due to the many changes arch linux goes through to stay the cutting edge distro it is. I understand that. But nobody warned me, that if you fail to update your software two or more times those major changes come in, then you’re humped. That’s because you need to make the intermediary updates to keep your system running. Those major changes can happen within one month. You know, that month you spent in italy. This wouldn’t be to bad, but there is no repository that keeps snapshots of all packages you’ve installed on your server for each of those intermediary steps in one place.

You might now say: »This is your own fault you dick head. Just update the server every once in a while.« And you are right. But if you want to have a life aside from being a nerd, this is more complicated than it sounds. Anyway, if you’re still with me and still want to install arch linux on your server, take this advice:

Even if you think you will update your server regularly, **keep snapshots of the latest versions of all the packages you’ve installed on your server at least once every two weeks**. You can install them when you have time. If you don’t, you’ll find out if the server really serves you or if you serve it.

You have been warned.

UPDATE:
-------

In the comments someone mentioned ARM (Arch Rollback Machine), so if you have come here out of frustration, there might be a hope. See the [Arch Wiki Page](https://wiki.archlinux.org/index.php/Downgrading_Packages#Arch_Rollback_Machine "ARM Arch Rollback Machine") for more information on the rollback machine. Nguyen, thanks for the heads-up.

  

	