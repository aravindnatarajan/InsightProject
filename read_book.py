
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

import nltk
import nltk.stem
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.stem.wordnet import WordNetLemmatizer

import os
import numpy as np
import sys

import numpy as np
import sys

path = "/Users/Arvi/InsightProject/"
alphabet = "abcdefghijklmnopqrstuvwxyz"
listSigns = [((word.split())[0]).lower() for word in open("/Users/Arvi/my_bootstrap/static/log.dat")]

#partsOfSpeech = ['NN', 'NNS', 
partsOfSpeech = ['NN', 'NNS', 'NNP', 'VB', 'VBD', 'VBZ', 'JJ']

trainingData = nltk.corpus.treebank.tagged_sents()
unigram_tagger = nltk.NgramTagger(n=1, train=trainingData)
bigram_tagger  = nltk.NgramTagger(n=2, train= trainingData, backoff=unigram_tagger)
lmtzr = WordNetLemmatizer()

stops = [t.lower() for t in stopwords.words('english')]
words = [w.lower() for w in ([word.split() for word in [open(path+sys.argv[1]).read()]][0])]

newWords = []
for word in words:

  if len(word) > 2:
    if word[-2] == "'" and word[-1] == "s": word = word[:-2]
  if "-" in word:
    for w in word.split("-"):  
      if w in listSigns: newWords.append(w)
    continue    
  ss = ""
  for letter in word:
    if letter in alphabet: ss += letter

  word = lmtzr.lemmatize(ss)
  if word in stops: continue    
  
  if word in listSigns:
    newA = []
    newA.append(word)        
    tagged = bigram_tagger.tag(newA)    
    if tagged[0][1] in partsOfSpeech: newWords.append(word)
    else:
      newA[0] = newA[0][0].upper() + newA[0][1:]
      tagged = bigram_tagger.tag(newA)    
      if tagged[0][1] in partsOfSpeech: newWords.append(word)        
      else:
        tagged = nltk.pos_tag(newA)
        if tagged[0][1] in partsOfSpeech: newWords.append(word)  
    
numWords = len(newWords)
fd = FreqDist(newWords)

for key in fd.keys():
  print key,fd[key],float(fd[key])*100./numWords

