# -*- coding: utf-8 -*-
from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.tag.stanford import NERTagger
import sys
import utils

reload(sys)
sys.setdefaultencoding("utf-8")

corp_root = "./YourSmallRel/"

def file_words(corpus_root):
	file_list = []
	corpus = PlaintextCorpusReader(corpus_root, '.*')
	for infile in sorted(corpus.fileids()):
		file_list.append([corpus.open(infile).read().encode('utf8').strip()]) 
	return file_list

def tag_files(file_list, tagger):
	tagged_words = []
	for file in file_list:
		tagged_words.append([tagger.tag(file)])
	return tagged_words

def sort_freq(tagged_words):
	# set_words = list(set(tagged_words))
	set_words = tagged_words
	return sorted(set_words, key=lambda word: tagged_words.count(word))

# st = NERTagger('./english.all.3class.distsim.crf.ser.gz', './stanford-ner.jar', encoding="utf-8") 
# utils.store(st, "stanf_tagger.pkl")

st = utils.read("stanf_tagger.pkl")

tagged_words = tag_files(file_words(corp_root), st)
tg = []
for sentence in tagged_words: # poorly named
	for actual_sentence in sentence:
		for word_tuple in sentence:
			for w in word_tuple:
				tg.append(w)
print tg
# Only relevant words:
named_entities = [entity for entity in tg if entity[1] != 'O']
locations = nltk.FreqDist([entity for entity in named_entities if entity[1] == 'LOCATION'])
orgs = nltk.FreqDist([entity for entity in named_entities if entity[1] == 'ORGANIZATION'])
people = nltk.FreqDist([entity for entity in named_entities if entity[1] == 'PERSON'])

top_locs = utils.sort_freq_dist(locations)[:10]
top_orgs = utils.sort_freq_dist(orgs)[:10]
top_people = utils.sort_freq_dist(people)[:10]

print "top locations:\n%s" % str(top_locs)
print "top organisations:\n%s" % str(top_orgs)
print "top people:\n%s" % str(top_people)
