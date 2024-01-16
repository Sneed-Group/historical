# Managment Engine Disabler for Linux.

This program acts the same as "fpt -disableme"
ME enters temporary disable mode. HECI interface shuts down.
This mode can only be cancelled by powering off the system.

You can even run at boot in debian-likes by using this crontab using root (sudo crontab -e, not exact):

```
@reboot /path/to/your/ime-disabler-binary &
```

i recommend copying it to /usr/bin/ for this sake, so it would be (not exact):

```
@reboot /usr/bin/your-ime-disabler-binary-name &
```
