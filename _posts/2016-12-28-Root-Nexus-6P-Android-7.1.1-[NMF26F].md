---
title: Rooting a Nexus 6P on Android 7.1.1 [NMF26F]
---

I looked at a handful of guides, but many pointed to outdated information (such as using ```fastboot oem unlock``` instead of ```fastboot flashing unlock```) which prevents any practical attempt at rooting a vanilla 6P. Here's what worked for me.

This post shows how to:

1. Unlock bootloader
2. Root phone
3. Install TWRP Custom Recovery

## Warning
- This will delete everything on your phone. All apps, app data, contacts, WhatsApp messages, photos, high scores, etc, downloaded Spotify music, podcasts, YouTube videos, etc.
- You probably want to ensure that Google is properly backing up everything to the cloud, including photos and contacts. If you use WhatsApp, ensure that it is properly backed up to Google Drive before proceeding.
- Modern Google phones (Nexus 6P, Nexus 5X, Pixel) have what is called a 'QFuse' which permanently 'blows' when you unlock the bootloader. After you do this, you will see a message on every boot up that `Your device software can't be checked for corruption. Please lock the bootloader`. More details [here](https://forum.xda-developers.com/nexus-5x/help/to-remove-corruption-warning-message-t3248441).

## How To

### Prerequisites
- Download & Install [Android Command Line Tools](https://developer.android.com/studio/command-line/index.html)
    + Add platform tools to $PATH
- Download [SuperSU](http://www.supersu.com/download)
- Download [TWRP recovery](https://dl.twrp.me/angler/)

Note: Text written `like this` means that it is to be run at a terminal or command line.

### 1. Unlock Bootloader
1. Enable Developer Options (tap 'Build Number' repeatedly)
2. Settings > Developer Options > Enable OEM Unlocking
3. Settings > Developer Options > Enable USB Debugging
4. Connect USB cable
5. Enter fastboot mode, either by:
    -  ```adb reboot bootloader``` if phone is on.
    -  Turning off phone, then hold Power + Volume Down when booting up.
6. ```fastboot flashing unlock```
    - WARNING: This is the step where everything gets deleted. Backup first!
    - Select Yes with the volume up/down buttons, then press power to select.
7. ```fastboot reboot```
8. You may see a message saying 'This device cannot be checked for corruption'. Let the phone reboot - the bootloader is now unlocked! You can ignore that error from now on.
9. Download the SuperSU ZIP file and ensure that it is the device filesystem - either in /Downloads or on an SD card (if not)

### 2. Root phone
1. Enter fastboot mode 
2. ```fastboot flash recovery twrp.img```
3. ```fastboot reboot-recovery```
4. In TWRP, tap Install, browse to the SuperSU ZIP file, and install it.
5. Let the phone reboot.

### 3. Flash Recovery (Persistent)
1. Enter fastboot mode 
2. ```fastboot flash recovery twrp.img```
3. ```fastboot reboot```
    - Immediately after the screen turns black to reboot, press and hold Power and Volume Up at the same time to enter recovery mode.
    - You may see a message saying 'This device cannot be checked for corruption'. In that case, wait a few seconds until that message disappears, and press & hold the Power+Volume Up combo as soon as it does.
4. You should see the phone boot into TWRP recovery. 
5. A "Unmodified System Partition - Keep System Read only" screen appeared. I did 'Swipe to Allow Modifications' so that TWRP could preserve itself in the event of an update.
6. TWRP is ready!

## Sources
- [http://www.theandroidsoul.com/nmf26f-root-android-7-1-1-nougat-nexus-6p-5x-pixel-c/](http://www.theandroidsoul.com/nmf26f-root-android-7-1-1-nougat-nexus-6p-5x-pixel-c/)
- [https://twrp.me/devices/huaweinexus6p.html](https://twrp.me/devices/huaweinexus6p.html)
- [http://www.droidape.com/nexus-6p-recovery-mode/](http://www.droidape.com/nexus-6p-recovery-mode/)
- [https://forum.hovatek.com/thread-10992.html](https://forum.hovatek.com/thread-10992.html)