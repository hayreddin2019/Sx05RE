**Sx05RE**
An emulation fork for Sx05 devices, Most of the code is from [Kszaq's LE](https://github.com/kszaq/LibreELEC.tv) and [Lakka](https://github.com/libretro/Lakka-LibreELEC), I just combine them with some changes, add Emulationstation and some standalone emulators (Advancemame, PPSSPP, Reicast). 

To build use:  

sudo apt update && sudo apt upgrade  
sudo apt install gcc make git gcc-multilib lib32stdc++6  
sudo dpkg-reconfigure dash (select no, to install bash as the default)  
git clone https://github.com/shantigilbert/LibreELEC.tv.git Sx05RE  
cd Sx05RE  
make image PROJECT=S905 ARCH=arm DISTRO=Sx05RE  

or if you have a 1GB device  
make image PROJECT=S905_1GB ARCH=arm DISTRO=Sx05RE  


# LibreELEC

LibreELEC is a 'Just enough OS' Linux distribution for running the award-winning [Kodi](http://kodi.tv) software on popular mediacentre hardware. LibreELEC is a conservative fork of the popular [OpenELEC](http://openelec.tv) project with a stronger focus on pre-release testing and post-release change management. Further information on the project can be found on the [LibreELEC website](https://libreelec.tv).

**Issues & Support**

Please report issues via the [LibreELEC forum: Bug Reports](http://forum.libreelec.tv/forum-35.html). Please ask support questions in the [LibreELEC forum: Help & Support](http://forum.libreelec.tv/forum-3.html) or ask a member of project staff in the #libreelec IRC channel on Freenode.

**Donations**

Contributions towards current project funding goals can be sent via PayPal to donations@libreelec.tv

**License**

LibreELEC original code is released under [GPLv2](http://www.gnu.org/licenses/gpl-2.0.html).

**Copyright**

As LibreELEC includes code from many upstream projects it includes many copyright owners. LibreELEC makes NO claim of copyright on any upstream code. However all original LibreELEC authored code is copyright LibreELEC.tv. For a complete copyright list please checkout the source code to examine license headers. Unless expressly stated otherwise all code submitted to the LibreELEC project (in any form) is licensed under [GPLv2](http://www.gnu.org/licenses/gpl-2.0.html) and copyright is donated to LibreELEC.tv. This approach allows the project to stay manageable in the long term by giving us freedom to maintain the code as part of the whole without the management overhead of preserving contact with every submitter, e.g. GPLv3. You are absolutely free to retain copyright. To retain copyright simply add a copyright header to each submitted code page. If you submit code that is not your own work it is your responsibility to place a header stating the copyright.
