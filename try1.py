
import numpy as np
import matplotlib.pyplot as plt
import sys

fileName = "/Users/Arvi/Downloads/Everpix-Intelligence-master/InternalMetrics/SystemUsers(TotalUsers).csv"

data = np.genfromtxt(fileName, delimiter=",", usecols=(1,2), skip_header=1)
months = [i for i in range(0,20)]
users  = [1E-6*np.sum(data[(30*month):30*(month+1),1]) for month in months]

plt.plot(months,users,c="red",linewidth=3)
plt.xlabel("Months")
plt.ylabel("Users in Millions")
plt.show()


#print data[:,0]
#print data[:,1]
