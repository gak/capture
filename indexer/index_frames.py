from storm.locals import *

class Frame(object):
    __storm_table__ = 'frame'
    id = Int(Primary=True)
    path = Unicode()
    ts = DateTime()

