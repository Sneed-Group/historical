# lightrecorder

Lightweight recorder for simple screencasting/vlogging. Afterall, in a world without OBS and ***manual*** FFMEPG, who needs SLOBS and SimpleScreenRecorder?

## How do I list my possible devices?

```
bash lrlsd.sh
```

## How do I apply my devices?

Assuming they are compatable with GNU/Linux...

* First off take note of the lrlsd.sh output.
* Then replace the audioout/audioin variable in each script with your device.

## Basic recording tips

* Wear headphones and put them on your cheeks or the back of your head
* Turn down the volume a bit to block out the noise of your own voice.
* In an event you cannot use headphones, it is urgent that you either mute your mic (which will disable voice input) ***or*** turn down your speaker volume a ton so you can barely hear it.
* This last solution means, however, that your video will come out very quiet. There is no solution for this currently to keep things unbloated.
* Always keep this in mind: your voice might likely be better and more well announciated than my voice, so sit back and talk away. You can always cut out the mumbles using a tool like Shotcut. (Unless you dislike bloat.)
