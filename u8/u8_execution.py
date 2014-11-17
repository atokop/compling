#!/usr/bin/python
import sys, re
reload(sys)
sys.setdefaultencoding("utf-8")
import os
direc = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, "scripts/")
sys.path.append(direc)

from small_analysis import big_wordlists, yoursmall_wordlists
from fill_template import *

print ""
print "Big Corpus Earthquake Analysis:"
earthquake_template(big_wordlists)

print ""
print "Small Corpus Earthquake Analysis:"
earthquake_template(yoursmall_wordlists)
