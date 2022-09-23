---
layout: post
title:  "Samsung SSD 840 EVO 2.5 Zoll SATA – Firmware update under GNU/Linux"
date:   2014-04-06 13:28:07 +0000
categories: ['Hack', 'Hardware', 'Linux', 'Mod', 'Software']
legacy_permalink: http://fomori.org/blog/?p=933
---


Samsung SSD 840 EVO 2.5 Zoll SATA – Firmware update under GNU/Linux
===================================================================

I recently bought a Samsung SSD to replace my HDD in my [Arch Linux](https://www.archlinux.org/ "archlinux.org") notebook. It is a “Samsung SSD 840 EVO 2.5 Zoll SATA”. One of the first things I do when I get new hardware is to make sure the latest firmware is installed. Mine did not have the latest firmware update and – as it was to expect – Samsung SSD firmware updates under GNU/Linux are not (officially) supported. Samsung ships only Microsoft Windows software, called “Magician”, which can directly update the firmware or create a [live USB-Stick](https://en.wikipedia.org/wiki/Live_USB "wikipedia.org - Live USB") to do the update. Additionally, they provide *.iso image files (one for Microsoft Windows systems and one for Apple computer, respectively) to update the firmware from a [live CD](https://en.wikipedia.org/wiki/Live_CD "wikipedia.org - Live CD"). The *.iso image file intended for Microsoft Windows would also work under GNU/Linux, only that my notebook does not have a CD Drive anymore. Obvioulsy, the only option left was to create my own live USB-Stick under GNU/Linux – without using Microsoft Windows and that crappy Samsung “Magician” software. A simple “dd” comand to “burn” the *.iso file on an USB-Stick did not do the trick, as the [Isolinux](https://en.wikipedia.org/wiki/SYSLINUX "wikipedia.org - Syslinux") version Samsung uses is over 10 years (!) old.

This article shows how to update the firmware of a “Samsung SSD 840 EVO 2.5 Zoll SATA” under GNU/Linux using a bootable live USB-Stick.

WARNING! The following method should work but is not (officially) supported by Samsung. Do at your own risk! You could brick your device or lose all your data on it. Make sure to backup all your data! Also backup all data you have on the USB-Stick used for the firmware update!  

You read the WARNING above and are still brave enough to try the firmware update under GNU/Linux? Good, that’s the spirit! However, if you happen to have Mircosoft Windows installed or a CD Drive I would recommend using one of the official methods available.

First, check your firmware vesion. Issue

```
$ dmesg
```

to find out under which device your SSD registered. To check the firmware version (“FwRev=…”), issue:

```
$ sudo hdparm -i /dev/sdX | grep FwRev
```

Replace “sdX” with your actual device name.

Now go to [Samsung’s download website](http://www.samsung.com/de/support/model/MZ-7TE120BW-downloads "samsung.com - SSD 840 EVO Downloads") to find the newest firmware available. If you already have the latest version you can stop right here.

Otherwise, download the firmware (Microsoft Windows *.iso image file) and proceed by zero-ing the USB-Stick you wish to use for the update. Find the device name by plugging in your USB-Stick and issue:

```
$ dmesg
```

The following command will overwrite the first 512 bytes of the USB-Stick with zeros in order to remove any potentially meta-information (MBR, partition table):

WARNING! You will lose all your data stored on the USB-Stick!

```
$ sudo dd count=1 bs=512 if=/dev/zero of=/dev/sdX && sync
```

Again, replace “sdX” with your actual device name.

Partition the USB-Stick (replace “sdX” with your device name):

```
$ sudo parted /dev/sdX
(parted) print # shows some information, including the current partition table (which should be non-existant)
(parted) mklabel msdos
(parted) mkpart primary ext2 0% 100%
(parted) set 1 boot on
(parted) print # check, if you partitioned the USB-Stick correctly
(parted) quit
```

Format the USB-Stick(replace “sdX1″ with your device name):

```
$ sudo mke2fs -t ext2 -L ssdfirmware /dev/sdX1
```

Now, mount the Samsung firmware *.iso file and the newly formatted USB-Stick (replace “sdX1″ with your device name, “SAMSUNGFIRMWARE.iso” with the correct file name and “MOUNTPOINT1″ and “MOUNTPOINT2″ with the actual mountpoints):

```
$ sudo mount -o loop -o exec SAMSUNGFIRMWARE.iso /MOUNTPOINT1
$ sudo mount /dev/sdX1 /MOUNTPOINT2
```

The final step of preparation is to install Syslinux and the Samsung firmware update files to the USB-Stick. (Again, replace “sdX” with your device name and “MOUNTPOINT1″ and “MOUNTPOINT2″ with the actual mountpoints.) Note that below source paths for Syslinux are from an Arch Linux installation. These Syslinux source paths might be different, depending on your GNU/Linux distribution. Adjust the paths accordingly or simply use the files and binaries from the Syslinux source package (they can be obtained from [here](http://www.syslinux.org/wiki/index.php/Download "syslinux.org - Download") and work without installation). Issue:

```
$ sudo mkdir MOUNTPOINT2/syslinux
$ sudo cp -r /usr/lib/syslinux/bios/*.c32 /MOUNTPOINT2/syslinux/
$ sudo extlinux --install /MOUTPOINT2/syslinux
$ sudo dd bs=440 count=1 conv=notrunc if=/usr/lib/syslinux/bios/mbr.bin of=/dev/sdX
$ sudo cp -v -r --remove-destination /MOUNTPOINT1/isolinux/isolinux.cfg /MOUNTPOINT2/syslinux/syslinux.cfg
$ sudo cp -v -r --remove-destination /MOUNTPOINT1/isolinux/memdisk /MOUNTPOINT2/syslinux/
$ sudo cp -v -r --remove-destination /MOUNTPOINT1/isolinux/btdsk.img /MOUNTPOINT2/syslinux/BTDSK.IMG
$ sudo sync
$ sudo umount MOUNTPOINT2
$ sudo umount MOUNTPOINT1
```

WARNING! As mentioned in the warnings obove, you do this on your own risk! Furthermore, if you are using a notebook, make sure that it is on AC! A powerloss during the firmware update would probably be fatal!

Now, do the firmware update using the USB-Stick… (Follow the instructions on the screen.)

If you get a failure message, saying that the update was unsuccessful, do not worry – it should work anyway, as you will see…

When you check the firmware version under GNU/Linux again, by entering (replace “sdX” with your device name):

```
$ sudo hdparm -i /dev/sdX | grep FwRev
```

you should see that the firmware was successfully updated. Arrr, I love it when things work without Microsoft Windows!

 

  

	