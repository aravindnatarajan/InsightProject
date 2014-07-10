
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
   
correctAnswers = [(word.split())[1] for word in open("ans")]
resultsFile =   "amazon_sunday_1.dat"
table = [word for word in open(resultsFile)][1:]
signNumber = [whichSign((word.split(","))[1]) for word in table]
choice   = [whichSign((word.split(","))[8]) for word in table]


rndAll = []
number = 100
for lp in range(0,number):

  rndChoice = []
  for i in range(0,len(signNumber)):
    for j in range(0,len(signNumber)):
      if signNumber[j] == i+1: 
        rndChoice.append( alphaOnly(  (table[j].split(","))[2 + random.randint(0,4)]   )   )
        break

  rndCorrect = 0
  rndCorrectArray = []
  for i in range(0,len(signNumber)):
    if rndChoice[i] == correctAnswers[i]: rndCorrect += 1
    rndCorrectArray.append(rndCorrect)

  rndAll.append(rndCorrectArray)
  

for lp in range(0,len(signNumber)):
  print lp+1, np.mean([rndAll[i][lp] for i in range(0,number)]), np.std([rndAll[i][lp] for i in range(0,number)])

sys.exit()   

#  print i+1,userChoice[i],correctAnswers[i],correct,rndCorrect  
#print correct,rndCorrect  
print rndCorrectArray
  
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

