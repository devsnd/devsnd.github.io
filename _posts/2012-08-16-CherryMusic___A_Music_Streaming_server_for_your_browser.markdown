---
layout: post
title:  "CherryMusic – A Music Streaming server for your browser"
date:   2012-08-16 18:13:17 +0000
categories: ['Audio', 'Programming', 'Python', 'Server']
legacy_permalink: http://fomori.org/blog/?p=431
---


CherryMusic – A Music Streaming server for your browser
=======================================================

**This post is quite old. CherryMusic has improved a lot since then. For the latest version and information on CherryMusic, please visit [http://fomori.org/cherrymusic](http://fomori.org/cherrymusic "http://fomori.org/cherrymusic")**

---

[![](/assets/2012-08-16-CherryMusic___A_Music_Streaming_server_for_your_browser/cherry_music_web_notext-e1345133282430.jpg "cherry_music_web_notext")](http://fomori.org/blog/wp-content/uploads/2012/08/cherry_music_web_notext.jpg)I recently wrote a Music Streaming Server in python, that allows you to listen to your music inside a browser, no matter where you are. It is called CherryMusic and features a standalone webserver based on [cherryPy](http://cherrypy.org) as well as [JPlayer](http://jplayer.org), a HTML5/Flash music player. It indexes your data for fast search using a sqlite database, so there is nothing to setup for you, just download the sources and off it goes!

In my tests it works perfectly with many thousand indexed files: searches are returned immediately, even on [my  little home server](http://fomori.org/blog/blog/2011/09/29/cheap-home-server-introducing-the-thin-server/ "Cheap Home Server: Introducing the Thin-Server").

You can download the [sources from github](http://github.com/devsnd/cherrymusic) or [download them directly from the projects page](http://fomori.org/cherrymusic/). Any suggestions for improvement are welcome.

After the break you can find some screenshots of it in action.

As you see, it is very minimalistic. You can click on the screen shots to view them in full resolution.

[![](/assets/2012-08-16-CherryMusic___A_Music_Streaming_server_for_your_browser/time1345133898-300x232.png "time1345133898")](http://fomori.org/blog/wp-content/uploads/2012/08/time1345133898.png)This is the search/main window. There are just 3 Tabs for all functionality. The Player always stays on top.

[![](/assets/2012-08-16-CherryMusic___A_Music_Streaming_server_for_your_browser/time1345133928-300x232.png "time1345133928")](http://fomori.org/blog/wp-content/uploads/2012/08/time1345133928.png)Once you’ve entered you search terms, you will get a list of folders and files. Each folder is expandable right in place.

[![](/assets/2012-08-16-CherryMusic___A_Music_Streaming_server_for_your_browser/time1345133951-300x230.png "time1345133951")](http://fomori.org/blog/wp-content/uploads/2012/08/time1345133951.png)This is the Playlist view. Nothing special.

[![](/assets/2012-08-16-CherryMusic___A_Music_Streaming_server_for_your_browser/time1345133998-300x240.png "time1345133998")](http://fomori.org/blog/wp-content/uploads/2012/08/time1345133998.png)There is also a view for browsing your files. If there are too many files you will only see the first letter, which in turn you can expand to see all files starting with that letter.

  

	