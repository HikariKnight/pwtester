#!/bin/bash
SCRIPTDIR=`dirname $0`
echo Removing old builds
rm -r "$SCRIPTDIR/deploy"

echo Building linux binaries
$HOME/go/bin/qtdeploy build linux
mv "$SCRIPTDIR/deploy/linux" "$SCRIPTDIR/deploy/pwtester_linux-x86_64"

echo Prepping icons for Windows x86_64
x86_64-w64-mingw32-windres assets/icon.rc assets/icon_windows.syso 

echo Building Windows x86_64 binaries
$HOME/go/bin/qtdeploy -docker -ldflags -H=windowsgui build windows_64_shared
mv "$SCRIPTDIR/deploy/windows" "$SCRIPTDIR/deploy/pwtester_windows-x86_64"

echo Prepping icons for Windows x86
i686-w64-mingw32-windres assets/icon.rc assets/icon_windows.syso

echo Building Windows x86 binaries
$HOME/go/bin/qtdeploy -docker -ldflags -H=windowsgui build windows_32_shared
mv "$SCRIPTDIR/deploy/windows" "$SCRIPTDIR/deploy/pwtester_windows-x86"

# Cleanup empty dirs when done (if we embed files into the binary, this wont be empty)
rmdir "$SCRIPTDIR/windows"