# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:27:36 2020

@author: qtckp
"""


from nltk.tokenize import RegexpTokenizer 
from pymystem3 import Mystem
import pymorphy2


tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
ms = Mystem()
morph = pymorphy2.MorphAnalyzer()

def new_categoty(marker):
    if marker in ('A', 'V', 'S', 'PR', 'CONJ'):
        return marker
    return 'ADV'


def lemmatize(words):
    res = list()
    for word in words:
        p = morph.parse(word)[0]
        res.append(p.normal_form)
    return res



with open('dataset.txt', 'r', encoding = 'utf-8') as file:
    
    lines = [line.strip() for line in file]
    
full = []
    

for txt in lines:
    
    words = [word for word in tokenizer.tokenize(txt) if all((w.isalpha() for w in word))]
        
    results = ms.analyze(' '.join(words))
        
    res = [obj['analysis'][0]['gr'] if obj['analysis'] else 'bad=,' for obj in results if 'analysis' in obj.keys()]
        
    res2 = [line.split(',')[0].split('=')[0] for line in res]
        
        
    end = []
    l = '{'
    r = '}'
        
    for word, lem, ps in zip(words, lemmatize(words), map(new_categoty, res2)):
            
        s = f"{word} {l}{lem}={ps}{r}"
            
        end.append(s)
            
    full.append(' '.join(end))
            

with open('result.txt', 'w', encoding='utf-8') as file:
    file.writelines([f + '\n' for f in full])














