# 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

import nltk
import os
import numpy as np
import nltk.stem
import sys
import cv2

# This must be typed at the command prompt.
#os.system('export PYTHONPATH="/usr/local/lib/python2.7/site-packages:$PYTHONPATH"')
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

def exist(theWord, listSigns):
  

english_stemmer = nltk.stem.SnowballStemmer("english")

class StemmedTfidfVectorizer(TfidfVectorizer):
  def build_analyzer(self):
    analyzer = super(TfidfVectorizer, self). build_analyzer()
    return lambda doc: (english_stemmer.stem(w) for w in analyzer( doc))

class StemmedCountVectorizer( CountVectorizer):
  def build_analyzer( self):
    analyzer = super( StemmedCountVectorizer, self). build_analyzer()
    return lambda doc: (english_stemmer.stem(w) for w in analyzer( doc))

vec = StemmedTfidfVectorizer(min_df = 1, stop_words ='english', decode_error="ignore")
path = "/Users/Arvi/InsightProject/chunks/Ginger/"
allChunks = [open(path+f).read() for f in os.listdir(path)]

fileName = "/Users/Arvi/InsightProject/gingerbreadman.txt"
allWords = []
for word in [line for line in open(fileName)]:
  allWords += word.split()

from nltk.corpus import stopwords
stops = stopwords.words('english')
wordList = [str(word) for word in allWords if word not in stops]
tagged = nltk.pos_tag(wordList)
nouns = [word for word,pos in tagged if (pos == 'NN' or pos == 'VB')]
from nltk import FreqDist
fd = FreqDist(nouns)
maxLength = 25
if maxLength > len(fd.keys()): maxLength = len(fd.keys())
listOfWords = fd.keys()[:maxLength]
print listOfWords
listOfSigns = open("list_of_signs.dat").read()

print listOfSigns
 
#playVideo(listOfWords[0])
#print os.path.isfile("/Users/Arvi/ASLVideos/Love.mp4")

sys.exit()

X = vec.fit_transform(allChunks)
#num_samples,num_features = X.shape
#print num_samples, num_features

#sys.exit()

numClusters = 10
km = KMeans(n_clusters=numClusters,init="random",n_init=1,verbose=1)
km.fit(X)

testPost = "guns ammunition jail sadness horror death graves hiding raids"
#testPost = "guns"
#"When it came to the little gingerbread man she felt sorry for him and gave him more color than the others. It doesn't matter he's small, she thought, He'll still be tasty." 
testPostVec = vec.transform([testPost])
testPostLabel = km.predict(testPostVec)[0]
similarIndices = (km.labels_==testPostLabel).nonzero()[0]

similar = []
for i in similarIndices:
  dist = np.linalg.norm((testPostVec - X[i]). toarray())
  similar.append((dist, allChunks[i]))
similar = sorted(similar)
print len(similar)
print similar[0]


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

