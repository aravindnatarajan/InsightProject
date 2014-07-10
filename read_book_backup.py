
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
import MySQLdb as MySQL
import sys
import random

listOfPhonemes =  ['aa', 'ae', 'ah', 'ao', 'aw', 'ax', 'ay', 'b', 'ch', 'd', 'dh', 'eh', 'el', 'em', 'en', 'eng', 'er', 'ey', 'f', 'g', 'hh', 'ih', 'iy', 'jh', 'k', 'l', 'm', 'n', 'ng', 'ow', 'oy', 'p', 'qu', 'r', 's', 'sh', 't', 'th', 'uh', 'uw', 'v', 'w', 'x', 'y', 'z', 'zh']
config_file = './.asl.mysql'


def findWord(theWord):

  con = MySQL.connect(read_default_file=config_file)
  cur = con.cursor()
  comm = 'select signLocation from signs where signName = ' + '"'+theWord+'"'
  cur.execute(comm)
  the_tuple = cur.fetchall()
  if len(the_tuple) == 0: return ""
  else: return str(the_tuple[0][0])
  con.close()


english_stemmer = nltk.stem.SnowballStemmer("english")

class StemmedTfidfVectorizer(TfidfVectorizer):
  def build_analyzer(self):
    analyzer = super(TfidfVectorizer, self). build_analyzer()
    return lambda doc: (english_stemmer.stem(w) for w in analyzer( doc))

class StemmedCountVectorizer( CountVectorizer):
  def build_analyzer( self):
    analyzer = super( StemmedCountVectorizer, self). build_analyzer()
    return lambda doc: (english_stemmer.stem(w) for w in analyzer( doc))

path = "/Users/Arvi/InsightProject/"

"""
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
listSigns = [((word.split())[0]).lower() for word in open("/Users/Arvi/my_bootstrap/static/log.dat")]

#partsOfSpeech = ['NN', 'NNS', 'VB',  'JJ']
partsOfSpeech = ['NN', 'NNS', 'NNP']

trainingData = nltk.corpus.treebank.tagged_sents()
unigram_tagger = nltk.NgramTagger(n=1, train=trainingData)
bigram_tagger  = nltk.NgramTagger(n=2, train= trainingData, backoff=unigram_tagger)

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
  word = ss   

  if word in stops: continue    
  if word in listSigns:
    newA = []
    newA.append(word)
    tagged = bigram_tagger.tag(newA)
    if tagged[0][1] not in partsOfSpeech:
      newA[0] = newA[0][0].upper() + newA[0][1:]
      tagged = bigram_tagger.tag(newA)
      if tagged[0][1] in partsOfSpeech: newWords.append(word)  
    
numWords = len(newWords)
fd = FreqDist(newWords)

for key in fd.keys():
  print key,fd[key],float(fd[key])*100./numWords

sys.exit()

sys.exit()

allWords = cleanUp(theArr)
ctr = 0
for word in allWords:
  if word.lower() == "horse": ctr += 1
  
print ctr
sys.exit()



print len(parts)
sys.exit()

listSigns = []
listFreq = []
fd = FreqDist(parts)

cutoff = 100
ctr = 0
for key in fd.keys():
  key = key.lower()
  ss = ""
  for letter in key:
    if letter in "abcdefghijklmnopqrstuvwxyz":
      ss += letter      
  key = ss    
  if findWord(key) != "":
    print key, fd[key]
    ctr += 1      
  if ctr > 100: break

     
sys.exit()
 
"""    
    listSigns.append(key)
    listFreq.append(fd[key])
    if cutoff > 10: break
    cutoff += 1
"""
for i in range(0,5):
  print listSigns[i], listFreq[i]
  
#for i in range(0,1):
#  print [t.split() for t in allW1[i]]



"""
from nltk.corpus import stopwords
stops = stopwords.words('english')
newTokens = [str(token) for token in tokens if token not in stops]
nltk.pos_tag(newTokens)

from nltk import FreqDist
fd = FreqDist(nouns)
"""


sys.exit()

allWords = []
for word in allW1:
  ss = ""  
  for letter in word:
    if letter not in ".0123456789?,<>?/;":
      ss += (letter.lower())
      
  if ss != '' and ss[-1] != "'" and ss[-1] != '"' and ss[0] != "'" and ss[0] != '"': allWords.append(ss)
  
print allWords
sys.exit()
  
  
allW = [word for word in allW1 if word not in "1234567890"]
for i in range(0,20):
  print allW[i]
sys.exit()  

allWords1 = [open(path+f).read() for f in os.listdir(path)]
allWords = [t.split() for t in allWords1]
for i in range(0,20):
  print allWords[i]


sys.exit()

allChunks = [open(path+f).read() for f in os.listdir(path)]

#print allChunks
#sys.exit()


"""
path = "/Users/Arvi/InsightProject/chunks/"
allPaths =  [(path+f) for f in os.listdir(path)]

allWords = []
for i in range(0,len(allPaths)):
  path = allPaths[i]+'/'
  for word in [line.lower() for line in [open(path+f).read() for f in os.listdir(path)]]:
    allWords += word
#    allWords += word.split()

print allWords
"""



"""
for i in range(0,len(allWords)):
  ss = ""
  for letter in allWords[i]:
    if letter not in '\\;,?.><!"-+' and letter not in "'": 
      ss += letter
  allWords[i] = ss

print allWords[:10]
sys.exit()
"""

vec = StemmedTfidfVectorizer(min_df = 1, stop_words ='english', decode_error="ignore")
X = vec.fit_transform(allChunks)
#num_samples,num_features = X.shape
#print num_samples, num_features
#sys.exit()

numClusters = 10
km = KMeans(n_clusters=numClusters,init="random",n_init=1,verbose=1)
km.fit(X)

testPost = str(sys.argv[1])

#testPost = "driving delays flight ticket cost food photographs scenic mountains food spicy culture passport safety taxi hotel vacation people colorful backpacking hiking"

#testPost = "Iran Saudi Arabia Egypt gasoline price guns desert war peace mess democrat presiedent white house talks diplomacy united nations religion state terrrorism human rights"

#testPost = "play summer blue sky mountains goats milk birds flowers snow pretty lady book read poem song dance happy dinner apple" 

 


testPostVec = vec.transform([testPost])
testPostLabel = km.predict(testPostVec)[0]
similarIndices = (km.labels_==testPostLabel).nonzero()[0]

similar = []
for i in similarIndices:
  dist = np.linalg.norm((testPostVec - X[i]). toarray())
  similar.append((dist, allChunks[i]))
similar = sorted(similar)

print similar[0]
print "\n"
print similar[1]
print "\n"
print similar[2]


sys.exit()

print similarIndices


print km.cluster_centers_


sys.exit()

#print vec.get_feature_names()
#sys.exit()

#theWords = vec.get_feature_names()
newPost = "rainbow"
newPostVec = vec.transform([newPost])
newPostVecNorm = newPostVec / np.linalg.norm(newPostVec.toarray())

 
for i in range(0,num_samples):
  post = posts[i]
  postVec = X.getrow(i)
  postVecNorm = postVec / np.linalg.norm(postVec.toarray())
  print np.linalg.norm((postVecNorm - newPostVecNorm).toarray())

