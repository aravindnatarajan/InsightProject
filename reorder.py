
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




################################################################################################


def bubbleSort(dummy,A): # Bubble Sort Algorithm
  for i in range(len(A)):
    for j in range(i+1, len(A)):
      if A[j] > A[i]: 
        A[j],A[i] = A[i],A[j]
        dummy[j],dummy[i] = dummy[i],dummy[j]

  return dummy,A

files = [
"analysis/analysis_AliceWonderland.dat",
"analysis/analysis_footprints_sea_shore.dat",
"analysis/analysis_mother_goose.dat",
"analysis/analysis_BlackBeauty.dat",
"analysis/analysis_gift_magi.dat",
"analysis/analysis_peter_pan.dat",
"analysis/analysis_BlackBeauty.dat",
"analysis/analysis_heidi.dat",
"analysis/analysis_secret_garden.dat",
"analysis/analysis_anne_green_gables.dat",
"analysis/analysis_hiawatha.dat",
"analysis/analysis_treasure_island.dat",
"analysis/analysis_anne_green_gables.dat",
"analysis/analysis_jack_jill.dat",
"analysis/analysis_wizard_of_oz.dat",
"analysis/analysis_arabian_nights.dat",
"analysis/analysis_jungle_book.dat",
"analysis/jp"
]

allWords = []
for i in range(0,len(files)):
  for w in [(word.split())[0] for word in open(files[i])]:
    allWords.append(w)
 
allWordsSet = [word for word in set(allWords)]

frequencies = []
 
for theWord in allWordsSet:  
  sumFreq = 0
  for whichFile in range(0,len(files)):
    words = [(word.split())[0] for word in open(files[whichFile])]
    freq  = [int((word.split())[1]) for word in open(files[whichFile])]
 
    for i in range(0,len(words)):
      if theWord == words[i]:
        sumFreq += freq[i]
  frequencies.append(sumFreq)


# new weights.
# for i in range(0,len(allWordsSet)):
#   print allWordsSet[i], frequencies[i]


       

listWords   = [word for word in allWordsSet]
listWeights = [int(f) for f in frequencies]

#listWords   = [(word.split())[0] for word in open("weights.dat")]
#listWeights = [int((word.split())[1]) for word in open("weights.dat")]

words = [(word.split())[0] for word in open(sys.argv[1])]
num = [int((word.split())[1]) for word in open(sys.argv[1])]
freq = [float((word.split())[2]) for word in open(sys.argv[1])]

newWeights = []
newWords = []
for whichWord in range(0,len(words)):
  for i in range(0,len(listWords)):
    if words[whichWord] == listWords[i]:
      newWeights.append(freq[whichWord]*(float(num[whichWord])/float(listWeights[i])))
      newWords.append(words[whichWord])


sortedWords, sortedWeights = bubbleSort(newWords,newWeights)
for i in range(0,len(newWords)):
  print sortedWords[i], sortedWeights[i]


