#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:09:23 2019

@author: Ove Andreas
"""

# Import libraries we use
import sys
import os
import os.path
import re
import hashlib
import ssl
from urllib.request import urlopen, Request
from qtpy.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from qtpy import uic


# Function to get the script path
def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


# Main
class PasswordCheck(QMainWindow):
    def __init__(self, parent=None):
        super(PasswordCheck, self).__init__(parent)
        # Load ui from pwcheck_GUI.ui
        uic.loadUi("{}/{}".format(get_script_path(), 'pwcheck_GUI.ui'), self)

        # Connect buttons to functions
        self.aboutButton.clicked.connect(self.aboutClicked)
        self.okButton.clicked.connect(self.okClicked)
        self.passwordEdit.returnPressed.connect(self.okClicked)

        # Give focus to the password box
        self.passwordEdit.setFocus()

        # Show the GUI
        self.show()

    def okClicked(self):
        # Hash the password to sha1 so we can test it with the HIBPWNED api
        sha1 = hashlib.sha1(str(self.passwordEdit.text()).encode())
        pw = sha1.hexdigest().upper()

        # Make an ssl context so we can communicate over https
        ssl_context = ssl.SSLContext()

        # Open the API and get the list of all sha1 encrypted passwords that matches the first 5 characters of our sha1 password
        # an user agent is set so we can actually get the results as the page returns a forbidden error when no user agent is set
        breaches = urlopen(Request("https://api.pwnedpasswords.com/range/{}".format(
            pw[:5]), headers={'User-Agent': 'Mozilla'}), context=ssl_context)
        breachedHashes = breaches.read().decode("utf-8")

        # Check the list we got from the API to see if the remainder of our sha1 hash is in it
        testfor = re.compile("{}:{}".format(pw[5:], r"\d+"))
        
        # Remove the hashed password from memory
        del pw
        
        if testfor.search(breachedHashes):
            # If we find our password, warn the user
            QMessageBox.warning(self, 'PASSWORD BREACHED!',
                                'The password you have entered has been found in a known breach!'
                                'Avoid using the password you just tested at all cost!', QMessageBox.Ok)
            breachInfo = testfor.search(breachedHashes)

            # Remove the testpattern from memory
            del testfor

            # Get how many breaches the hash has been in
            breachCount = breachInfo.group().split(":")

            # Show the user how many times the password has been found in data breaches
            self.resultLbl.setText(
                '<html><head/><body><p>Result:<br/><span style=" color:#ff0004;">'
                'Password has appeared in one or more data breaches!<br/>'
                'It has been sighted {} times</span></p></body></html>'.format(breachCount[1]))
        else:
            # Remove the test pattern from memory
            del testfor

            # If we do not find our sha1 password in the list, show the user that it has not showed up in any known breaches
            self.resultLbl.setText(
                '<html><head/><body><p>Result:<br/><span style=" color:#08a700;">'
                'Password not found in any known breaches.</span></p></body></html>')

    def aboutClicked(self):
        # Write the about text
        aboutText = "A small open source program written in Python by Ove\n"\
            "to check if a password has been in any known breaches\n"\
            "reported to haveibeenpwned.com\n\n"\
            "The password typed in is encrypted and not exposed\n"\
            "to haveibeenpwned!\n"\
            "Only the first 5 characters of the\n"\
            "encrypted password is exposed to the API,\n"\
            "the program then checks the list from HIBP\n"\
            "if the remaining part is in the database."

        # Display information about the small program
        QMessageBox.information(self, 'Password Tester', aboutText, QMessageBox.Ok)


# Initialize the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = PasswordCheck()
    sys.exit(app.exec_())
