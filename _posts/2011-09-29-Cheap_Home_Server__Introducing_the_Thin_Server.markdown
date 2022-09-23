---
layout: post
title:  "Cheap Home Server: Introducing the Thin-Server"
date:   2011-09-29 15:40:20 +0000
categories: ['Hardware', 'Linux', 'Server']
legacy_permalink: http://fomori.org/blog/?p=37
---


Cheap Home Server: Introducing the Thin-Server
==============================================

[![](/assets/2011-09-29-Cheap Home Server: Introducing the Thin-Server/630px_thinserver_teaser.jpg "630px_thinserver_teaser")](/assets/2011-09-29-Cheap Home Server: Introducing the Thin-Server/630px_thinserver_teaser.jpg)

A little while ago I finally made the decision that I would like to have a server at home and I was at first fascinated by the [SheevaPlug](http://de.wikipedia.org/wiki/SheevaPlug "SheevaPlug wikipedia"), but many people complained that the [powersupply of it would die](http://chemicaloliver.net/electronics/sheevaplug-why-globalscale-suck/) [within weeks](http://www.newit.co.uk/forum/index.php?topic=353.0), so I needed an alternative but I still didn’t want to use a regular computer because of several disadvantages;

* It would be to loud
* It would consume too much energy
* It would be overkill for my purposes
* The hardware is relatively expensive

But when I had a look on Ebay, I stumbled upon a Thin-Client, which is essentially a small, low power computer, that is used in companies as something like a next-generation terminal. Since it did only cost 50€ I thought I would just give it a try.

[![](/assets/2011-09-29-Cheap Home Server: Introducing the Thin-Server/thinsrv_internal_thumbnail.jpg "thinsrv_internal_thumbnail")](http://fomori.org/blog/wp-content/uploads/2011/09/thinsrv_internal_big.jpg)Hardware porn: Click to enlarge!

The Specs of the Thinclient, a [HP T5710](http://h20000.www2.hp.com/bizsupport/TechSupport/SoftwareIndex.jsp?lang=de&cc=de&prodNameId=439749&prodTypeId=12454&prodSeriesId=439748&swLang=18&taskId=135&swEnvOID=1058 "HP T5710"), are more than suffiecient to run Linux:  

It has a 800MHz [Transmeta Crusoe TM5700](http://de.wikipedia.org/wiki/Transmeta_Crusoe#TM5700 "Transmeta Crusoe TM5700") CPU, which actually is an [VLIW](http://de.wikipedia.org/wiki/VLIW "VLIW") processor, that emulates x86 instructions. That is why it is very energy efficient and doesn’t need active cooling. It has 256MB RAM and an embedded ATI GPU. It also was very important for me that it has 4 USB 2.0 ports, so i could easily attach USB Harddrives and the like. Inside the ThinClient there actually is a little SSD connected to a 1,8″ IDE port. But I would need a (very rare) 1,8″ IDE expansion cable to connect anything to that port and thats why I decided to attach (very professionally using duct tape) an external USB-HDD, instead of the IDE port inside. Also, there is a unused PCI slot, where I could plug in a SATA-controller or something in the future. Sadly this PCI slot is not mounted parallel to the mainboard, so I would need a [riser card](http://en.wikipedia.org/wiki/Riser_card "Riser Card") to plug in anything without sticking out of the enclosure. Furthermore there are audio in- and outputs, a parallel port, a serial port, VGA and of course 100MBit LAN.[![](/assets/2011-09-29-Cheap Home Server: Introducing the Thin-Server/thinsrv_ports.jpg "thinsrv_ports")](/assets/2011-09-29-Cheap Home Server: Introducing the Thin-Server/thinsrv_ports.jpg)

Unfortunately the CPU lacks a single instruction of the 686 instruction set, which actually is the NO-OP instruction. This instruction is used to tell the CPU to do nothing for one cycle, which is probably used to optimize the handling of some interrupts. I actually don’t know why, but this doesn’t seem to make any difference running [arch linux](http://www.archlinux.org/ "Arch Linux"), even though all arch packages are compiled for either i686 or x64 CPUs. (Of course you could just go with any i386 distribution, but I prefer arch linux.)

So I installed arch linux on a external USB harddrive that can be powered by only one USB port by following [the instructions in the arch linux wiki](https://wiki.archlinux.org/index.php/Installing_Arch_Linux_on_a_USB_key "Installing arch linux on a usb key"). I had to use my desktop computer to do so, because the installation didn’t really work on the Thin Client, but I don’t really have a clue why. I just had to [chroot into the new environment to take all the steps from there](https://wiki.archlinux.org/index.php/Install_from_Existing_Linux). After that, there was only one line I had to change in */etc/pacman.conf*, because the processor was not recognized as a 686 CPU and [pacman](https://wiki.archlinux.org/index.php/Pacman) refused to update the system.

```
Architecture = i686
```

[![](/assets/2011-09-29-Cheap Home Server: Introducing the Thin-Server/250px_resized.jpg "250px_resized")](/assets/2011-09-29-Cheap Home Server: Introducing the Thin-Server/250px_resized.jpg)Now i could install all the packages, like samba and subversion to make the server serve me. The little SSD inside provides a little space (~256MB) for making backups, so that not everything is lost, once the HDD dies.

Since I own a [fritz!box](http://www.avm.de/de/Produkte/FRITZBox/FRITZ_Box_Fon_WLAN/index.php "Fritz!box"), I could just attach the ThinServer via LAN and access it via WiFi. Additionally the Fritz!Box supports DynDNS out-of-the-box, so my little server is now available for me from everywhere all the time.

Summary:  

The Thin Server costs only about 50€, is completely silent, can easily handle the load of running a LAMP, sshd, subversion, samba, cups and only consumes about 15W. I’m using it now for almost one year without ever having any troubles. I assume it could be used as a small workstation as well, but I didn’t try to install X on it. And, of course, “recycling” old hardware is good for the environment.

  

	