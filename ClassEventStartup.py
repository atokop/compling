# -*- coding: utf-8 -*-
from __future__ import division
import nltk
from nltk.book import *
import dateutil
import pyparsing
import numpy
import six
import matplotlib
from nltk.corpus import PlaintextCorpusReader
# Put your corpus directory path below instead, e.g.” D:\Test\ClassEvents” 
corpus_root = '/Users/kwamina/school_dev/senior/comp_linguistics/Islip13Rain'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
# The next step is to show the file names under the directory (optional step)
wordlists.fileids()
ClassEvent = nltk.Text(wordlists.words())
