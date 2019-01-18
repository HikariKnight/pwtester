# HIBPWNED_pwtester
A GUI password tester utilizing the haveibeenpwned API for anonynomously checking if a password has been breached without exposing the password

This python script lets you get a simple GUI for testing passwords in.
The password you type in gets hashed to sha1, then the first 5 characters are fed to the
HaveIBeenPWned Password Checker API to get a list of all breached passwords starting with the
same sha1 range.

Then the program checks the result we get and checks to see if the remainder of the sha1 hash is in the returned list from
HaveIBeenPWned.

For more information, check out Troy Hunt's blogpost here: [here](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/)<br/>
Note: Troy Hunt is the owner of [haveibeenpwned](https://haveibeenpwned.com)

**Why a GUI over CLI?**<br/>
I wanted to make something that can be used and understood by normal people using Windows and Mac OSX,
who does not neccessarily understand how to use a CLI program.
Plus there are already several CLI versions of this.

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
