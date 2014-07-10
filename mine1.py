
from bs4 import BeautifulSoup
import os
import sys
import re
from urllib2 import urlopen

def revstr(a):
  b = ""
  for i in range(len(a)-1,-1,-1): b += a[i]
  return b

path = "http://www.goodreads.com"

myUrl1 = "http://www.goodreads.com/genres/pre-k"
myUrl2 = "http://www.goodreads.com/genres/new_releases/childrens"

def getListOfBooks(myUrl):
  
  soup = BeautifulSoup(urlopen(myUrl).read())
  links = [str(val) for val in soup.find_all('a') if '<a href="/book/show/' in str(val)]
  books = []
  for link in links: 
    ss = ""
    for l in link[9:]:
      if l == '"': break
      ss += l
    books.append(path+ss)
  return books


bookUrls = getListOfBooks(myUrl1)
bookUrls += getListOfBooks(myUrl2)
#for book in bookUrls: print book  
#sys.exit()



# <span id="freeTextContainer723150042311518910">Laszlo is afraid of the dark. The dark is not afraid of Laszlo. <br><br>Laszlo lives in a house. The dark lives in the basement. <br>$

def getDescription(myUrl):

  allWords = str(urlopen(myUrl).read()).split()
  subset = ""
  found = False  
  for i in range(0,len(allWords)):
    if "readable" in allWords[i] and "stacked" in allWords[i+1]:
      found = True
      for j in range(i+4,i+100):
        if "</span>" in allWords[j]: break;
        if ("<br><br>" in allWords[j]) or ("id=" in allWords[j]):
          ss = ""
          for lp in range(len(allWords[j])-1,-1,-1):
            if allWords[j][lp] == '>': break
            ss += allWords[j][lp]
          allWords[j] = revstr(ss)  

        subset += allWords[j] + " "

  if not found: return ""
  ss = ""
  for lp in range(0,len(allWords[j])):
    if allWords[j][lp] == '<': break
    ss += allWords[j][lp]
  subset += ss
  listWords = subset.split()
#  print listWords
#  sys.exit()
  
  ss = ""
  for word in listWords:
    if "#" in word: continue
    if ">" in word: continue  
    if "<" in word: continue    
    if "/" in word: continue
    if "onclick" in word: continue
    if "class=" in word: continue
    ss += (word + " ")
  return ss+'\n'  

outf = open("data", "w")
for bookUrl in bookUrls:
  print "Getting description for: " + bookUrl
  outf.write(getDescription(bookUrl))
  outf.write("\n")
outf.close()
  
#myUrl = "http://www.goodreads.com/book/show/15790852-the-dark"
#print getDescription(myUrl)
