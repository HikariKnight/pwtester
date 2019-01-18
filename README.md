# HIBPWNED_pwtester
A GUI password tester utilizing the haveibeenpwned API for anonynomously checking if a password has been breached without exposing the password

This python script lets you get a simple GUI for testing passwords in.
The password you type in gets hashed to sha1, then the first 5 characters are fed to the
HaveIBeenPWned Password Checker API to get a list of all breached passwords starting with the
same sha1 range.

Then the program checks the result we get and checks to see if the remainder of the sha1 hash is in the returned list from
HaveIBeenPWned.

__Why a GUI over CLI?__<br/>
I wanted to make something that can be used and understood by normal people using Windows and Mac OSX,
who does not neccessarily understand how to use a CLI program.
Plus there are already several CLI versions of this.

__Why Qt?__<br/>
It is a GUI framework I know inside-out.

__Is this going to steal my password?!__
NO!
The source is fully available and you are free to view it yourself.
* main.py - Main script file, contains less than 80 lines of python3 code and almost line by line explaination of the script
* pwcheck_GUI.ui - User Interface file made in Qt Designer, there is no need for anything super flexible so why waste time programming it?
* LICENSE - The license file, containing your use license for the program
* README.md - Youre reading this file right now
