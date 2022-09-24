---
layout: post
title:  "Repair the Syma X12S quadcopter by replacing the motors and rotor blades (and what to do if it does not lift off afterwards)"
date:   2015-10-19 21:21:36 +0000
categories: ['Handycrafts', 'Hardware']
author: 6arms1leg
legacy_permalink: http://fomori.org/blog/?p=1237
---


[![Syma X12S quadcopter with new motors](/assets/images/Cover-300x213.png)](http://fomori.org/blog/wp-content/uploads/2015/10/Cover.png)My friend owns a Syma X12S [quadcopter](https://en.wikipedia.org/wiki/Quadcopter "en.wikipedia.org - quadcopter") that was cheaply imported from China. It really is an amazing piece of hardware and the perfect entertainment when you spend an evening with friends. Piloting this miniature aircraft is quite easy – it only takes a few flying sessions until you acquired enough skills to handle it. However, I still managed to crash the quadcopter in a way that damaged two of its four motors. The beauty of this toy is its modular design: Even though it is a cheap product, most of the parts are [LRU](https://en.wikipedia.org/wiki/Line-replaceable_unit "en.wikipedia.org - Line-replaceable unit")s, so you can simply order a replacement for the defect part and replace it yourself.  

This short post shows how to replace the motors of a Syma X12S quadcopter and highlights some difficulties to look out for.

Replacing the motors
====================

The Syma X12S quadcopter has two pairs of motors, two spinning in one direction and two spinning in the opposite direction. Both motor pairs are placed diagonally in the quadcopter mount positions (see items 04 and 05 in the exploded assembly drawing below). This design concept accounts for the spin moment of each rotor, assuring an equilibrium on the overall spin moment.

[![Exploded assembly drawing - modular design](/assets/images/Exploded-assembly-drawing-237x300.png)](http://fomori.org/blog/wp-content/uploads/2015/10/Exploded-assembly-drawing.png)Replacing any part of this quadcopter model is straight forward, even for people that are not so technically gifted: The only tools needed are a small [Phillips screw drive](https://en.wikipedia.org/wiki/List_of_screw_drives "en.wikipedia.org - List of screw drives") and basic soldering equipment. To get access to the motors you only need to remove three parts. First, the rotor blades of the motors need to be removed:

[![Rotor blades removed](/assets/images/Rotor-blades-removed-300x283.png)](http://fomori.org/blog/wp-content/uploads/2015/10/Rotor-blades-removed.png)They are simply pushed onto the motor shaft, creating a frictional connection. So just reverse the process by pulling them off again. Do not pull on the blades, as they bend and break easily. Instead grab the rotors at the hub.

Next, the bottom cover plate needs to be removed, which is held in place by four screws:

[![Buttom cover plate](/assets/images/Buttom-cover-plate-300x198.png)](http://fomori.org/blog/wp-content/uploads/2015/10/Buttom-cover-plate.png)Then, remove the chassis parts that cover each motor, which serve as a rotor blade protection and landing gear. Only remove the one(s) on the motor(s) you want to replace. This is probably the most delicate step: Theses parts are kept in place by two tiny clips each. Removing the part without breaking the clips requires a little patience and a steady hand – I ripped one off right away. If you break one of the clips, the part will not be held in place anymore after reassembly (later in this guide). Applying adhesive or a tiny drop of [hot glue](https://en.wikipedia.org/wiki/Hot-melt_adhesive "en.wikipedia.org - Hot-melt adhesive") will fix this.

[![Quadcopter opened and ready for motor repair](/assets/images/Quadcopter-opened-282x300.png)](http://fomori.org/blog/wp-content/uploads/2015/10/Quadcopter-opened.png)The Picture above shows the motors ready for removal. They are simply pushed into the chassis (no adhesive is applied) and the two wires are soldered to the [PCB](https://en.wikipedia.org/wiki/Printed_circuit_board "en.wikipedia.org - Printed circuit board"). When replacing the motors, make sure to swap it with the correct motor type (The “normal” or counter-spinning motors can easily be distinguished by their wire coloring).

[![Motor close-up](/assets/images/Motor-300x208.png)](http://fomori.org/blog/wp-content/uploads/2015/10/Motor.png)Finally, reverse the steps above to reassemble the quadcopter again.

Difficulties to look out for
============================

### Never rotate the rotors manually

Rotating the motors manually (with your hand or by blowing on the blades) should be avoided. Manually rotating electrical motors [induces voltage](https://en.wikipedia.org/wiki/Electromagnetic_induction "en.wikipedia.org - Electromagnetic induction") in the circuity. Although most (good) circuits have protection against this phenomenon, it is good practice not to do so.

### Motor cable length

The length of the cables is just enough to push the motors into the mounting positions in the chassis *after* soldering the wires. However, twisting them is not possible then, which makes the bottom cover plate not fit that easily anymore. So ideally, install the motors first and solder the wires last.

### Rotor blade form

Your quadcopter does not lift off after repairing?

Since there are two different motor types spinning in different directions, it is clear that they need different rotor blade forms to create lift (see the exploded assembly drawing shown earlier in this post). The shipped rotor blades came in two different colors (black and white) so I thought that each color marked one of the two rotor forms – why else would there be two black and two white rotors? Well, this was not the case. The rotor color has nothing to do with its form! That was quite confusing to me. So make sure to fit the right rotor blades on each motor.

  

	