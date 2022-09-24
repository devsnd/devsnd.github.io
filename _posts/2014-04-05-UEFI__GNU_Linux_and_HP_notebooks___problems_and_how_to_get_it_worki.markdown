---
layout: post
title:  "UEFI, GNU/Linux and HP notebooks – problems and how to get it worki"
date:   2014-04-05 15:10:51 +0000
categories: ['Arch Linux', 'Hack', 'Hardware', 'Linux', 'Mod']
author: 6arms1leg
legacy_permalink: http://fomori.org/blog/?p=892
---


UEFI, GNU/Linux and HP notebooks – problems and how to get it working
=====================================================================

There is a lot of confusion and wrong information in the internet about the [Unified Extensible Firmware Interface (UEFI)](https://en.wikipedia.org/wiki/Uefi "en.wikipedia.org - UEFI") and how to set it up correctly – especially under GNU/Linux. What makes things worse and also confused me a lot is that all vendors tend to implement this “standard” differently. So although UEFI is defined as a new industry standard replacing the [BIOS](https://en.wikipedia.org/wiki/BIOS "en.wikipedia.org - BIOS"), it can hardly be called “standard” at this time. Yet another problem of understanding UEFI is, that people seem to mix up words that have a special meaning.

My old notebook still uses the old BIOS-MBR setup, not capable of any UEFI fancy-ness. But it is dying, so I recently bought a new one. It is an “HP EliteBook 840 G1″. I used that opportunity to familiarize myself with UEFI and GNU/Linux.

This article explains two things (only taking [GPT](https://en.wikipedia.org/wiki/GUID_Partition_Table "en.wikipedia.org - GPT") setups into account):

* How is UEFI implemented in practice and set up with GNU/Linux?
* How to set up UEFI and GNU/Linux on HP notebooks?

How is UEFI implemented in practice and set up with GNU/Linux?

First, you should read [some general information about UEFI](https://en.wikipedia.org/wiki/Uefi "en.wikipedia.org - UEFI"), if you are new to it. (You should read this, if you do not fully understand the following paragraphs.)

The vocabulary for UEFI terms used on the internet is very confusing and often wrong. People often use one term, e.g. “BIOS” or “boot manager”, to refer to different things. When they use the word “BIOS”, they sometimes actually mean BIOS, a few lines later they using the same word to refer to the “UEFI pre-boot graphical environment” – bad practice and simply wrong. The word “boot manager” is even more problematic, as with UEFI there actually is more than one boot manager (in contrast to BIOS-MBR systems). I will try to explain (simplisticly) how an UEFI-GPT setup is generally implemented with GNU/Linux while defining UEFI specific terms for this article. Hopefully, this will give the reader a clearer view of UEFI and GNU/Linux.

When setting up an UEFI system with GNU/Linux we need to know about two things:

* An “[EFI System Partition (ESP)](https://en.wikipedia.org/wiki/EFI_System_partition "en.wikipedia.org - ESP")“
* [UEFI NVRAM](https://en.wikipedia.org/wiki/NVRAM "en.wikipedia.org - NVRAM") settings

The ESP is a regular partition in the main (GPT) partition table of your HDD/SSD with a FAT32 filesystem. It should be 512 MiB in size, although smaller or bigger sizes are possible. The partition type code should be “ef00″ (using “[gdisk](https://github.com/caldwell/gdisk "github.com - gdisk")“, with “[parted](https://www.gnu.org/software/parted/ "gnu.org - parted")” you have to set the bootable flag instead). On this ESP, the UEFI applications are saved. These UEFI applications usually are the Operating System (OS) boot loaders (e.g. [GRUB](https://www.gnu.org/software/grub/ "gnu.org - grub"), [ELILO](http://elilo.sourceforge.net/ "elilo.sourceforge.net") or Mircosoft Windows Boot Loader), but can be applications for memory testing or interactive Shells as well. I intentionally use the word “saved”: There is no much of an installation process – the UEFI applications can just be copied manaully (e.g. using “cp”) to the right paths (just keep in mind possibly hard coded paths within the UEFI applications). The applications are saved by honoring the following path scheme (e.g. on a [x86-64](https://en.wikipedia.org/wiki/X86-64 "en.wikipedia.org - X86-64") architecture):

```
\EFI\APPNAME\APPNAMEx64.efi
```

Where “APPNAME” is a descriptive name, you can freely choose. Note that noramally upper or lower case letters do not matter, since FAT32 filesystems are case-insensitive (unless [UFT-8](https://en.wikipedia.org/wiki/UTF-8 "en.wikipedia.org - UTF-8") encoding is explicitly used). Also note the use of backslashs, as UEFI internally uses backslashs. Under GNU/Linux, of course, use normal slashs. The backslashs only are important when defining paths within the UEFI pre-boot graphical environment or the UEFI shell. Additionally, a few standard paths are defined (but do not have to exist on your ESP):

```
\EFI\Boot\Bootx64.efi # for starting a generic OS boot loader, e.g. on a Live-CD
```

```
\EFI\Microsoft\Boot\bootmgfw.efi # not really a standard path, but still honored by most computer vendors because Microsoft Windows uses it
```

```
\Shellx64.efi # UEFI expects an interactive UEFI shell here
```

On an UEFI system you have to distinguish between two different kinds of boot loaders: the OS boot loader already mentioned above (UEFI application) and the UEFI boot loader, which launches the specified UEFI application. The UEFI boot loader is controlled via the UEFI NVRAM settings.

To configure the UEFI boot loader you have to change the variables in the UEFI NVRAM. This can be done in the running OS. In GNU/Linux this can be achieved using the “efibootmgr” program. Just typing:

```
$ sudo efibootmgr
```

should show the current UEFI boot manager settings. With this tool you can add and remove boot entries and adjust the boot oder. Every UEFI application copied to the ESP should be added to the UEFI NVRAM.

Note that most GNU/Linux OS boot laoders will do both during their installation, copy their UEFI application to the right place on your ESP and add an entry to your UEFI NVRAM – as long as an ESP already exists.

Now, what if you can simply configure the boot order in the BIOS-like UEFI pre-boot graphical environment – just as you could change it in the BIOS before, with your BIOS-MBR system? Well, lucky you! When saying “changing s.th. in the BIOS” (on a BIOS-MBR system), we usually meant entering the graphical environment by pressing a certain key after switching on the computer and change some values there. The UEFI standard, however, does not define such a graphical environment. But for convenience, most computer vendors add such a BIOS-like UEFI pre-boot graphical environment to aid the transition from traditional BIOS systems to UEFI. Such a system then auto-detects applications on your ESP, adds them to the boot order and lets you configure it just as you would on your old BIOS-based system.

Now, this is the problem: Although UEFI itself defines a standard, the actual implementation of UEFI by the different computer vendors is far from standardized. They do as they like and thus every computer acts differently. This point gave me a hard time figuring out how to configure my new notebook.

### Short summary

To get your UEFI-based system to boot GNU/Linux you have to:

* set up an ESP
* copy the UEFI applications to it
* change the UEFI NVRAM variables

Note that the last two points are normally done automatically when installing certain OS boot loaders (e.g. GRUB).

Also note that althought this is very easy and straight forward to set up, it often creates problems, because computer vendors implement certain functions differently and deviate from the UEFI standard (see next section).

How to set up UEFI and GNU/Linux on HP Notebooks?
=================================================

As mentioned above, I bought a new HP notebook (HP EliteBook 840 G1), which gave me a lot of trouble when trying to set it up with UEFI and GNU/Linux. The notebook just did not want to boot [my favourite GNU/Linux distribution, Arch Linux](https://www.archlinux.org/ "archlinux.org"), although everything was installed and configured correctly. It took me quite a while to understand HP’s rather studip implementation of UEFI. While investigating that issue, I found that quite a lot people had similar problems with their HP notebooks (although different models). So this seems to affect all kinds of HP notebooks. This section covers troubleshooting and workarounds of UEFI boot problems with HP notebooks (esp. HP EliteBook 840 G1).

First, make sure you have the latest firmware installed. Things have gotten a lot better with the last fimrware updates.

I installed Arch Linux with GRUB on my HP EliteBook. I set up the ESP beforehand and GRUB installed it’s UEFI application to it and added an UEFI NVRAM entry just fine. Still the notebook refused to boot. So the regular way did not work. The problem was that HP hard coded the path for the OS boot manager in their UEFI boot manager to

```
\EFI\Microsoft\Boot\bootmgfw.efi
```

to boot Microsoft Windows, regardless of how you changed the UEFI NVRAM variables. So when setting the device boot order in the UEFI pre-boot graphical environment of HP to boot from the first HDD/SSD by selecting “OS Boot Manager” it expects to boot Microsoft Windows (only!) from above mentioned path. The only workaround was to change the UEFI application path of the OS boot loader to that hard coded path.

On your ESP (e.g. $MOUNTPOINT=/boot/efi), do (e.g. GRUB on Arch Linux):

```
$ sudo mkdir -p $MOUNTPOINT/EFI/Microsoft/Boot
$ sudo cp $MOUNTPOINT/EFI/grub_archlinux/grubx64.efi $MOUNTPOINT/EFI/Microsoft/Boot/bootmgfw.efi
```

After that, GRUB loaded as expected. This was far from perfect, as it obviously would create conflicts in a dual boot setup with Microsoft Windows. Also, everytime you installed GRUB, you had to remmeber to copy it over to the hard coded path. (Admittedly, you do not install GRUB that often, though.)

A later HP firmware update made things much better. The above path was still hard coded, but at least they added the UEFI standard path (also hard coded):

```
\EFI\Boot\Bootx64.efi
```

Now, at least you could have both, a GNU/Linux OS boot loader and Microsoft Windows OS boot loader in their own places. Although I did not try which loads first.

But the real improvement is, that the new HP firmware allows defining a “Customized Boot” path in the UEFI pre-boot graphical environment:

Select the “Customized Boot” option in the UEFI pre-boot graphical environment under “Boot Optoins” and set the path to:

```
\EFI\grub_archlinux\grubx64.efi
```

and adjust the device boot order (also in the UEFI pre-boot graphical environment) to boot this entry first.

This seems to be the best (acceptable) solution so far. Why HP hard codes these paths in the first place and names them “OS Boot Manager”, is beyond me. Also, I do not understand why most computer vendors in general deviate from the UEFI standard – it gives users a hard time figuring out what is wrong. It defeats the very purpose of a standard!

Other souces:
=============

* [Arch Linux forum post](https://bbs.archlinux.org/viewtopic.php?id=168904&p=1 "Arch Linux forum post")
* [HP forum post](http://h30434.www3.hp.com/t5/Notebook-Operating-Systems-and-Software/Changing-Boot-Order-on-Dual-Boot-Windows-8-and-Ubuntu/td-p/2503733 "HP forum post")

 

  

	