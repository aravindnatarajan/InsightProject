
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


def getSigns(wordsDatabase):

  listWords = [(word.split())[0] for word in open(wordsDatabase)]    
  myWords = []
  myLocs = []
  for word in listWords:
    loc = findWord(word)
    if loc != "": 
      myWords.append(word)
      myLocs.append(loc)
          
  return myWords,myLocs

def getList(wordNum,words,signs,numSigns):

  import nltk
  import random
  
  def getRand5(maxLen, howMany, wordNum):

    if maxLen-1 < howMany:
      print "Please send me a larger list."
      sys.exit()
    
    myList = []  
    while len(myList) < howMany:
      r =  random.randrange(0,maxLen) 
      if r != wordNum and r not in myList: myList.append(r)
    return myList

  def getPhonemes(myWord):
 
    arpabet = nltk.corpus.cmudict.dict()
    phonemes = arpabet[(myWord.lower())][0]
    myPhonemes = []
    for phoneme in phonemes:    
      if phoneme[-1] in "0123": phoneme = phoneme[:-1]
      if phoneme.lower() not in listOfPhonemes:  return []
      myPhonemes.append("phoneme_"+phoneme.lower()+".mp4")
    return myPhonemes

  wrongChoices = 4
  word = words[wordNum]
  sign = signs[wordNum]
  
  wrongNum = getRand5(numSigns,wrongChoices,wordNum)
  choices = ["", "", "", "", "" ]
  choices[0] = words[wordNum]
  for i in range(0,4):
    choices[i+1] = words[wrongNum[i]]
  random.shuffle(choices)

  myList = []
  myList.append(len(word))
  phons = getPhonemes(word)
  if phons == []: return []

  myList.append(len(phons))
  
  myList.append(sign)
  myList.append(word)
  for i in range(0,5): myList.append(choices[i])
  for letter in word:  myList.append(letter.upper()+".jpg")
  for phon in phons:   myList.append(phon)
  return myList  

#  videos = [5,4,"happy.mp4", "Happy", "Happy", "Cold", "Hungry", "Sleepy", "Bored", "H.jpg", "A.jpg", "P.jpg", "P.jpg", "Y.jpg", "hh.mp4", "ae.mp4", "p.mp4", "iy.mp4"]

def write_to_database(list,title):
 
  myTable1 = title + "1"
  myTable2 = title + "2"
  myTable3 = title + "3"
  myTable4 = title + "4"
      
  con = MySQL.connect(read_default_file=config_file)
  cur = con.cursor()
  cur.execute('Drop table if exists %s' % (myTable1))
  cur.execute('create table %s (Num int auto_increment, numLetters int, numPhonemes int, signName char(20), wordName char(100), primary key (Num))' % (myTable1))

  for i in range(0,len(list)):  
    comm = "insert into " + myTable1 + " (numLetters,numPhonemes,signName,wordName) values (" +  str(list[i][0]) + ',' + str(list[i][1]) + ', "' + list[i][2] + '",' + ' "' + list[i][3] + '"' +  ')'
    cur.execute(comm)
 
  cur.execute('Drop table if exists %s' % (myTable2))
  cur.execute('create table %s (signNum int, choice char(100))' % (myTable2))

  for i in range(0,len(list)):  
    for j in range(0,5):
      comm = "insert into " + myTable2 + " (signNum,choice) values (" +  str(i+1) + ',' + '"'+str(list[i][4+j])+'"' +   ')'    
      cur.execute(comm)   
      
  cur.execute('Drop table if exists %s' % (myTable3))
  cur.execute('create table %s (signNum int, letter char(5))' % (myTable3))

  for i in range(0,len(list)):  
    for j in range(0,list[i][0]):
      comm = "insert into " + myTable3 + " (signNum,letter) values (" +  str(i+1) + ',' + '"'+str(list[i][9+j])+'"' +   ')'    
      cur.execute(comm)   

  cur.execute('Drop table if exists %s' % (myTable4))
  cur.execute('create table %s (signNum int, phoneme char(50))' % (myTable4))

  for i in range(0,len(list)):  
    for j in range(0,list[i][1]):
      comm = "insert into " + myTable4 + " (signNum,phoneme) values (" +  str(i+1) + ',' + '"'+str(list[i][9+list[i][0]+j])+'"' +   ')' 
      cur.execute(comm)   
      
  con.commit()
  con.close()


def makeList(key, title):

  con = MySQL.connect(read_default_file=config_file)
  cur = con.cursor()
  
  table1 = title + "1"
  table2 = title + "2"
  table3 = title + "3"
  table4 = title + "4"
  myList = []
  
  comm = 'select * from ' + table1 + " where Num = " + str(key)
  cur.execute(comm)
  the_tuple = cur.fetchall()
  numL = int(the_tuple[0][1])
  numP = int(the_tuple[0][2])    
  myList.append(numL)
  myList.append(numP)
  myList.append(str(the_tuple[0][3]))   
  myList.append(str(the_tuple[0][4]))     

  comm = 'select choice from ' + table2 + " where signNum = " + str(key)
  cur.execute(comm)
  the_tuple = cur.fetchall()  
  for i in range(0,5):
    myList.append(str(the_tuple[i][0]))   

  comm = 'select letter from ' + table3 + " where signNum = " + str(key)
  cur.execute(comm)
  the_tuple = cur.fetchall()  
  for i in range(0,numL):
    myList.append(str(the_tuple[i][0]))

  comm = 'select phoneme from ' + table4 + " where signNum = " + str(key)
  cur.execute(comm)
  the_tuple = cur.fetchall()
  
  for i in range(0,numP):
    myList.append(str(the_tuple[i][0]))
    
  return myList
  



def main():  

  fileName = sys.argv[1]
  title = sys.argv[2]  
  choices = [4,5,6,7,8]
  random.shuffle(choices)
  
#  python read_from_db.py reanalysis/reanalysis_peter_pan.dat PeterPan
  
  
  words,signs = getSigns(fileName)
  
  numSigns = 103
  if len(words) < numSigns: numSigns = len(words)
  wordNum = 0
  
  bigList = []
  for wordNum in range(0,numSigns):
    list = getList(wordNum,words,signs,numSigns)
    if list != []:  bigList.append(list)

  fileName = "sign"
  out1 = open("list", "a")
  out2 = open("ans", "a")  
  offset = int(sys.argv[3])
  lim = 50
  for i in range(0,lim):

    out = open(fileName+str(offset+i+1)+".html", "w")  
    out.write("<html>\n")
    out.write('<body bgcolor="black">\n')
    out.write('<center><video width="420" height="420"  src="http://www.funwithasl.net/static/'+str(bigList[i][2])+'" ' + 'type="video/mp4" controls autoplay></video></center> \n')
    out.write("</body>\n")
    out.write("</html>\n")
    out.close()
    
    out1.write("www.funwithasl.net/static/sign"+str(offset+i+1) + ".html, " + str(bigList[i][choices[0]]) + ", " + str(bigList[i][choices[1]]) + ", " + str(bigList[i][choices[2]]) + ", " + str(bigList[i][choices[3]]) + ", " + str(bigList[i][choices[4]]) + "\n")
    out2.write("sign"+ str(offset+i+1) + "  " + str(bigList[i][3]) + "\n")
    
  out1.close()  
  out2.close()    
  sys.exit()
  
  write_to_database(bigList,title)      
  

if __name__ == '__main__':
  main()
  