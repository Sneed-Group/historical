@echo off
title TTCLASSIC - Client
cd..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

set /P TTOFF_LOGIN_TOKEN="Secret token: " || ^


set TTOFF_GAME_SERVER=server.sparksammy.com
set /P TTOFF_GAME_SERVER="Game Server (default: Sparkys Realm): " || ^


"panda\python\ppython.exe" -m toontown.launcher.TTOffQuickStartLauncher
pause
exit