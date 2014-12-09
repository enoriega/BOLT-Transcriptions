''' This script reads the data collected by us and organized by Coleen at SRI and generates a Django fixture for the annotation app '''
import json
import os.path as pt
import codecs
#from annotations.models import ARAnnotation, ENAnnotation

en_path = '/home/enoriega/UnivAriz-2/P3Testing_UnivAriz-2.en.hyps'
ar_path =  '/home/enoriega/UnivAriz-2/P3Testing_UnivAriz-2.ia.hyps'

ar_fixture = 'ia_fixture.json'
en_fixture = 'en_fixture.json'




def parse_hyps(path, lang, model, pk = 1):
    elements = []
    with codecs.open(path, 'r', encoding='utf_8') as f:
        for line in f:
            tokens = line.split(' ', 1) # Split only two tokens
            id = tokens[0]
            hyp = tokens[1][:-1]

            item = {
                'pk': pk,
                'model':'transcriptions.annotation',
                "fields":{
                    'audio': pt.join(lang, id+'.wav'),
                    'sentence_id':id,
                    'hyp': hyp,
                    'trans':hyp,
                    'annotated':False,
                    'skipped':False,
                }
            }

            elements.append(item)

            item = {
                'pk': pk,
                'model':model,
                "fields":{
                }
            }

            elements.append(item)

            pk += 1
    return elements, pk

# First deal with english
en, pk = parse_hyps(en_path, 'en', 'transcriptions.enannotation')

# Now with arabic
ar, pk = parse_hyps(ar_path, 'ia', 'transcriptions.arannotation', pk=pk)

with codecs.open(ar_fixture, 'w', encoding='utf_8') as f:
    json.dump(ar, f)

with codecs.open(en_fixture, 'w', encoding='utf_8') as f:
    json.dump(en, f)
