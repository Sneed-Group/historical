echo "Started Video2Resolve by Sparksammy."
echo "Detected that you wanted the file: $1"
mov=".mov"
ffmpeg -i "$1" -c:v mpeg4 -q:v 5 -c:a pcm_s16le "$1$mov"
