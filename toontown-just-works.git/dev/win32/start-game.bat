@echo off
color 0a
title Poodletooth isLand Game Launcher

echo Choose your connection method!
echo.
echo #1 - Localhost
echo #2 - Server
echo #3 - Custom
echo #4 - MiniGames
echo.


:selection

set INPUT=-1
set /P INPUT=Selection: 

if %INPUT%==1 (
    set TTS_GAMESERVER=127.0.0.1
) else if %INPUT%==2 (
    set TTS_GAMESERVER=server.sparksammy.com
) else if %INPUT%==4 (
    GOTO 4
) else if %INPUT%==5 (
    SET TTS_GAMESERVER=lw2.ez-webz.com:7198
) else if %INPUT%==3 (
    echo.
    set /P TTS_GAMESERVER=Gameserver: 
) else (
	goto selection
)

echo.


if %INPUT%==4 (
    set /P ttsUsername="Username: "
    set /P ttsPassword="Password: "
) else (
    set /P TTS_PLAYCOOKIE="Secret token:" 
)

echo.

echo ===============================
echo Starting Poodletooth Island...
echo ppython: "C:\Panda3D-1.10.0\python\ppython.exe"

if %INPUT%==2 (
    echo Username: %ttsUsername%
) else if %INPUT%==4 (
    echo Username: %ttsUsername%
) else (
    echo Username: %TTS_PLAYCOOKIE%
)

echo Gameserver: %TTS_GAMESERVER%
echo ===============================

cd ../../

:main
if %INPUT%==2 (
    "C:\Panda3D-1.10.0\python\ppython.exe" -m toontown.toonbase.ToontownStart
) else if %INPUT%==4 (
    "C:\Panda3D-1.10.0\python\ppython.exe" -m toontown.toonbase.ToontownStartRemoteDB
) else (
    "C:\Panda3D-1.10.0\python\ppython.exe" -m toontown.toonbase.ToontownStart
)
pause

goto main
:4
echo #1m - Escape from the castle Cogenstien
echo #256m exit
set /p a="> " 
goto %a%
goto 4

:1m
cd ../../
cd resources
C:\Panda3D-1.10.0\python\ppython.exe escape.py
goto 4

:256m
goto main