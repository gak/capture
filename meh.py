#!/usr/bin/env python

from glob import glob
from shutil import copyfile

i = 0

for file in glob('avg/*jpg'):
    out = 'avg2/%03i.jpg' % i
    i += 1
    print file, out
    copyfile(file, out)

