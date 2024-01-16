set "mydir=%PROGRAMFILES(X86)%\Microsoft\Edge\Application"

FOR /d %%a IN ("%mydir%\*") DO SET "myfolder=%%~nxa"&GOTO found

:found
"%mydir%/%myfolder%/Installer/setup.exe" --uninstall --system-level --verbose-logging --force-uninstall 
