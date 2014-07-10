
# Repeating digits in a string.
def isRepeat(string):
  for loop in range(0,len(string)):
    letter = string[loop]
    ctr = 0
    for i in range(loop,len(string)):
      if string[i] == letter: ctr += 1
    if ctr > 1: return False
  return True


#First non-repeating letter in a string. Order n*n
import sys
def nonRepeat(string):
  for letter in string:
    ctr = 0
    for letter2 in string:
      if letter == letter2: 
        if letter != ' ': ctr += 1  
    if ctr == 1: return letter


def nonRepeat(word):
  count = {}
  for c in word:
    if c not in count: count[c] = 0
    count[c] += 1
    print count
  
  for c in word:
    if count[c] == 1: return c
  
def main():
  word = "helloh"
  print nonRepeat(word)
  
if __name__ == '__main__':
  main()

  