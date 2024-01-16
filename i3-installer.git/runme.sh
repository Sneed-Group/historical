sudo apt update
sudo apt remove -y pcmanfm
sudo apt install --no-install-recommends -y i3 compton git xfce4-panel nitrogen thunar
git clone https://github.com/sparksammy/i3configs.git
cd i3configs
sudo cp i3 -r /etc/i3/
cp i3 -r ~/.config/i3
cp gtk-2.0 -r ~/.config/gtk-2.0
cp gtk-3.0 -r ~/.config/gtk-3.0
cp menus -r ~/.config/menus
cp compton -r ~/.config/compton
cp xfce-perchannel-xml -r ~/.config/xfce-perchannel-xml
sudo cp sparksammy-logout /bin/sparksammy-logout
sudo chmod 777  /bin/sparksammy-logout
sudo mkdir /wallpapers
sudo cp -r wallpapers /wallpapers
echo Done!
