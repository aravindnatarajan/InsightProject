
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

import nltk
import nltk.stem
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

import os
import numpy as np
import sys

english_stemmer = nltk.stem.SnowballStemmer("english")

class StemmedTfidfVectorizer(TfidfVectorizer):
  def build_analyzer(self):
    analyzer = super(TfidfVectorizer, self). build_analyzer()
    return lambda doc: (english_stemmer.stem(w) for w in analyzer( doc))

class StemmedCountVectorizer( CountVectorizer):
  def build_analyzer( self):
    analyzer = super( StemmedCountVectorizer, self). build_analyzer()
    return lambda doc: (english_stemmer.stem(w) for w in analyzer( doc))

def cleanUp(rawWords):
  
  stops = [t.lower() for t in stopwords.words('english')]

  sumarr = []
  for i in range(0,len(rawWords)):
    arr = [t.lower() for t in rawWords[i].split()]
    for word in arr: 
      if word not in stops:
        sumarr.append(word.lower())
  
  punct1 = '.,?/><";![]:@#$%&*()'
  punct2 = "'"
#  for i in range(0,len(sumarr)):
  for i in range(0,1):  
    if r'\\xe2' in sumarr[i]: sumarr[i] = '*'
    if len(sumarr[i]) > 1:
      if sumarr[i][-1] in punct1 or sumarr[i][-1] in punct2: sumarr[i] = sumarr[i][:-1]   # delete punctuation at the end of the word.
      if sumarr[i][-1] in punct1 or sumarr[i][-1] in punct2: sumarr[i] = sumarr[i][:-1]   # once more to delete double punctuations.      if sumarr[i][0] in punct1 or sumarr[i][0] in punct2: sumarr[i] = sumarr[i][1:]   # delete punctuation at the start of the word.      
    if len(sumarr[i]) > 2:
#      print sumarr
      if sumarr[i][-2] == "'" and sumarr[i][-1] == 's' : sumarr[i] = sumarr[i][:-2] # so that Jim's --> Jim.
      if sumarr[i][-2] == "'" and sumarr[i][-1] == 'm' : sumarr[i] = sumarr[i][:-2] # so that I'm --> I.
    if len(sumarr[i]) > 3:    
      if sumarr[i][-3] == 'n' and sumarr[i][-2] == "'" and sumarr[i][-1] == 't' : sumarr[i] = sumarr[i][:-3] # so that isn't --> is. Not is a stop word.
    
  lmtzr = WordNetLemmatizer()
  return [lmtzr.lemmatize(t) for t in sumarr if ("'" not in t and t not in stops)]


    

#print getPhonemes("Tunnel")
#sys.exit()

path = "/Users/Arvi/InsightProject/books/"

"""
"""

allFiles = [f for f in os.listdir(path)]

theArr = [open(path+f).read() for f in os.listdir(path)]
allWords = cleanUp(theArr)

tagged = nltk.pos_tag(allWords)
partsOfSpeech = ['NN', 'NNS' 'VB', 'VBD', 'VBZ'] #, 'NNS', 'JJ', 'RB', 'VB', 'VBD', 'VBZ']
parts = [word for word,pos in tagged if pos in partsOfSpeech]


# parts = [part for part in allWords]
fd = FreqDist(parts)
for key in  fd.keys(): 
  print key, fd[key]

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

