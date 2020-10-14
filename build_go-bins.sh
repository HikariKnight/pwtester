#!/bin/bash
SCRIPTDIR=`dirname $0`
rm -r "$SCRIPTDIR/deploy"
$HOME/go/bin/qtdeploy build linux
mv "$SCRIPTDIR/deploy/linux" "$SCRIPTDIR/deploy/pwtester_linux-x86_64"
# Cleanup when we are done
rm -r "$SCRIPTDIR/linux"

echo Press enter to build the Windows binaries (requires that you have pulled the docker images from therecipe/qt)
echo Press CTRL+C to exit
$HOME/go/bin/qtdeploy -docker -ldflags -H=windowsgui build windows_64_shared
mv "$SCRIPTDIR/deploy/windows" "$SCRIPTDIR/deploy/pwtester_windows-x86_64"
$HOME/go/bin/qtdeploy -docker -ldflags -H=windowsgui build windows_32_shared
mv "$SCRIPTDIR/deploy/windows" "$SCRIPTDIR/deploy/pwtester_windows-x86"

# Cleanup when we are done
rm -r "$SCRIPTDIR/windows"