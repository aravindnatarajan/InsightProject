from urllib2 import urlopen
from bs4 import BeautifulSoup
import sys
import numpy as np
import os

path = "http://www.handspeak.com"

def revstr(a):
  b = ""
  for i in range(len(a)-1,-1,-1): b += a[i]
  return b
       
def getFileNames(word):

  # Returns list of filenames of videos. Return empty if word not found. 
  
  url = "http://www.handspeak.com/word/search.php?wordID="+word+"&submitword=Find"    
  soup = BeautifulSoup(urlopen(url).read())  
  links = [str(val) for val in soup.find_all('video') ]
  if links == []: return links
  
  ll = [val for val in links]
  fileNames = []
  for lp in range(0,len(ll)):
    quo = 0; fileName = ""
    for val in ll[lp]:
      if quo == 7: fileName += val
      if val == '"': quo += 1
    fileNames.append(path + fileName[:-1])
  return fileNames


outputPath = "/Users/Arvi/SignVideos/"  
def downloadVideos(fileNames,theWord):


#  for i in range(0,len(fileNames)):
  for i in range(0,1):  
    os.system("curl " + fileNames[i] + " -# -o  " +  outputPath + theWord + ".mp4")  
#    os.system("curl " + fileNames[i] + " -# -o  " +  outputPath + theWord + str(i+1) + ".mp4")

wordFile = sys.argv[1]
listOfWords = [name.rstrip() for name in open(wordFile)]
#print listOfWords
#sys.exit()

f = open(outputPath+"logsub.dat", 'a')
for theWord in listOfWords:
  fileNames = getFileNames(theWord)
  if len(fileNames) == 0:
    print "No videos found for " + theWord
  else:  
    print theWord + " videos found for " + str(len(fileNames))
    downloadVideos(fileNames,theWord)
    f.write(theWord + " " + outputPath+theWord+".mp4"+'\n')
f.close()  
  
