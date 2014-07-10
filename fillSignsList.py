
import sys
import numpy as np
import MySQLdb as MySQL

config_file = './.asl.mysql'

def write_to_database(list):
 
  myTable1 = "PeterPan1"
  con = MySQL.connect(read_default_file=config_file)
  cur = con.cursor()
  cur.execute('Drop table if exists %s' % (myTable))
  cur.execute('create table %s (Num int auto_increment, numLetters int, numPhonemes int, signName char(20), wordName char(100), primary key (Num))' % (myTable))

  for i in range(0,len(list)):
    comm = "insert into " + myTable1 + " (numLetters,numPhonemes,signName,wordName) values (" + str(list[0]) + ',' + str(list[1]) +  '"'+signArray[i]+'"' + "," + " " + '"'+loc[i]+'"' + ')'
    print comm
#    cur.execute(comm)
 
  sys.exit()   
  con.commit()
  con.close()

  def getPhonemes(myWord):
 
    arpabet = nltk.corpus.cmudict.dict()
    phonemes = arpabet[(myWord.lower())][0]
    myPhonemes = []
    for phoneme in phonemes:    
      if phoneme[-1] in "0123": phoneme = phoneme[:-1]
      if phoneme.lower() not in listOfPhonemes:  return []
      myPhonemes.append("phoneme_"+phoneme.lower()+".mp4")
    return myPhonemes


def main():

  path = "/Users/Arvi/SignVideos/"
  
  aslSign  = [str((line.split())[0]) for line in open("/Users/Arvi/my_bootstrap/static/log.dat")]
  aslLoc  = [str((line.split())[1]) for line in open("/Users/Arvi/my_bootstrap/static/log.dat")]  
  
  for i in range(0,len(aslLoc)):
    for j in range(len(aslLoc[i])-1,-1,-1):
      if aslLoc[i][j] == '/': break
    aslLoc[i] = aslLoc[i][j+1:]

#  for i in range(0,3):
#    print aslSign[i], aslLoc[i]
   
  write_to_database(aslSign,aslLoc)

if __name__ == "__main__":
  main()

