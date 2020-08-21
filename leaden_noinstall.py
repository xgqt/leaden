#!/usr/bin/env python


import sys
from subprocess import call

call(["make"])


import leaden.cmdline


leaden.cmdline.execute(argv=sys.argv[1:], settings=None)
