
import sys

def bubbleSort(dummy,A): # Bubble Sort Algorithm
  for i in range(len(A)):
    for j in range(i+1, len(A)):
      if A[j] > A[i]: 
        A[j],A[i] = A[i],A[j]
        dummy[j],dummy[i] = dummy[i],dummy[j]
       
  return dummy,A

listWords   = [(word.split())[0] for word in open("weights.dat")]
listWeights = [int((word.split())[1]) for word in open("weights.dat")]

words = [(word.split())[0] for word in open(sys.argv[1])]
num = [int((word.split())[1]) for word in open(sys.argv[1])]
freq = [float((word.split())[2]) for word in open(sys.argv[1])]

newWeights = []
newWords = []
for whichWord in range(0,len(words)):
  for i in range(0,len(listWords)):
    if words[whichWord] == listWords[i]:
      newWeights.append(freq[whichWord]*(float(num[whichWord])/float(listWeights[i])))
      newWords.append(words[whichWord])


sortedWords, sortedWeights = bubbleSort(newWords,newWeights)
for i in range(0,len(newWords)):
  print sortedWords[i], sortedWeights[i]

