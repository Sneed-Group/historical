echo Char. Width
read width
echo Char. Height
read height
echo Video URL
read url
multiplier="x"
youtube-dl $url -o - | CACA_GEOMETRY=$width$multiplier$height mplayer -quiet -vo caca -
