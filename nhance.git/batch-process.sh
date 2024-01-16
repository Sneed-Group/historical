echo "Detected that you wanted the folder: $1"

for pic in "$1/*.*"
do
node index.js "$pic"
done
