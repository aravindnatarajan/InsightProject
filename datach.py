import numpy as np

def getData(fileName, col):
  table = [line for line in open(fileName)]
  data = [w.split(",")[col] for w in table][1:]
  data = [float(w) for w in data]
  return data

 
# file = "/Users/Arvi/Downloads/Everpix-Intelligence-master/Internal Metrics/Subscriptions_and_Revenues_(Subscriptions_Sold).csv"
file = "/Users/Arvi/Downloads/Everpix-Intelligence-master/Internal Metrics/SystemUsers(TotalUsers).csv"
for i in range(0,691,30):
  print np.sum(getData(file,1)[i:i+30])
#print (getData(file,1)[90:121])
     
