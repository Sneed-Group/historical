mkdir "bloatless-videos"

audioout="replace-me-with-output"
audioin="replace-me-with-input"

echo We are starting the recording!
ffmpeg -f pulse -i $audioin -ac 1 -f mp3 - | ffplay - |  ffmpeg -f v4l2 -thread_queue_size 64 -video_size 400x225 -framerate 30 -i /dev/video0 \
       -f pulse -i $audioout -ac 2 \
       -vcodec libx264 -preset ultrafast -qp 0 \
       "bloatless-videos/$1.smallfinal.mp4"
