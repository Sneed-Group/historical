mkdir "bloatless-videos"
resscreen=$(xdpyinfo | awk '/dimensions:/ { print $2 }')
audioout="replace-me-with-output"
audioin="replace-me-with-input"

echo We are starting the screencast!
ffmpeg -f pulse -i $audioin -ac 1 -f mp3 - | ffplay - |  ffmpeg -f x11grab -thread_queue_size 450  -framerate 45 -video_size $resscreen -i :0.0 \
       -f v4l2 -thread_queue_size 64 -video_size 320x180 -framerate 30 -thread_queue_size 225 -i /dev/video0 \
       -f pulse -i $audioout -ac 2 \
       -filter_complex 'overlay=main_w-overlay_w:main_h-overlay_h:format=yuv444' \
       -vcodec libx264 -preset ultrafast -qp 0 \
       -f "mp4" "bloatless-videos/$1.largetmp.mp4"
echo Scaling for smaller file size.. please wait.
ffmpeg -i "bloatless-videos/$1.largetmp.mp4" -vf "scale=iw*.5:ih*.5" "bloatless-videos/$1.smallfinal.mp4"
rm "bloatless-videos/$1.largetmp.mp4"
