import nltk
from trigram_tagging import raw_trigram_tag
from small_analysis import yoursmall_sents as sents

def ne_tag(sentences):
    tagged = raw_trigram_tag(sentences, tagger_file="tagger.pkl")[1]
    short_tagged = tagged[0:3]
    fin = []
    for tagged_sent in short_tagged:
        # print tagged_sent
        fin.append(str(nltk.ne_chunk(tagged_sent)))
    return fin

i = ne_tag(sents)

