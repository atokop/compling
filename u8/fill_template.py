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
    return date
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

def find_word(word, path_to_corpus, cutoff):
    files = os.listdir(path_to_corpus)
    found = len(["a" for f in files if word in open(os.path.join(path_to_corpus, f)).read()])
    word_percentage = float(found)/len(files)
    if word_percentage > cutoff:
        print word + "(s) present"
        return True
    else:
        print word + "(s) not present"
        return False

def earthquake_template(corpus, path_to_corpus=None):
    raw_text = corpus.raw()
    sents = corpus.sents()

    template = {}; 
    template['date'] = find_date(raw_text)
    template['location'] = find_location(raw_text)
    template['magnitude'] = find_magnitude(raw_text)
    template['epicentre'] = find_epicenter(sents)
    template['deaths'] = find_deaths(raw_text)
    # find_injuries(raw_text)
    template['time'] = find_time(raw_text)
    if path_to_corpus:
        template['aftershock'] = find_word('aftershock', path_to_corpus, 0.2)
        template['tsunami'] = find_word('tsunami', path_to_corpus, 0.3)
        template['landslide'] = find_word('landslide', path_to_corpus, 0.15)

    return template


