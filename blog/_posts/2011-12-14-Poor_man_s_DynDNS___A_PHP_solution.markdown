---
layout: post
title:  "Poor man’s DynDNS – A PHP solution"
date:   2011-12-14 03:51:46 +0000
categories: ['Hack', 'Linux', 'PHP', 'Programming']
author: devsnd
legacy_permalink: http://fomori.org/blog/?p=308
---


I’m running a [Thin-Client as a home server](http://fomori.org/blog/blog/2011/09/29/cheap-home-server-introducing-the-thin-server/ "Cheap Home Server: Introducing the Thin-Server") and sometimes I need access to some files at home. Since those no-ip services didn’t prove that reliable in the past, I decided to implement a DynDNS substitute in PHP.

The concept is quite simple: Let the little server at home call a PHP script somewhere on a “big” Server that has a static IP. The big server then writes the IP to a file, so it can be read from anywhere. There are two scripts that have to reside on the big server: an *index.php*, which reads and echoes the IP, that was recorded, and another script in a *.htaccess* protected folder, which is able to write the IP of the home server to a file.

index.php:

```
echo file_get_contents("ip");
```

setip.php:

```
$fh = fopen("../ip", 'w') or die("can't open file");
fwrite($fh, $_SERVER['REMOTE_ADDR']);
fclose($fh);
```

By putting the *setip.php* inside a *.htaccess* protected folder you’re making sure that the IP is only set by your home server and nobody else.

The only thing that’s left to do, is to set a cron job on your home server, that calls this script once in a while. So call the crontab editor as root

```
crontab -e
```

and add a line to call *wget* every 5 minutes, for example. (the user and pass should of course be the ones defined in your *.htpasswd*.

```
*/5 * * * * * wget -O - --http-user=user --http-password=pass domain.com/p/setip.php
```

There you have it, you own cheap DynDNS service in just 3 minutes. To use it, just open *domain.com/index.php* in your browser, or even better, add a bash alias like this:

```
alias homeserver='`wget -q -O - domain.com/index.php`'
```

Now you can use *homeserver* inside your terminal as if it would be in your */etc/hosts*.

  

	