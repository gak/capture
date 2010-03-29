#!/usr/bin/env python

from glob import glob
from os.path import join
from datetime import datetime

files = []

for day in glob('frames/*'):

    if day.endswith('_ip'):
        continue

    for frame in glob(join(day, '*jpg')):
        ts = int(frame.split('.')[0].split('/')[-1])
        dt = datetime.fromtimestamp(ts)

        if dt.hour < 12:
            continue

        files.append(frame)
        print frame

        break

cmd = 'convert ' + ' '.join(files) + ' -average avg.jpg'
print cmd

