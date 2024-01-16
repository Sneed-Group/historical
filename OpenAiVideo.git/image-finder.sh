url=$(curl -sS "https://unsplash.com/s/photos/$1?license=free" | grep -o 'href="[^"]*' | grep 'download' | head -n 1 | sed 's/href="//')
wget -O "img/$1.$(wget --spider --server-response -O - 'YOUR_URL' 2>&1 | grep -E -o -i 'Content-Type:.*' | cut -d ' ' -f 2 | cut -d ';' -f 1)" "$url"

