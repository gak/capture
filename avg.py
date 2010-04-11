#!/usr/bin/env python

import os
from glob import glob
from os.path import join
from datetime import datetime

import Image
import ImageFont, ImageDraw

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

for hour in xrange(6, 21):
    for minute in xrange(0, 60):

        if hour == 6 and minute < 32:
            continue

        frames = get_frames_for_time(hour, minute)
        if len(frames) < 4:
            continue

        destfile = 'avg/%02i%02i.png' % (hour, minute)
        cmd = get_avg_cmd_for_images(frames, destfile)
        print cmd
        os.system(cmd)

        im = Image.open(destfile)
        font = ImageFont.truetype('Verdana', 12)

        draw = ImageDraw.Draw(im)
        draw.text((5, 5), '%02i:%02i' % (hour, minute), font=font)

        im.save(destfile)
