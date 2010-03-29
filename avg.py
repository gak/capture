#!/usr/bin/env python

import os
from glob import glob
from os.path import join
from datetime import datetime

def get_frames_for_time(hour, minute):

    files = []

    for day in glob('frames/*'):

        if day.endswith('_ip'):
            continue

        for frame in glob(join(day, '*jpg')):
            ts = int(frame.split('.')[0].split('/')[-1])
            dt = datetime.fromtimestamp(ts)

            if dt.hour != hour or dt.minute != minute:
                continue

            files.append(frame)
            break

    return files

def get_avg_cmd_for_images(files, dest):
    cmd = 'convert ' + ' '.join(files) + ' -average ' + dest
    return cmd

for hour in xrange(0, 23):
    for minute in xrange(0, 60):

        frames = get_frames_for_time(hour, minute)
        if len(frames) < 3:
            print 'skip yo', hour, minute
            continue
        cmd = get_avg_cmd_for_images(frames, 'avg/%02i%02i.jpg' % (
            hour, minute))
        print cmd
        os.system(cmd)

