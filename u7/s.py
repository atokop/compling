#!/usr/bin/python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
direc = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, "scripts/")
sys.path.append(direc)

from small_analysis import yoursmall_sents as sents
print sents

a = 0
for sent in sents:
    sentence = " ".join(sent)
    name = "sent_" + str(a)
    f = open(name, "w")
    f.write(sentence)
    a = a+1
    print "%s written" % name

