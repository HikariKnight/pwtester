#!/bin/bash
SCRIPTDIR=`dirname $0`
rm -r "$SCRIPTDIR/deploy"
$HOME/go/bin/qtdeploy build desktop
mv "$SCRIPTDIR/deploy/darwin" "$SCRIPTDIR/deploy/pwtester_MacOS-x86_64"

# Cleanup when we are done
rm -r "$SCRIPTDIR/darwin"