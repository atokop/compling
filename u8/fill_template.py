#!/usr/bin/python
import sys, re
reload(sys)
sys.setdefaultencoding("utf-8")
import os
direc = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, "scripts/")
sys.path.append(direc)

# from small_analysis import *

def most_common(lst):
    return max(set(lst), key=lst.count)

location_pattern_string = "((in|at)\s([A-Z][a-zA-Z]{4,}|[A-Z][a-zA-Z]{2,}\s[A-Z][a-zA-Z]{3,})|\s+[A-Z][a-zA-Z]{3,},\s[A-Z][a-zA-Z]{2,}\s[A-Z][a-zA-Z]{3,})"
monthPatternString = "(?:January|February|March|April|May|June|July|August|September|October|November|December)"

# Magnitudes
def find_magnitude(raw_collection):
    strin = raw_collection
    regexes = []
    regexes.append(re.findall('magnitude (?:of )?[0-9]\.?[0-9]*', strin))
    regexes.append(re.findall('[0-9]\.?[0-9]* magnitude', strin))
    results = []
    for reg in regexes:
        results += reg
    a = " ".join(results)

    mags = [float(num) for num in re.findall('[0-9]\.?[0-9]*', a)]
    avg = sum(mags) / len(mags)
    mode = most_common(mags)
    print "Magnitude: %s" % mode
    return mode

# Deaths
def find_deaths(raw_collection):
    strin = raw_collection
    regexes = []
    regexes.append(re.findall('(?:[0-9]+ deaths)', strin))
    regexes.append(re.findall('(?:[0-9]+ were killed)', strin))
    regexes.append(re.findall('killed (?:\w+ ){0,2}[0-9]+ people', strin))
    regexes.append(re.findall('(?:[0-9]+ casualties)', strin))
    results = []
    for reg in regexes:
        results += reg
    a = " ".join(results)
    deaths = [float(num) for num in re.findall('[0-9]\.?[0-9]*', a)]
    avg = sum(deaths) / len(deaths)
    mode = most_common(deaths)
    print "Deaths: %s" % mode
    return mode

# Injuries
def find_injuries(raw_collection):
    strin = raw_collection
    regexes = []
    regexes.append(re.findall('[0-9]+ injur(?:(?:ies)|(?:ed))', strin))
    regexes.append(re.findall('(?:[0-9]+ were injured)', strin))
    regexes.append(re.findall('injured (?:\w+ ){0,2}[0-9]+ people', strin))
    results = []
    for reg in regexes:
        results += reg
    a = " ".join(results)
    deaths = [float(num) for num in re.findall('[0-9]\.?[0-9]*', a)]
    avg = sum(deaths) / len(deaths)
    mode = most_common(deaths)
    print "Injuries: %s" % mode
    return mode

# Location
def find_location(raw_collection):
    strin = raw_collection
    regexes = []
    regexes.append([a[-1] for a in re.findall(location_pattern_string, strin) if len(a[-1]) > 0])
    results = []
    for reg in regexes:
        results += reg

    mode = most_common(results)
    print "Location: %s" % mode
    return mode

# Epicenter
def find_epicenter(collection_sents):
    relevant_sents = [sent for sent in collection_sents if "epicenter" in sent]
    strin = []
    for sent in relevant_sents:
        strin += sent
    strin = " ".join(strin)
    regexes = []
    t = re.findall(location_pattern_string, strin) 
    ting = [a[-1] for a in t if len(a[-1]) > 0]
    regexes.append(ting)
    results = []
    for reg in regexes:
        results += reg
    #results = [a[-1] for a in results]
    mode = most_common(results)
    print "Epicenter: %s" % mode
    return mode

def find_date(raw_collection):
    strin = raw_collection

    results = re.findall(monthPatternString, strin)
    month = most_common(results)

    results = re.findall('(?:January|February|March|April|May|June|July|August|September|October|November|December),?\s([0-9]{,2})[^0-9]', strin)
    day = most_common(results)
    
    results = re.findall('(?:1|2)[0-9]{3}', strin)
    year = most_common(results)

    date = (day, month, year)
    print "Date: {1} {0}, {2}".format(date[0], date[1], date[2])

def find_time(raw_collection):
    results = re.findall('[0-9]{1,2}:[0-9][0-9](?::[0-9][0-9])?(?:\s?[apAP]\.?[mM]\.?)?', raw_collection)

    raw_times = " ".join(results)
    results = re.findall('([0-9]{1,2}:[0-9][0-9])(?::[0-9][0-9])?(?:\s?[apAP]\.?[mM]\.?)?', raw_times)
    time = most_common(results)
    results = re.findall('[aApP]\.?[mM]\.?', raw_times)
    results = [a for a in results if len(a) != 0]
    am_versus_pm = most_common(results)

    print "Time: {0} {1}".format(time, am_versus_pm)
    return time
    
def find_aid(sentences):
    from nltk.stem.wordnet import WordNetLemmatizer
    stopwords = nltk.corpus.stopwords.words('english')
	lemmer = WordNetLemmatizer()
	wordvec = []
	aidwords = ["aid", "provide"]
    for sentence in sentences:
			words = sentence.split()
			for x, word in enumerate(words):
				if lemmer.lemmatize(word.lower()) in aidwords:
					phrase = words[x-2:x]
					for string in phrase:
						if string.lower() not in stopwords and string not in aidwords and string[0].isupper():
							wordvec.append(string)
	set_words = set(wordvec)
	set_words = sorted(set_words, key=lambda v: wordvec.count(v))
	set_words = set_words[len(set_words)-k:].reverse()
    print "Aid: {0} {1} {2}".format(set_words[0], set_words[1], set_words[2])
    return set_words[0:3]
    
def earthquake_template(corpus):
    raw_text = corpus.raw()
    sents = corpus.sents()

    find_date(raw_text)
    find_location(raw_text)
    find_magnitude(raw_text)
    find_epicenter(sents)
    find_deaths(raw_text)
    # find_injuries(raw_text)
    find_time(raw_text)
    find_aid(sents)
