#!/bin/bash
SCRIPTDIR=`dirname $0`
printf "This script will install the contents of $SCRIPTDIR/ into /opt/pwtester/
and copy the /opt/pwtester/assets/pwtester.desktop file to /usr/share/applications/.
To uninstall the application just run /opt/pwtester/uninstall.sh.

To continue press ENTER, to quit press CTRL+C\n\n"
read i

printf "Making /opt/pwtester/\n"
sudo mkdir -p /opt/pwtester

printf "\nCopying files to /opt/pwtester/\n"
sudo cp -rv "$SCRIPTDIR" /opt/pwtester/

printf "\nCopying pwtester.desktop to /usr/share/applications"
cp -v /opt/pwtester/assets/pwtester.desktop /usr/share/applications/
