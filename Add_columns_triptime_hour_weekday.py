import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import datetime
from datetime import datetime

df=pd.read_csv('/home/mfuster/Desktop/datacorrected/nyto/2013nyj.csv',skipinitialspace=True)

#this function adds a column with the triptime
def addtime(df):
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
    #addcolumn
    df['triptime']=t
    return df
    
    
df=addtime(df)
#df.to_csv('/home/mfuster/Desktop/datacorrected/nyto/2013nyjwithtime.csv')

#this one adds the hour and the weekday.
def add_weekdayandhour(path):
    #reading
    df=pd.read_csv(path,skipinitialspace=True)

    t1=df['dropoff_datetime'].values.tolist() #who arrive
    
    #convert to datetime format and add weekdaycolumn   
    weekdaylist=[]
    hourlist=[]
    for i in range(len(t1)):
        t1[i] = datetime.strptime(t1[i], '%Y-%m-%d %H:%M:%S')
        weekdaylist.append(t1[i].weekday())
        hourlist.append(t1[i].hour)

    #add new column
    df['hour']=hourlist
    df['weekday']=weekdaylist
    return df
