import utils
import nltk
from trigram_tagging import raw_trigram_tag
from small_analysis import big_sents as sents

def ne_tag(sentences):
    tagged = raw_trigram_tag(sentences, tagger_file="tagger.pkl")[1]
    fin = []
    for tagged_sent in tagged:
        # print tagged_sent
        fin.append(nltk.ne_chunk(tagged_sent))
    return fin

def ne_freq_dist(tagged_sents):
	named_entities = []
	for sentence in tagged_sents:
		for elem in sentence:
			if isinstance(elem, nltk.tree.Tree):
				entity = " ".join([leaf[0] for leaf in elem.leaves()])
				named_entities.append((elem.label(), entity))
	return named_entities
	
tagged = ne_tag(sents)
named_entities = ne_freq_dist(tagged)

gpes = nltk.FreqDist([entity for entity in named_entities if entity[0] == 'GPE'])
orgs = nltk.FreqDist([entity for entity in named_entities if entity[0] == 'ORGANIZATION'])
people = nltk.FreqDist([entity for entity in named_entities if entity[0] == 'PERSON'])

top_gpes = utils.sort_freq_dist(gpes)[:10]
top_orgs = utils.sort_freq_dist(orgs)[:10]
top_people = utils.sort_freq_dist(people)[:10]

print "before"
# named_entities = [entity for entity in tagged if entity]
print str(tagged)
