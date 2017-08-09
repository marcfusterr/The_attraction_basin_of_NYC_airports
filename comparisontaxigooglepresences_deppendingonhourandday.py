import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import datetime
from datetime import datetime
import glob


"""FROM TAXI"""
df1=pd.read_csv('/home/mfuster/Desktop/datacorrected/nyto/2013nyjwithhour.csv',skipinitialspace=True)
df2=pd.read_csv('/home/mfuster/Desktop/datacorrected/tony/2013jnywithhour.csv',skipinitialspace=True)
#we create a dictionaire divided by the weekday
mydict1={}  #arrivals
mydict2={}  #departures

#create dictionaries separated by the weekday
for i in range(7):
    mydict1['weekday'+str(i)]=df1[df1['weekday']==i]
    mydict2['weekday'+str(i)]=df2[df2['weekday']==i]


countsdict1={}
countsdict2={}

#for the separated weekdays count how many per hour
for i in range(7):
    countsdict1['weekday'+str(i)]=mydict1['weekday'+str(i)]['hour'].value_counts()
    countsdict2['weekday'+str(i)]=mydict2['weekday'+str(i)]['hour'].value_counts()
    
for i in range(7):
    countsdict1['weekday'+str(i)]=countsdict1['weekday'+str(i)].sort_index()
    countsdict2['weekday'+str(i)]=countsdict2['weekday'+str(i)].sort_index()
    
    #correct data since on google it is not centered
    #0 of google is 4 real
    
#first convert it to np array

for i in range(7):
    countsdict1['weekday'+str(i)]=countsdict1['weekday'+str(i)].as_matrix()
    countsdict2['weekday'+str(i)]=countsdict2['weekday'+str(i)].as_matrix()    

#roll numbers, put the last 4 in first positions roll(,4)
for i in range(7):
    countsdict1['weekday'+str(i)]=np.roll(countsdict1['weekday'+str(i)],4)
    countsdict2['weekday'+str(i)]=np.roll(countsdict2['weekday'+str(i)],4) 

    
substractdict={}
for i in range(7):
    substractdict['weekday'+str(i)]=countsdict1['weekday'+str(i)]-countsdict2['weekday'+str(i)]


#try to plot it all    
t = np.arange(24*7)/24.
nytojfk=[]
for i in range(7):
    for j in range(24):
        nytojfk.append(countsdict1['weekday'+str(i)][j])
        

              
"""FROM TXT"""              
             
paths = glob.glob('/home/mfuster/Desktop/datacorrected/peolegoogle/JFK/*')

unsort = []
for path in paths: #for all 7 files
    with open(path) as inFile:
        s = inFile.read()
        
    if len(unsort) != 2: #one of those has a different format
        p =  s.split("height: ")
   # else:
    #    p =  s.split("height:")
    
    unsort.append([int(cc[:2]) for cc in p[1:]]) #only the first two characters of all lines but the first
    

#Make the week in order (from tuesday to monday because my other data are like this)
ind =[5,4,1,0,6,3,2] #WRITE PATH TO SHELL TO KNOW THE ORDER.
days = ['Sunday', 'Saturday', 'Wednesday', 'Tuesday','Monday', 'Friday', 'Thursday']
week = []
for i in range(7):
    week+= unsort[ind[i]]
#correct the 4 hour difference, 
#put the last 4 in first positions roll(,4)
week=np.array(week)
week=np.roll(week,6)   

"""plots"""

plt.figure()  
plt.plot(t,np.array(nytojfk)/160+17,label='taxi data')
plt.plot(t,week,label='google data')
plt.title('ny to jfk')
plt.xlabel('Days of the week')
plt.ylabel('Arbitrary units')
plt.xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5], ['Mon', 'Tue', 'Wed','Thu','Fri','Sat','Sun'], size = 'small', color = 'k') 
plt.legend(loc='upper left')