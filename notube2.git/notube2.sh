search="${1// /%20}"
yt=$(curl "https://vid.puffyan.us/search?q=$search" | grep "youtube.com/watch?v=" | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" | sort -u | head -n 1)
mpv $yt
