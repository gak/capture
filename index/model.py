#!/usr/bin/env python

import os

from elixir import *

ROOT = os.path.dirname(os.path.realpath(__file__))
DB = os.path.join(ROOT, 'db.sqlite')
DBURL = 'sqlite:///' + DB

metadata.bind = DBURL
#metadata.bind.echo = True

class Frame(Entity):
    path = Field(Unicode(200), unique=True)
    ts = Field(DateTime, unique=True)

    def __repr__(self):
        return '<Frame %s>' % str(self.ts)


class Day(Entity):
    ts = Field(Date, unique=True)
    processed = Field(Boolean, required=True, default=False)

    def __repr__(self):
        return '<Day %s processed:%s>' % (
            self.ts, self.processed
            )
