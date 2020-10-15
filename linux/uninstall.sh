#!/bin/bash
SCRIPTDIR=`dirname $0`
printf "This script will uninstall the contents of /opt/pwtester
and remove the /usr/share/applications/pwtester.desktop file.

To continue press ENTER, to quit press CTRL+C\n\n"
read i

printf "Removing the menu entry\n"
sudo rm -v /usr/share/applications/pwtester.desktop

printf "\nRemoving the application from /opt/pwtester\n"
sudo rm -rfv /opt/pwtester