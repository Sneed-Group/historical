if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <file or directory>"
	exit 1
fi

read -p "Are you sure you want to snap $1 out of existence? (y/n): " answer
if [ "$answer" != "y" ]; then
	echo "Operation aborted. $1 is safe and sound."
	exit 1
fi

echo "Snapping $1 out of existence..... Please wait!"

if [ -d "$1" ]; then
        find "$1" -type f -exec shred -u -z -n 128 {} \;
	rm -rf "$1"
fi


if [ -f "$1" ]; then
  	for i in {1..128}
	do
		dd if=/dev/random of="$1" bs=1M count=1 status=none
	done
	rm -f "$1"
fi

echo "OK!"
