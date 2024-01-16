@echo off
echo  :: Remove OneDrive
echo Deleting OneDrive...
timeout /t 2 /nobreak > NUL

set x64="%SYSTEMROOT%\SysWOW64\OneDriveSetup.exe"
 
taskkill /f /im OneDrive.exe > NUL 2>&1
ping 127.0.0.1 -n 5 > NUL 2>&1
 
if exist %x64% (
%x64% /uninstall
) else (
echo "OneDrive installer not found, skipping..."
)
ping 127.0.0.1 -n 8 > NUL 2>&1

echo Removing OneDrive leftovers...
echo 1
rd "%USERPROFILE%\OneDrive" /Q /S > NUL 2>&1
echo 2
rd "C:\OneDriveTemp" /Q /S > NUL 2>&1
echo 3
rd "%LOCALAPPDATA%\Microsoft\OneDrive" /Q /S > NUL 2>&1
echo 4
rd "%PROGRAMDATA%\Microsoft OneDrive" /Q /S > NUL 2>&1

echo.
echo Removing OneDrive from Explorer Panel....
reg delete "HKEY_CLASSES_ROOT\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}" /f > NUL 2>&1
reg delete "HKEY_CLASSES_ROOT\Wow6432Node\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}" /f > NUL 2>&1
pause
