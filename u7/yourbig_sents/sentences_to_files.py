#!/usr/bin/python
import sys
import os
direc = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, "scripts/")
sys.path.append(direc)

from small_analysis import big_sents as sents
print sents

a = 0
for sent in sents:
    name = "sent_" + str(a)
    f = open(name, "w")
    f.write(sent)
    a = a+1
    print "%s written" % name

