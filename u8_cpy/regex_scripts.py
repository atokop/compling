#!/usr/bin/python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
direc = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, "scripts/")
sys.path.append(direc)

from small_analysis import *

strin = big_wordlists.raw()
print strin
