#!/usr/bin/python
import sys
import os
direc = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, "scripts/")
sys.path.append(direc)
import u4
import utils
import os
import random
import nltk
 
bayes = utils.read(direc + "dtree.pkl")
feature_words = utils.read(direc + "feat_words.pkl")

if len(sys.argv) < 2:
    print len(sys.argv)
    print "NOT VALID YOU DUNCE!"
else:
    filename = sys.argv[1]
    print filename
    f = open(filename, "r")
    g = open(filename + "clean", "w")
    lines = f.readlines()
    for line in lines:
        features = u4.contains_word_feature_set(line, feature_words)
        # print bayes.classify(features)
        a = "quake" in line or "earthquake" in line
        # if bayes.classify(features):
        if ("quake" in line or "earthquake" in line) and "." in line:
            g.write(line)
            g.write("\n")

