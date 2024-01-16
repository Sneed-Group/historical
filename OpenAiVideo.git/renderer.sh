total_frames=$(wc -l < concat.txt)  # Count the total number of frames in concat.txt
voice_length=$(ffprobe -i voice.wav -show_entries format=duration -v quiet -of csv="p=0")  # Get the length of voice.wav

# Calculate the correct duration of each frame
duration=$(echo "$voice_length / $total_frames" | bc)

fps=$(echo "scale=2; $total_frames / $voice_length" | bc)

# Use the corrected duration in the FFmpeg command
ffmpeg -r $fps -f concat -safe 0 -i concat.txt -i voice.wav -c:v libx264 -c:a aac -vf "setpts=PTS/1" -pix_fmt yuv420p -shortest output_video.mp4

