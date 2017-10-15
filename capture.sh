#!/bin/bash -e

DIR="$( cd "$( dirname "$0" )" && pwd )"
cd $DIR
cd frames

BASE=`date +%Y%m%d`
D=$BASE
D2=${BASE}_ip

mkdir -p $D
mkdir -p $D2

BASE=`date +%s`
Fa=$BASE-a.jpg
Fb=$BASE-b.jpg
F2=$BASE.ip

#fswebcam --no-banner --jpeg 95 --no-overlay -d /dev/video0 -r 1280x720 -S 20 $D/$Fa
#fswebcam --no-banner --jpeg 95 --no-overlay -d /dev/video1 -r 1280x720 -S 20 $D/$Fb

# /usr/local/bin/imagesnap -v -w 1 $D/$Fa

ffmpeg -f avfoundation -video_size 1280x720 -framerate 30 -i "0" -vframes 1 $D/$Fa

/sbin/ifconfig | grep --color=none "inet " | grep -v --color=none 127.0.0.1 > $D2/$F2

