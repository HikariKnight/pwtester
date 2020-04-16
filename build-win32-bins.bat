@echo off
cd "%~dp0"
"C:\WinPython\WPy32-3810\python-3.8.1\Scripts\pyinstaller.exe" --hidden-import Crypto.PublicKey --hidden-import Crypto.Hash --hidden-import Crytpro.Signature --hidden-import PySide2.QtXml --hidden-import PySide2.QtQuick --noconfirm --name Pwtester-x86 --window main.py
"C:\WinPython\WPy64-3810\python-3.8.1.amd64\Scripts\pyinstaller.exe" --hidden-import Crypto.PublicKey --hidden-import Crypto.Hash --hidden-import Crytpro.Signature --hidden-import PySide2.QtXml --hidden-import PySide2.QtQuick --noconfirm --name Pwtester-x86_64 --window main.py
pause
