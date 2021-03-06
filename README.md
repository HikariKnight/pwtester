# pwtester
(An anonynomous HaveIBeenPwned Password Tester)<br/>
A GUI password tester utilizing the haveibeenpwned API for anonynomously checking if a password has been breached without exposing the password

This python (and golang) script lets you get a simple GUI for testing passwords in.
The password you type in gets hashed to sha1, then the first 5 characters are fed to the
HaveIBeenPWned Password Checker API to get a list of all breached passwords starting with the
same sha1 range.

Then the program checks the result we get and checks to see if the remainder of the sha1 hash is in the returned list from
HaveIBeenPWned.

For more information, check out Troy Hunt's blogpost here: [here](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/)<br/>
Note: Troy Hunt is the creator of [haveibeenpwned](https://haveibeenpwned.com)

![image of a non compromised password](https://i.imgur.com/WOPa0XO.png)
![example of when a password is confirmed as compromised by the API results](https://i.imgur.com/GP0GTDA.png)
![image of a compromised password](https://i.imgur.com/zbyPfL0.png)


**Why a GUI over CLI?**<br/>
I wanted to make something that can be used and understood by normal people using Windows and Mac OSX,
who does not neccessarily understand how to use a CLI program.
Plus there are already several CLI scripts and programs that interfaces with the pwnedpasswords API.

**Why Qt?**<br/>
It is a GUI framework I know inside-out.

**Is this going to steal my password?!**<br/>
NO!
The source is fully available and you are free to view it yourself.
* main.py - Main script file, contains less than 80 lines of python3 code and almost line by line explaination of the script
* pwcheck_GUI.ui - User Interface file made in Qt Designer, there is no need for anything super flexible so why waste time programming it?
* LICENSE - The license file, containing your use license for the program
* README.md - Youre reading this file right now

**Install instructions for Windows and MacOSX**<br/>
1. Download the binary for your platform from: https://github.com/HikariKnight/pwtester/releases
2. Unzip/Extract the files from the archive you downloaded
3. Run the Password Tester executable

**Install instructions for Linux (or run from source if you have python3 and git installed)**<br/>
```
git clone https://github.com/hikariknight/pwtester.git
cd pwtester
pip3 install wheel PyQt certifi
python3 main.py
```

**Build instructions for golang version**<br/>
1. Setup golang and the [Qt bindings for golang](https://github.com/therecipe/qt/wiki/Installation)
2. Once that is set up, run the commands below
   ```
   mkdir ~/go/devel
   git clone https://github.com/hikariknight/pwtester.git ~/go/devel/pwtester
   cd ~/go/devel/pwtester
   ```
3. Build for your platform
   Linux and MacOS
   ```
   ~/go/bin/qtdeploy build desktop

   ```
   Note: If you run linux and want to build for linux and windows just run `./build_go-bins.sh`
   <br/><br/>
   Windows:
   ```
   qtdeploy -ldflags -H=windowsgui build desktop
   ```