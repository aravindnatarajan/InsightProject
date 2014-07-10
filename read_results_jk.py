
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
   
correctAnswers = [(word.split())[1] for word in open("ans_amazon_sunday_1")]
resultsFile =   "amazon_sunday_1.dat"
table = [word for word in open(resultsFile)][1:]
signNumber = [whichSign((word.split(","))[1]) for word in table]
choice   = [whichSign((word.split(","))[8]) for word in table]


userChoice = []
rndChoice = []
for i in range(0,len(signNumber)):
  for j in range(0,len(signNumber)):
    if signNumber[j] == i+1: 
      userChoice.append( alphaOnly( ((table[j].split(","))[2:7])[choice[j]-1] )  )
      rndChoice.append( alphaOnly(  (table[j].split(","))[2 + random.randint(0,4)]   )   )
      break


rndCorrect = 0

#list = []
#div = 25
#for st in range(0,16):
correct = 0
for i in range(0,len(signNumber)):
#  for i in range(div*st,div*(st+1)):  
  if userChoice[i] == correctAnswers[i]: correct += 1
#  if rndChoice[i] == correctAnswers[i]: rndCorrect += 1
#  print i+1,userChoice[i],correctAnswers[i],correct,rndCorrect  
  print i+1,correct
#  list.append(float(correct)/div)
#print np.mean(list)
#print np.std(list)
# print correct,rndCorrect  
  
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

