# micro11builder

Scripts to build a super trimmed-down Windows 11 image, with a post-install script set.

This is a script to automate the build of a streamlined Windows 11 image, similar to tiny11.
My main goal is to use only Microsoft utilities like DISM, and nothing external. The only executable included is oscdimg.exe, which is provided in the Windows ADK and it is used to create bootable ISO images. Also included is an unattended answer file, which is used to bypass the MS account on OOBE and to deploy the image with the /compact flag.
It's open-source, so feel free to add or remove anything you want! Feedback is also much appreciated.

As of now, only 25300 is supported.

Instructions:

0. extract oscdimg.zip so the exe is in the same directory as the batch file
1. Download Windows 11 25300 from UUPDump
2. Mount the downloaded ISO image using Windows Explorer.
3. For .1265, run micro11 creator.bat as administrator.
4. Select the drive letter where the image is mounted (only the letter, no colon (:))
5. Select the SKU that you want the image to be based.
6. Sit back and relax :)
7. When the image is completed, you will see it in the folder where the script was extracted, with the name micro11.iso

What is removed:
Clipchamp,
News,
Weather,
Xbox (although Xbox Identity provider is still here, so it should be possible to be reinstalled with no issues),
GetHelp,
GetStarted,
Office Hub,
Solitaire,
PeopleApp,
PowerAutomate,
ToDo,
Alarms,
Mail and Calendar,
Feedback Hub,
Maps,
Sound Recorder,
Your Phone,
Media Player,
QuickAssist,
Internet Explorer,
LA57 support,
OCR for en-us,
Speech support,
TTS for en-us,
Media Player Legacy,
Tablet PC Math,
Wallpapers,
Edge,
OneDrive,
Tons of new registry edits to make the system more private, including the running the ***windows version of betterify scripts on first login.***

Known issues:

1. Microsoft Teams (personal) and Cortana are still here. If you find a way to remove them before I find one, feel free to help!
2. Although Edge is removed, the icon and a ghost of its taskbar pin are still available. Also, there are some remnants in the Settings. But the app in itself is deleted.
3. The script is rather inflexible, as in only the builds specified can be modified. This is because with each new build Microsoft also updates the inbox apps included. If one tries to use other builds, it will work with varying degrees of success, but some things like the removal of Edge and OneDrive as well as bypassing system requirements or other patches will always be applied.
4. Only en-us x64 is supported as of now. This can be easily fixable by the end user, just by replacing every instance of en-us with the language needed (like ro-RO and so on), and every x64 instance with arm64.

And that's pretty much it for now!
Thanks for trying it and let me know how you like it!

# Disclaimer

Auto-activation was removed from a previous version. To "quack", do this after installing:

```
PowerShell.exe -command "irm https://raw.githubusercontent.com/NodeMixaholic/Microsoft-Activation-Scripts/master/hwid | iex"
```

# Default credentials
```
Username: Admin
Password: password
Note: Be sure to change the password to something more secure!
```

## Help! I couldn't download the script pack due to lack of internet!
1. get internet
2. save this as a batch file:
```
PowerShell.exe -command "irm https://github.com/windowsbetterify/1liner/raw/main/1l | iex"
PowerShell.exe -command "irm https://github.com/gam3less/debloatwindows/raw/master/debloatwindows.ps1 | iex"
PowerShell.exe -command "irm https://github.com/windowsbetterify/windowsbetterify/raw/main/mini-christitus.ps1 | iex"
```
3. Run batch file as admin
4. Reboot.

## Which OSCDIMG do you use?

This one: https://go.microsoft.com/fwlink/?linkid=2196127

## Errors when installing MSI packages! How do I fix this?

Watch this video guide:

[![Video](http://img.youtube.com/vi/CYsl9ZaEcGE/0.jpg)](http://www.youtube.com/watch?v=CYsl9ZaEcGE)
