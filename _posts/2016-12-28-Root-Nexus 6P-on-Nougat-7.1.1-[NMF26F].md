---
title: Rooting Nexus 6P on 7.1.1 [NMF26F]
published: false
---

I looked at a handful of guides, but many pointed to outdated information (such as using ```fastboot oem unlock``` instead of ```fastboot flashing unlock```) which prevents any practical attempt at rooting a vanilla 6P. Here's what worked for me.

This post shows how to:
1. Unlock bootloader
2. Root phone
3. Install TWRP Custom Recovery

##Warning
All data will be wiped clean. All apps, app data, contacts, WhatsApp messages, photos, high scores, etc. Ensure Google is backing up the Android, and do a  WhatsApp backup to Google Drive before proceeding.

##Prereqs
- SuperSU (http://downloadmirror.co/1KuJ/SR5-SuperSU-v2.78-SR5-20161130091551.zip)
- TWRP recovery (https://dl.twrp.me/angler/)
- platform-tools (command-line only is fine)
    + Add platform tools to $PATH

##Steps

###1. Unlock Bootloader
1. Enable Developer Options (tap 'Build Number' repeatedly)
2. Settings > Developer Options > Enable OEM Unlocking
3. Settings > Developer Options > Enable USB Debugging
4. Connect USB cable
5. Enter fastboot mode, either by:
    -  ```adb reboot bootloader``` if still in the Android system
    -  Turning off phone, then hold Power + Volume Down when booting up.
6. ```fastboot flashing unlock```
    - WARNING: This is the step where everything gets deleted. Backup first!
    - Select Yes with the volume up/down buttons, then press power to select.
7. ```fastboot reboot```
8. You may see a message saying 'This device cannot be checked for corruption'. Let the phone reboot - the bootloader is now unlocked! You can ignore that error from now on; it will be there unless the bootloader is locked again.
9. Download the SuperSU ZIP file and ensure that it is the device filesystem - either in /Downloads or on an SD card (if not)

###2. Root phone
1. Enter fastboot mode 
2. ```fastboot flash recovery twrp.img```
3. ```fastboot reboot-recovery```
4. In TWRP, tap Install, browse to the SuperSU ZIP file, and install it.
5. Let the phone reboot.

###3. Flash Recovery (Persistent)
1. Enter fastboot mode 
2. ```fastboot flash recovery twrp.img```
3. ```fastboot reboot```
    - Immediately after the screen turns black to reboot, press and hold Power and Volume Up at the same time to enter recovery mode.
    - You may see a message saying 'This device cannot be checked for corruption'. In that case, wait a few seconds until that message dissappears, and press & hold the Power+Volume Up combo as soon as it does.
4. You should see the phone boot into TWRP recovery. 
5. A "Unmodified System Partition - Keep System Read only" screen appeared. I did 'Swipe to Allow Modifications' so that TWRP could preserve itself in the event of an update.
6. TWRP is ready!

##Sources
- http://www.theandroidsoul.com/nmf26f-root-android-7-1-1-nougat-nexus-6p-5x-pixel-c/
- https://twrp.me/devices/huaweinexus6p.html
- http://www.droidape.com/nexus-6p-recovery-mode/
- https://forum.hovatek.com/thread-10992.html