import sys
fileName = "wiki_travel.txt"
  
allWords = []
for word in [line for line in open(fileName)]:
  allWords += word.split()

sizeChunks = 100 #number of words per chunk.
numChunks = int(float(len(allWords))/float(sizeChunks))

ctr = 1
for st in range(0,(sizeChunks*numChunks),sizeChunks):
  chunk = ""
  for i in range(st,st+sizeChunks):
    chunk += allWords[i].lower()+" "
  
  f = open("chunks/wiki"+str(ctr), "w")
  f.write(chunk)
  f.close()
  ctr += 1
