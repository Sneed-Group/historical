./scripter.sh "$1"
./keywords2images.sh
espeak -f script.txt -w voice.wav
ls -1v img/* | while IFS= read -r file; do
  echo "file '$(echo "$file" | sed "s/'/\\\'/g")'"
done > concat.txt
sed -i '/\\/d' concat.txt 

./renderer.sh
