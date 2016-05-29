---
title: Installing Kodi (XBMC) on a Raspberry Pi 3
---

I just picked up a Raspberry Pi 3 Model B and figured I'd write a quick how-to on my preferred set up with Kodi as media center, having tried a few configurations with earlier Pi's. All you need is:

- Raspberry Pi 3
- An external keyboard/mouse (I use [this](http://www.amazon.com/Logitech-Wireless-Keyboard-Touchpad-Internet-Connected/dp/B014EUQOGK))
- microSD card
- Computer with microSD card reader/adapter
- HDMI Cable
- Micro USB cable for powering the Pi
- TV

## Tutorial
1. Download [BerryBoot](http://www.berryterminal.com/doku.php/berryboot) and unzip the files to a fresh (FAT formatted) microSD card.
2. Put that microSD card in the Pi
3. Connect the HDMI cable from the Pi to the TV. Turn on the TV.
4. Connect the Pi to any USB power source with the microUSB cable.
5. You should see the Berryboot setup screen appear a few seconds after the big color square shows up on the TV. Use the keyboard to configure the overscan, internet connection, and timezone.
6. At the disk selection screen, choose the option that corresponds to the microSD card. This is usually the first option and should looks something like *mmcblk0: SL16G*. Then click/select the **Format** button.
7. At the Add OS screen, choose openELEC. The download should begin.
8. Once finished, you'll see it on the list. Click the **Set Default** button to have OpenELEC auto-boot when the Pi starts up.
9. Click the little **>>** button in the opper right next to **Exit**, and then click **Edit Config**. Click the **cmdline.txt** tab and change **bootmenutimeout=** from 10 to 3. Then click OK, and then press ESC to reboot.
10. You should now be booted into Kodi with OpenELEC!

From here, you can follow the OpenELEC wizard to guide you through the rest of the setup. You should probably:

- Calibrate the screen by going to **System** > **Settings** > **System** > **Video Calibration...**.
- I like to disable the RSS news feed at the bottom. You can do this at **System** > **Settings** > uncheck **Show RSS news feeds**.

## Thought Process

### Choosing an Operating System
Kodi itself is just an application, so it has to run on top of an operating system. The two most common Linux OS's for running Kodi on the Pi are [OSMC](https://osmc.tv/) and [OpenELEC](http://openelec.tv/home/what-is-openelec). I've used both and prefer OpenELEC as it:

- Has a simple getting started wizard for configuration
- Can be managed from Kodi interface without jumping to a new one
- Better handles automatic updates (IMO)
- Can be installed from Berryboot (next section)

### Deciding to use BerryBoot
The traditional way to install an OS on the Pi is to flash the linux distribution to the microSD card using your computer, and then install from there. I came across BerryBoot, which is itself a tiny bootloader OS that is dedicated to letting you easily download and load multiple operating systems on the Pi. Once BerryBoot is installed, you can:

- Browse, download, and install multiple OS's without a computer
- Have multiple OS's on a single SD card (Raspbian, Kali, RetroPie, etc.)
- Quickly install & experiment with multiple distributions & applications.
- Esily save, restore, and clone configuration of any OS

Since you've got a Pi I assume you like to tinker, and [BerryBoot](http://www.berryterminal.com/doku.php/berryboot) is great way to get a lot more value of the Pi without having to deal with multiple microSD cards. If you  want a dedicated Pi just Kodi, you can change the **bootmenutimeout** to 1 second, or just install OpenELEC the traditional way using other guides on the web.