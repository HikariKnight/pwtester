#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:09:23 2019

@author: Ove Andreas
"""

import sys
import os
import os.path
import re
import hashlib
from urllib.request import urlopen, Request
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from PyQt5 import uic

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

class PasswordCheck(QMainWindow):
    def __init__(self, parent=None):
        super(PasswordCheck, self).__init__(parent)
        # Load ui from pwcheck_GUI.ui
        uic.loadUi("{}/{}".format(get_script_path(),'pwcheck_GUI.ui'), self)
        self.aboutButton.clicked.connect(self.aboutClicked)
        self.okButton.clicked.connect(self.okClicked)
        self.passwordEdit.returnPressed.connect(self.okClicked)
        self.passwordEdit.setFocus()
        self.show()
        
    def okClicked(self):
        # Hash the password to sha1 so we can test it with the HIBPWNED api
        sha1 = hashlib.sha1(str(self.passwordEdit.text()).encode())
        pw = sha1.hexdigest().upper()
        
        # Open the API and get the list of all sha1 encrypted passwords that matches the first 5 characters of our sha1 password
        # an user agent is set so we can actually get the results as the page returns a forbidden error when no user agent is set
        breaches = urlopen(Request("https://api.pwnedpasswords.com/range/{}".format(pw[:5]),headers={'User-Agent': 'Mozilla'}))
        breachedHashes = breaches.read().decode("utf-8")
        
        # Check the list we got from the API to see if the remainder of our sha1 hash is in it
        testfor = re.compile("{}:{}".format(pw[5:],"\d+"))
        if testfor.search(breachedHashes):
            # If we find our password, warn the user
            QMessageBox.warning(self, 'PASSWORD BREACHED!', "The password you have entered has been found in a known breach!\nAvoid using the password you just tested at all cost!", QMessageBox.Ok)
            breachInfo = testfor.search(breachedHashes)
            breachCount = breachInfo.group().split(":")
            
            # Show the user how many times the password has been found in data breaches
            self.resultLbl.setText('<html><head/><body><p>Result:<br/><span style=" color:#ff0004;">Password has been found in {} breaches!</span></p></body></html>'.format(breachCount[1]))
        else:
            # If we do not find our sha1 password in the list, show the user that it has not showed up in any known breaches
            self.resultLbl.setText('<html><head/><body><p>Result:<br/><span style=" color:#08a700;">Password not found in any known breaches.</span></p></body></html>')
        
    
    def aboutClicked(self):
        # Display information about the small program
        QMessageBox.information(self, 'Password Tester', "A small open source program written in Python by Ove\n to check if a password has been in any known breaches\nreported to haveibeenpwned.com\n\nThe password typed in is encrypted and not exposed to haveibeenpwned, only the first 5 characters of the\nencrypted password is exposed to the API,\nthe program then checks the list from HIBPWNED\nif the remaining part is in the database.", QMessageBox.Ok)
            
            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ui = PasswordCheck()
    sys.exit(app.exec_())
