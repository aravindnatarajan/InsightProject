
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

# import cv2

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

"""
tokens = nltk.word_tokenize(words)
from nltk.corpus import stopwords
stops = stopwords.words('english')
newTokens = [str(token) for token in tokens if token not in stops]
nltk.pos_tag(newTokens)

tagged = nltk.pos_tag(newTokens)
nouns = [word for word,pos in tagged if pos == 'NN']
from nltk import FreqDist
fd = FreqDist(nouns)
"""

#def exist(theWord, listSigns):
  

english_stemmer = nltk.stem.SnowballStemmer("english")

class StemmedTfidfVectorizer(TfidfVectorizer):
  def build_analyzer(self):
    analyzer = super(TfidfVectorizer, self). build_analyzer()
    return lambda doc: (english_stemmer.stem(w) for w in analyzer( doc))

class StemmedCountVectorizer( CountVectorizer):
  def build_analyzer( self):
    analyzer = super( StemmedCountVectorizer, self). build_analyzer()
    return lambda doc: (english_stemmer.stem(w) for w in analyzer( doc))


path = "/Users/Arvi/InsightProject/allChunks/"
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

