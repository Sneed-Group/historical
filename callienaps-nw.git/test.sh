rm -rf files_main
mkdir files_main
echo Transfering test build to files_main
cp builds/* files_main/
chmod +x files_main/callienaps_blue_main.dylib
echo Launching...
  git clone https://github.com/sparksammy/lib2proc-fluxus
  cp lib2proc-fluxus/* files_main/
  rm files_main/README.md
  chmod +x files_main/lib2proc
  cd files_main/
  sudo ./lib2proc $(pgrep '^RobloxPlayer$' | head -1) callienaps_blue_main.dylib

