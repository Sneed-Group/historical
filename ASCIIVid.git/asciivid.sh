videoSRC="gabe.mp4"
title="Gabe the dog - don't stop me now"
originalBy="Rapid Liquid"
asciiBy="Sparksammy"
endingMSG="Sleep tight, sweet pupper."

#DO NOT MESS WITH THE CODE BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING!

echo This song is: $title
echo Original material is by $originalBy
echo ASCII version is by $asciiBy
mplayer -quiet -vo caca $videoSRC
clear
echo $endingMSG
