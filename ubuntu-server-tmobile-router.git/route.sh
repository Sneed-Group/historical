sudo iptables -t mangle -A POSTROUTING -j TTL --ttl-set 66
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
sudo ./lnxrouter --ap wlp4s0 $1 -p $2
