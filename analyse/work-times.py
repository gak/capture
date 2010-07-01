#!/usr/bin/env python

import os
from datetime import datetime
from glob import glob

def hours(a):
    delta = a - datetime(a.year, a.month, a.day, 0, 0, 0)
    return delta.seconds / 3600.

def mins(a):
    return hours(a) * 60.

days = glob('frames/*_ip')

workStartTimes = ''
workEndTimes = ''
homeMorningTimes = ''
homeEveningTimes = ''
morningCommuteTimes = ''
eveningCommuteTimes = ''

total_hours = 0
total_days = 0

days = days[:-1]

for i, day in enumerate(days):

    print float(i) / len(days) * 100

    d = os.path.basename(day)
    day_datetime = datetime(int(d[0:4]), int(d[4:6]), int(d[6:8]))

    workStartTime = None
    workEndTime = None

    homeMorningTime = None
    homeEveningTime = None
    
    shots = glob(day + '/*.ip')

    for shot in shots:
        
        data = open(shot).read()

        isWork = data.find('10.212') != -1
        isHome = data.find('10.0.0.') != -1 and not isWork

        unix = float(os.path.basename(shot)[:-3])
        dt = datetime.fromtimestamp(unix)

        if isHome and not workStartTime:
            homeMorningTime = dt

        if isHome and workStartTime and not homeEveningTime:
            homeEveningTime = dt

        if isWork and not workStartTime:
            workStartTime = dt

        if isWork:
            workEndTime = dt

    print d, homeMorningTime, workStartTime, workEndTime, \
        homeEveningTime

    if workStartTime and workEndTime and homeMorningTime and homeEveningTime:

        ts = float(day_datetime.strftime('%s')) * 1000

        workStartTimes += '[%s,%f],' % (ts, hours(workStartTime))
        workEndTimes += '[%s,%f],' % (ts, hours(workEndTime))
        homeMorningTimes += '[%s,%f],' % (ts, hours(homeMorningTime))
        homeEveningTimes += '[%s,%f],' % (ts, hours(homeEveningTime))

        morningCommuteTimes += '[%s,%f],' % (ts, mins(workStartTime) - mins(homeMorningTime))
        eveningCommuteTimes += '[%s,%f],' % (ts, mins(homeEveningTime) - mins(workEndTime))

        total_hours += ((hours(workEndTime) - hours(workStartTime)))
        total_days += 1
    
d = 'workdata = [ ['
d += '],\n ['.join([
    homeMorningTimes, workStartTimes, workEndTimes, homeEveningTimes
    ])
d += '] ]\n'

d += 'commutedata = [ ['
d += '],\n ['.join([ morningCommuteTimes, eveningCommuteTimes ])
d += '] ]\n'

open('work-data.js', 'wb').write(d)

print total_hours / total_days
