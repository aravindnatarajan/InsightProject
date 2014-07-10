
import sys
import numpy as np
import random

def whichSign(sign):

  digits = "0123456789"
  num = ""  
  for letter in sign:
    if letter in digits: num += letter
  return int(num)

def alphaOnly(string):
  ans = ""
  alphas = "abcdefghijklmnopqrstuvwxyz"
  for letter in string.lower():
    if letter in alphas:
      ans += letter
  return ans
   
dataFile = "amazon_sunday_2.dat"
ansFile = "ans_amazon_july6"

#dataFile = "amazon_july6.dat"
#ansFile = "ans_amazon_july6"

# "HITID","Sign_Name","Choice_1","Choice_2","Choice_3","Choice_4","Choice_5","Worker","Answer","Date"

correctAnswers = [(word.split())[1] for word in open(ansFile)]
resultsFile = dataFile  
table = [word for word in open(resultsFile)][1:]
signNumber = [whichSign((word.split(","))[1]) for word in table]
choice   = [whichSign((word.split(","))[8]) for word in table]


workers   = [(word.split(","))[7] for word in table]
workers_set   = [w for w in set([(word.split(","))[7] for word in table])]

print workers_set
sys.exit()

"""
for worker in workers_set:
  ct = 0
  for w in workers:
    if w == worker: ct += 1
  print worker,ct
    
  
sys.exit()
"""

userChoice = []
rndChoice = []
for i in range(0,len(signNumber)):
  for j in range(0,len(signNumber)):
    if signNumber[j] == i+1: 
      userChoice.append( alphaOnly( ((table[j].split(","))[2:7])[choice[j]-1] )  )
      rndChoice.append( alphaOnly(  (table[j].split(","))[2 + random.randint(0,4)]   )   )
      break

correct = 0
for i in range(0,len(signNumber)):
  if userChoice[i] == correctAnswers[i]: correct += 1
  print i+1,correct
   
    
sys.exit()


for i in range(0,300):
  print signName[i], choice[i]
sys.exit(0)

# whichSign(table[0][0])
whichSign("www.funwithasl.net/static/sign187.html")
sys.exit()

col1 = [word.split(",") for word in table]
for i in range(1,5):
  print col1[i][1], col1[i][8]
 

#"HITID","Sign_Name","Choice_1","Choice_2","Choice_3","Choice_4","Choice_5","Worker","Answer","Date"

