#!/bin/bash
SCRIPTDIR=`dirname $0`

echo Removing old builds
rm -r "$SCRIPTDIR/deploy"

echo Building MacOS/darwin binaries
$HOME/go/bin/qtdeploy build desktop
mv "$SCRIPTDIR/deploy/darwin" "$SCRIPTDIR/deploy/pwtester_MacOS-x86_64"