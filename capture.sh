#!/bin/bash

DIR="$( cd "$( dirname "$0" )" && pwd )"
cd $DIR
cd frames

BASE=`date +%Y%m%d`
D=$BASE
D2=${BASE}_ip

mkdir -p $D
mkdir -p $D2

BASE=`date +%s`
F=$BASE.jpg
F2=$BASE.ip

killall -9 imagesnap > /dev/null 2>&1

$DIR/imagesnap $D/$F > /dev/null 2>&1
/sbin/ifconfig | grep --color=none "inet " | grep -v --color=none 127.0.0.1 > $D2/$F2

