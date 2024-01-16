tmp="temp$RANDOM$RANDOM$RANDOM$RANDOM.tmp"
fid="$RANDOM$RANDOM$RANDOM$RANDOM"
ofn="printfile-$fid.sh"
dfn="decryptfile-$fid.sh"
folderName="$RANDOM$RANDOM"
mkdir "$folderName"
cd "$folderName"
echo "cat \\" > $ofn
echo "echo Passphrase? && read passDec" > $dfn
nano "$tmp"
echo Passphrase? && read passwrd

echo "echo Shredding..." >> "shredder-$fid.sh"

while IFS= read -r line; do
   fn="$RANDOM-$RANDOM-$RANDOM$RANDOM.txt"
   echo "$line" > $fn
   echo "$passwrd" | openssl aes-256-cbc -e -pbkdf2 -salt -in "$fn" -out "$fn.enc" -pass stdin
   echo "$fn \\" >> $ofn
   echo "shred -zun 4 $fn" >> "shredder-$fid.sh"
   echo "echo \"\$passDec\" | openssl aes-256-cbc -d -pbkdf2 -salt -in \"$fn.enc\" -out \"$fn\" -pass stdin" >> $dfn
   shred -zun 4 $fn
done <<< "$(cat $tmp)"

shred -zun 4 $tmp
echo "&& echo EoF" >> $ofn
