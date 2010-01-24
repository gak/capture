cd /Users/gak/src/capture/frames

BASE=`date +%Y%m%d`
D=$BASE
D2=${BASE}_ip

mkdir -p $D
mkdir -p $D2 

BASE=`date +%s`
F=$BASE.jpg
F2=$BASE.ip

isightcapture $D/$F 
/sbin/ifconfig | grep --color=none "inet " | grep -v --color=none 127.0.0.1 > $D2/$F2

