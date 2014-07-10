
import sys
import numpy as np
import MySQLdb as MySQL

config_file = './.asl.mysql'

def write_to_database(signArray,loc):
 
  myTable = "phonemes"
  con = MySQL.connect(read_default_file=config_file)
  cur = con.cursor()
  cur.execute('Drop table if exists %s' % (myTable))
  cur.execute('create table %s (Num int auto_increment, phonemeName char(20), signLocation char(100), primary key (Num))' % (myTable))

  for i in range(0,len(signArray)):       
    comm = "insert into " + myTable + " (signName,signLocation) values (" + '"'+signArray[i]+'"' + "," + " " + '"'+loc[i]+'"' + ')'
    cur.execute(comm)
    
  con.commit()
  con.close()


def main():

  path = "/Users/Arvi/SignVideos/"
  
  aslSign  = [str((line.split())[0]) for line in open("/Users/Arvi/my_bootstrap/static/log.dat")]
  aslLoc  = [str((line.split())[1]) for line in open("/Users/Arvi/my_bootstrap/static/log.dat")]  
  
  for i in range(0,len(aslLoc)):
    for j in range(len(aslLoc[i])-1,-1,-1):
      if aslLoc[i][j] == '/': break
    aslLoc[i] = aslLoc[i][j+1:]

  write_to_database(aslSign,aslLoc)

if __name__ == "__main__":
  main()

