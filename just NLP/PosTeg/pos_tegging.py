# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:40:28 2020

@author: qtckp
"""

from nltk.tokenize import RegexpTokenizer 
from pymystem3 import Mystem


with open('dataset.txt', 'r', encoding = 'utf-8') as file:
    lines = [line.strip() for line in file]
    txt = ' '.join(lines)


tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')

words = [word for word in tokenizer.tokenize(txt) if all((w.isalpha() for w in word))]


ms = Mystem()


results = ms.analyze(' '.join(words))


res = [obj['analysis'][0]['gr'] if obj['analysis'] else 'bad=,' for obj in results if 'analysis' in obj.keys()]

# for obj in results:
#     if 'analysis' in obj.keys():
#         print(obj['text'])
#         print(obj['analysis'])
#         print(obj['analysis'][0]['gr'] )
#         print()



res2 = [line.split(',')[0].split('=')[0] for line in res]


def new_categoty(marker):
    if marker in ('A', 'V', 'S', 'PR', 'CONJ'):
        return marker
    return 'ADV'




import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def lemmatize(words):
    res = list()
    for word in words:
        p = morph.parse(word)[0]
        res.append(p.normal_form)

    return res




end = []
l = '{'
r = '}'

for word, lem, ps in zip(words, lemmatize(words), map(new_categoty, res2)):
    
    s = f"{word} {l}{lem}={ps}{r}"
    
    end.append(s)
    



with open('result.txt', 'w', encoding='utf-8') as file:
    file.writelines([' '.join(end)])














