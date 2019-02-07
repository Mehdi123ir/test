
# coding: utf-8

# In[11]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import pickle
from nltk import tree2conlltags

import codecs
import sys

import os
dir_path = '%s\\\TabText\libs\\' %  os.environ['APPDATA'] 
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

    
    
import os.path

save_path = '%s\\\TabText\libs\\'%  os.environ['APPDATA'] 


completeName = os.path.join(save_path,"outpos.txt")         

file2 = open(completeName, "w",encoding="utf-8")

def read_conll(path, col=2):
    with open(path, "r", encoding="utf-8") as conll:
        out = []
        for sent in conll.readlines():
            split = sent.strip("\r\n").split()
            if len(split) > 1:
                none_token_count = col - 1
                new_elem = split[-1:]
                new_elem = split[:none_token_count] + new_elem
                out.append(new_elem)

            else:
                yield out
                out = []
def template(word):
    return "".join([(lambda item: "x" if not item in "آایو" else "a")(char) for char in word])


def isdigit(word):
    return all(map(lambda char: char in "۱۲۳۴۵۶۷۸۹۰1234567890.", word))


def ngram(word, leng=2):
    for i in range(len(word) - 1):
        yield 'word[' + str(i) + ":" + str(i + leng) + "]", word[i:i + leng]



class POSTagger:
    def init(self, model_path):
        self.model_path = model_path
        self.crf = pickle.load(open(model_path, "rb"))

    def parse(self, token_stream):
        return self.parse_sentences([token_stream])[0]

    def parse_sentences(self, list_of_token_stream):
        X_test = [token2features(s) for s in list_of_token_stream]
        y_pred = self.crf.predict(X_test)
        out = []
        for x_sent, y_pred in zip(list_of_token_stream, y_pred):
            out.append(list(zip(x_sent, y_pred)))
        return out



def word2features(sent, i):
    W = sent[i]
    features = {
        'B': 1.0,
        'W': W,
        'P': W in string.punctuation,
        'T': template(W),
        'D(W)': isdigit(W),
    }
    for leng in range(max(4 + 1, len(W)) + 1):
        for k, v in ngram(W, leng=leng):
            features[k] = v
   
  
    
  
    return features


def token2features(token_list):
    return [word2features(token_list, i) for i in range(len(token_list))]


def sent2labels(sent):
    return [postag for token, postag in sent]


def sent2tokens(sent):
    return [token for token, postag in sent]
class POSTagger:
    def __init__(self, model_path):
        self.model_path = model_path
        self.crf = pickle.load(open(model_path, "rb"))

    def parse(self, token_stream):
        return self.parse_sentences([token_stream])[0]

    def parse_sentences(self, list_of_token_stream):
        X_test = [token2features(s) for s in list_of_token_stream]
        y_pred = self.crf.predict(X_test)
        out = []
        for x_sent, y_pred in zip(list_of_token_stream, y_pred):
            out.append(list(zip(x_sent, y_pred)))
        return out


pos_tagger = POSTagger("D:/model/corpus.model")
import codecs
import sys

b=sys.argv[1]
with codecs.open(b,'r',encoding='utf8') as f:
    text = f.read()


file2.write(str(pos_tagger.parse(text.split())))


file2.close() 



import json
out1=[]
out2=[]
output_list = []  
id1=0
import datetime

dat1 = str( datetime.datetime.now() )
sub1={}
sub1['Description']=None
sub1['FileName']=b
sub1['RunDate']=dat1

save_path = '%s\\TabText\libs\\'%  os.environ['APPDATA'] 


completeName = os.path.join(save_path,"outpos.txt")         

file2 = open(completeName, "r",encoding="utf-8")
save_path2 = '%s\\TabText\libs\\'%  os.environ['APPDATA'] 


completeName2 = os.path.join(save_path2,"outpos2.txt")         

file2 = open(completeName, "r",encoding="utf-8")
fo = open(completeName2, "w",encoding="utf-8")
#with open(file3, 'w',encoding="utf-8") as fo:
for line in file2:
    fo.write(line.replace(']', '').replace("[", "").replace(' ', '').replace('),','),\n').replace('(','').replace("\\u200c",'').replace("\\ufeff",'').replace(')\n',''))
import codecs
out1=[]
f = open(completeName2, "r",encoding="utf-8")

for line in f:
    tu=tuple(line.split(','))
    # 
    
    sub_dict = {}
    sub_dict['id'] = id1
    a=str(tu[1].replace(')',''))
    sub_dict['Token'] = tu[0]
    
    sub_dict['POS-Tagg'] =a
    sub_dict['Type'] = 'Persian' 
    
    output_list.append(sub_dict) 
    id1=id1+10
   
kol=[]
kol.append(sub1)
kol.append(output_list)   
import io
with io.open(sys.argv[2], 'w', encoding='utf8') as json_file:
    json.dump(kol, json_file,indent=4, ensure_ascii=False)

