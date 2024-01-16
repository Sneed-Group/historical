echo "$1" > script.txt
awk '{ print $2 }' script.txt > script-keywords.txt
awk '{ print $4 }' script.txt >> script-keywords.txt
awk '{ print $6 }' script.txt >> script-keywords.txt

mkdir img
rm img/*
while IFS= read -r line; do
    ./image-finder.sh "$line"
done < script-keywords.txt
find img -type f -size 0 -delete
