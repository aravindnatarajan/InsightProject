
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

import nltk
import nltk.stem
from nltk import FreqDist
from nltk.corpus import stopwords

import os
import numpy as np
import sys
import cv2

# This must be typed at the command prompt.
#os.system('export PYTHONPATH="/usr/local/lib/python2.7/site-packages:$PYTHONPATH"')

"""
def playVideo(fileName):

  cap = cv2.VideoCapture(fileName)
  while(cap.isOpened()):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()
"""
  
path = "/Users/Arvi/InsightProject/childrens_books/"
allWords = []
for word in [line.lower() for line in [open(path+f).read() for f in os.listdir(path)]]:
  allWords += word.split()

for i in range(0,len(allWords)):
  ss = ""
  for letter in allWords[i]:
    if letter not in '\\;,?.><!"-+' and letter not in "'": 
      ss += letter
  allWords[i] = ss

english_stemmer = nltk.stem.SnowballStemmer("english")   
stops = stopwords.words('english')
wordList = [word.lower() for word in allWords if word.lower() not in stops]
wordList = FreqDist(wordList).keys()

tagged = nltk.pos_tag(wordList)
partsOfSpeech = ['NN', 'V', 'VB', 'VBN', 'VBZ', 'ADJ']
newWords = [word for word,pos in tagged if pos in partsOfSpeech]

dictOfSigns = [sign.rstrip() for sign in open("list_of_signs.dat")]
databaseWords = []
databaseSigns = []

for i in range(0,len(newWords)):
  for j in range(0,len(dictOfSigns)):
    if newWords[i].lower()+".mp4" == dictOfSigns[j].lower():
      databaseWords.append(newWords[i])
      databaseSigns.append(dictOfSigns[j])

for i in range(0,len(databaseWords)):
  print databaseWords[i]
#  print databaseWords[i], databaseSigns[i]
 