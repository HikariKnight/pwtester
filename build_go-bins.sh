#!/bin/bash
SCRIPTDIR=`dirname $0`
rm -r "$SCRIPTDIR/deploy"
$HOME/go/bin/qtdeploy build linux
mv "$SCRIPTDIR/deploy/linux" "$SCRIPTDIR/deploy/pwtester_linux-x86_64"

# Cleanup empty dirs when done (if we embed files into the binary, this wont be empty)
rmdir "$SCRIPTDIR/linux"

$HOME/go/bin/qtdeploy -docker -ldflags -H=windowsgui build windows_64_shared
mv "$SCRIPTDIR/deploy/windows" "$SCRIPTDIR/deploy/pwtester_windows-x86_64"
$HOME/go/bin/qtdeploy -docker -ldflags -H=windowsgui build windows_32_shared
mv "$SCRIPTDIR/deploy/windows" "$SCRIPTDIR/deploy/pwtester_windows-x86"

# Cleanup empty dirs when done (if we embed files into the binary, this wont be empty)
rmdir "$SCRIPTDIR/windows"