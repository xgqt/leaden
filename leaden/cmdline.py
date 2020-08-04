#!/usr/bin/env python3


import sys

from leaden import app


def execute(argv=sys.argv[1:], settings=None):
    app.main(argv=argv)
