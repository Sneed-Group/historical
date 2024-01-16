echo "Preparing..."
cd $1 
mkdir TMRW-BACKUPS
cd TMRW-BACKUPS
mkdir $(uname -m)
cd $(uname -m)
mkdir $(scutil --get LocalHostName)
cd $(scutil --get LocalHostName)
DATE="$(date)"
mkdir "$DATE"
cd "$DATE"
mkdir Apps
mkdir Vids
mkdir Pics
mkdir Music
mkdir Docs
mkdir ./Pics/nhance-outputs


echo "Backing up... (This'll take awhile!)"
cp -r /Applications/* ./Apps
cp -r ~/Documents/* ./Docs
cp -r ~/Movies/* ./Vids
cp -r ~/Pictures/* ./Pics
cp -r ~/nhance/output* ./Pics/nhance-outputs
cp -r ~/Music/* ./Music
