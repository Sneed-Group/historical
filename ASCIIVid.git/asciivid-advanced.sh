echo Char. Width
read width
echo Char. Height
read height
multiplier="x"
CACA_GEOMETRY=$width$multiplier$height mplayer -quiet -vo caca "$1"
