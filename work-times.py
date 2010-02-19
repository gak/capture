#!/usr/bin/env python

import os
from datetime import datetime
from glob import glob

def secs(a):
    delta = a - datetime(a.year, a.month, a.day, 0, 0, 0)
    return delta.seconds

days = glob('frames/*_ip')

worktimes = []                     

starts = ''
ends = ''
total_hours = 0
total_days = 0

for day in days[:-1]:

    d = os.path.basename(day)
    day_datetime = datetime(int(d[0:4]), int(d[4:6]), int(d[6:8]))

    first = None
    last = None
    
    shots = glob(day + '/*.ip')

    for shot in shots:

        isWork = open(shot).read().find('10.212') != -1
        if not isWork:
            continue

        unix = float(os.path.basename(shot)[:-3])
        dt = datetime.fromtimestamp(unix)

        worktimes.append(dt)

        if not first:
            first = dt
        last = dt

    if first:
        ts = float(day_datetime.strftime('%s')) * 1000
        starts += '[%s,%f],' % (ts, secs(first) / 3600.)
        ends += '[%s,%f],' % (ts, secs(last) / 3600.)

        total_hours += ((secs(last) - secs(first)) / 3600.)
        total_days += 1
    
d = 'workdata = [ [' + starts + '] , [' + ends + '] ]'
open('work-data.js', 'wb').write(d)

print total_hours / total_days
