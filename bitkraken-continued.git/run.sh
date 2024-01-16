bitcoin/bin/bitcoind -daemon
KEYBASE=$(shuf -n 1 NotDansSecLists.txt)
KEY=$(echo $KEYBASE | sha256sum)
KEY=$(echo $KEY | cut -c 1-64)
printf "\n$KEYBASE = "
printf "$KEY\n"
bitcoin/bin/bitcoin-cli importprivkey "$KEY" "$KEYBASE$RANDOM" # imports key to unencrypted wallet
sleep .7 # important so things don't crash as easily. (i hope.)
./run.sh
