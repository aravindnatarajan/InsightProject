
import numpy as np
import matplotlib.pyplot as plt
import sys
import json

  
fileName = "getglue_sample.json"
lines = []
num = 1000000
f = open(fileName)
for i in range(0,num):
  l = f.readline()
  lines.append(json.loads(l))

#print lines[0:10]
  
#  line.append(open(fileName).readline())

#print lines[0]

#times = [lines[i]['timestamp'] for i in range(0,num)]
#print times

#for i in range(0,10):
#  print lines[i]['title'], lines[i]['action']

theMovie = "G.I. Joe: Rise of Cobra"
titles = [w for w in set([lines[i]['title'] for i in range(0,num)])]
titlesLiked = []
lp = 0
like2009 = 0
like2010 = 0
like2011 = 0
like2012 = 0
like2013 = 0
like2014 = 0

movieList = [
"Avatar: The Last Airbender",
"Blade",
"From Russia With Love",
"Killing Me Softly",
"Tango and Cash",
"Jurassic Park",
"The Black Scorpion",
"Steven Seagal Lawman",
"Doctor Who: Enlightenment",
"A Streetcar Named Desire"
]


for movie in movieList:
  for i in range(0,num):
    if lines[i]['title'] == movie:
      if lines[i]['action'] == 'Liked': 
        if lines[i]['timestamp'][0:4] == '2009':    
          like2009 += 1
        if lines[i]['timestamp'][0:4] == '2010':    
          like2010 += 1
        if lines[i]['timestamp'][0:4] == '2011':    
          like2011 += 1
        if lines[i]['timestamp'][0:4] == '2012':    
          like2012 += 1
        if lines[i]['timestamp'][0:4] == '2013':
          like2013 += 1
        if lines[i]['timestamp'][0:4] == '2014':
          like2014 += 1
          
        totalLikes = like2009 + like2010 + like2011 + like2012 + like2013 + like2014  

          
  print movie,like2009, like2010, like2011, like2012, like2013, totalLikes
