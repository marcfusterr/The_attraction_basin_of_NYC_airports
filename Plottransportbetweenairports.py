# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:11:00 2017

@author: mfuster
"""

import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import datetime
from datetime import datetime

#create 24 hour list
hour24=[]
for i in range(24):
    hour24.append(i)
    
    """first jl then lj, further info see bottom"""


#reading
df=pd.read_csv('/home/mfuster/Desktop/datacorrected/2013lj.csv',skipinitialspace=True)
#adding to list
t1=df['pickup_datetime'].values.tolist()
t2=df['dropoff_datetime'].values.tolist()

#convert to datetime format
for i in range(len(t1)):
    t1[i] = datetime.strptime(t1[i], '%Y-%m-%d %H:%M:%S')
    t2[i] = datetime.strptime(t2[i], '%Y-%m-%d %H:%M:%S')
#to substract lists, use np.array
t1=np.array(t1)
t2=np.array(t2)

t=t2-t1


#convert to minutes of travel
for i in range(len(t)):
    t[i]=np.float(t[i].total_seconds()/60)
    
#delete less than 5 minutes and more than 120 minutes
t=t[(t>5.)&(t<240.)]

    
#histogram of time from
"""
plt.figure()
n, bins, patches = plt.hist(t, 50, facecolor='green', alpha=0.75)
plt.xlim(0,160)
plt.xlabel('Minutes')
plt.ylabel('Number of travels in 2013')
plt.title('From JFK to Laguardia')
"""
#create hour list but not 24 elements, of all elements
hour=[]
for i in range(len(t)):
    hour.append(t1[i].hour) #from 0 to 23
    

#create a dictionaty for making statistics
elements={}
for i in range(24):
    elements['list'+str(i)]=[]


#fulfil the dictionary
for i in range(24):
    for j in range(len(hour)):
        if hour[j]==i:
            elements['list'+str(i)].append(t[j])
            

#create mean list to save the means      
meanlist=[]
errorlist=[]
     
for i in range(24):
    elements['list'+str(i)]=np.array(elements['list'+str(i)])
    meanlist.append(np.mean(elements['list'+str(i)]))
    errorlist.append(np.std(elements['list'+str(i)])/len(elements['list'+str(i)]))



"""

plt.figure()
plt.errorbar(hour24,meanlist,yerr=errorlist,fmt='--.',label='LaG to Newark')
plt.ylabel('trip time (minutes)')
plt.xlabel('Hours of the day')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22])
plt.title('Trip time from LaGuardia to Newark')
plt.axis([-1,24,40,70])
plt.legend()
plt.show()
"""

"""to plot both ways:
FIRST JL 

hour24jl=hour24
meanlistjl=meanlist
errorlistjl=errorlist

NOW LJ

hour24lj=hour24
meanlistlj=meanlist
errorlistlj=errorlist


plt.figure()

plt.errorbar(hour24jl,meanlistjl,yerr=errorlistjl,fmt='--.',label='JFK to LaG')
plt.errorbar(hour24lj,meanlistlj,yerr=errorlistlj,fmt='--.',label='LaG to JFK')
plt.errorbar(hour24jn,meanlistjn,yerr=errorlistjn,fmt='--.',label='JFK to Newark')
plt.errorbar(hour24ln,meanlistln,yerr=errorlistln,fmt='--.',label='LaG to Newark')

plt.ylabel('trip time (minutes)')
plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22])
plt.xlabel('Hours of the day')
plt.title('Trip times between New York Airports')
plt.legend()
plt.axis([-1,24,10,100])
plt.show()

"""


