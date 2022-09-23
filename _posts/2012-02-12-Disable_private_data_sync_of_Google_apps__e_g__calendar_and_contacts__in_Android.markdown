---
layout: post
title:  "Disable private data sync of Google apps (e.g. calendar and contacts) in Android"
date:   2012-02-12 14:28:00 +0000
categories: ['Android', 'Hack', 'Linux', 'Mod']
legacy_permalink: http://fomori.org/blog/?p=293
---


Disable private data sync of Google apps (e.g. calendar and contacts) in Android
================================================================================

This post describes a dirty (but effective) workaround to individually disable data synchronization of the installed Google apps, while keeping others (e.g. Android Market) intact.

First of all, this only works on “[rooted](http://en.wikipedia.org/wiki/Rooting_%28Android_OS%29 "en.wikipedia.org - Rooting (Android OS)")” devices and you need to have the [ADB](http://developer.android.com/sdk/installing.html "developer.android.com - Installing the SDK") installed on your computer. If you have not rooted your device yet, I can only recommend doing so, even if you do not plan to apply any of the solutions described in this post. Not having root access on your own GNU/Linux system is stupid and frustrating. You paid for it, you should have full control over it!

I own an Android phone and the most important feature to me (after making calls) is the calendar. The calendar itself works great, but in order to use it you got to have a Google account and sync your calendar entries with it. What an insolence! I tried every option, there was no way to prevent the calendar from syncing. The only options are “visible & sync”, “sync & not visible” and “don’t sync & not visible”. Viewing the calendar without syncing was not possible. I had similar problems with other Google apps, e.g. Contacts. I do not want any of my private data on Google’s servers! Of course, that is easy:  Use a custom ROM and do not install any Google apps. But I still want to use the Android Market (the only trade-off between privacy and comfort I accept). **So to be clear: Except for Android Market I do not want any app to sync data with Google.**

My first solution was to use [Droidwall](https://market.android.com/details?id=com.googlecode.droidwall.free&hl=en "market.android.com - DroidWall - Android Firewall"), which basically is a GUI for iptables. It works great, but on rare occasions when DroidWall was not active the calendar app synced. I wanted a final solution. The best method I found is to just remove the package that does the syncing (which is different from the actual calendar app). In this case it is “GoogleCalendarSyncAdapter.apk”.

First, connect your device to your computer and locate the package on your device:

```
$ adb shell ls /system/app
```

The absolute path should be */system/app/GoogleCalendarSyncAdapter.apk*. Before modifying anything make a backup of all applications inside the directory (skip this step if you have a [NANDroid](http://wiki.cyanogenmod.com/wiki/Howto:_Using_the_Recovery#NANDroid_backups "wiki.cyanogenmod.com - NANDroid backups") backup):

```
$ adb pull /system/app/* /path_to_destination_on_your_computer/
```

Applications in */system/app* can not be uninstalled via the package manager, you have to remove it manually:

```
$ adb shell rm -f /system/app/GoogleCalendarSyncAdapter.apk
```

**Done! Now there is no way, the Android calendar will ever sync again, finally.**

Since you have come this far, you maybe want to do it right and prevent some of your other Google apps from syncing, too:

```
$ adb shell rm -f /system/app/GoogleContactsSyncAdapter.apk # disable contacts sync
$ adb shell rm -f /system/app/GoogleBackupTransport.apk # disables backup mechanism to google servers
$ adb shell rm -f /system/app/GoogleFeedback.apk # disables fc reports
```

There are probably more to remove (depending on your system).

**Keep in mind that, unless you are using NANDroid, your data (like calendar entries and contacts) are not backuped anywhere anymore.**

To restore the sync mechanism for a particular app again, re-install the removed package:

```
$ adb install /path_to_your_package
```

and everything should work like before.

I do not like Google, but I really like Android. Sadly both are closely related. It is no secret that Google collects an absurd amount of data from it’s users. From collecting your data on your phone (“[[…] hardware model, operating system version, unique device identifiers, and mobile network information including phone number. […] telephony log information like your phone number, calling-party number, forwarding numbers, time and date of calls, duration of calls, SMS routing information and types of calls […]](http://www.google.com/intl/en_ALL/policies/privacy/ "www.google.com - Privacy Policy")“) to logging your search queries and filter your search results based on that. Google considers the latter a feature, for me it is stalking and censorship (~~By the way, a solution for that is [scroogle](http://scroogle.org/ "scroogle.org")~~). All that information is stored somewhere on Google’s servers. Well, Google is not evil (“[Don’t be evil](http://en.wikipedia.org/wiki/Don%27t_be_evil "en.wikipedia.org - Don't be evil")“), of course not! It even tells you about it in its [privacy policy](http://www.google.com/intl/en_ALL/policies/privacy/ "www.google.com - Privacy Policy"). I bet most people that use any kind of Google service never even read it.

**Update:** [scroogle.org](http://scroogle.org/ "scroogle.org") is down. Alternatively use [duckduckgo.com](https://duckduckgo.com/ "duckduckgo.com - HTTPS") or [ixquick.com](https://ixquick.com/ "ixquick.com"). Those are excellent meta search engines that emphasise privacy. If you insist on using Google, try [startpage.com](https://startpage.com/ "startpage.com") (belongs to ixquick.com), which anonymously queries Google for you – just like scroogle.org did.

  

	