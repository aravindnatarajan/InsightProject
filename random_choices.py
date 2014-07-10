
import random
import sys

correctAnswers = [(word.split())[1] for word in open("ans")]

resultsFile =   "amazon_sunday_1.dat"
table = [word for word in open(resultsFile)][1:]
print (table[0].split(","))[2:7]
sys.exit()



choice = [(word.split())[1] for word in open("ans")]

random.shuffle(choice)

correct = 0
for i in range(0,len(correctAnswers)):
  if choice[i] == correctAnswers[i]:
    correct += 1
    print i+1,correct
    