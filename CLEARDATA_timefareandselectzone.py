import pandas as pd
import numpy as np
from datetime import datetime

"""NY state until JFK"""

longituderightny=-73.7353
longitudeleftny=-74.215056
latitudeupny=40.915532
latitudedownny=40.5936

# JFK
latitudeupjfk=40.6451629
latitudedownjfk=40.63548
longituderightjfk=-73.7672
longitudeleftjfk=-73.798118

#Laguardia
latitudeupl=40.778471
latitudedownl=40.765763
longituderightl=-73.858559
longitudeleftl=-73.883579

#newark
latitudeupn=40.701687
latitudedownn=40.681513
longituderightn=-74.169956
longitudeleftn=-74.194675

#wich files we'll use
year=str('2013')

#add a column with the triptime by substracting the inital time and the final time
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
    

n=12 #number of files we wanna read
n=n+1 #to fulfil the loop

#read trip_data
df1 = [pd.read_csv("/../data/social/NYC_Taxi_2010-2013/FOIL"+ year+ "/trip_data_" + str(k) + ".csv", usecols=[5,6,10,11,12,13], dtype={'pickup_datetime':datetime, 'dropoff_datetime':datetime,'pickup_longitude':np.float64, 'pickup_latitude':np.float64,'dropoff_longitude':np.float64 , 'dropoff_latitude':np.float64}, skipinitialspace=True)  for k in xrange(1,n)]
#read trip_fare
df2 = [pd.read_csv("/../data/social/NYC_Taxi_2010-2013/FOIL"+ year+ "/trip_fare_" + str(k) + ".csv", usecols=[10], dtype={'total_amount':np.float64}, skipinitialspace=True)  for k in xrange(1,n)]
#join all elements of the list
df=pd.concat(df1)
df2=pd.concat(df2)

#add column triptime
df=addtime(df)

#add total amount, you can also add tolls, tips ,...
df['total_amount']=df2['total_amount']



#select only final cordinates
df=df[df['dropoff_longitude']<longituderightl]
df=df[df['dropoff_longitude']>longitudeleftl]
df=df[df['dropoff_latitude']<latitudeupl]
df=df[df['dropoff_latitude']>latitudedownl]

#only NYarea pickups
df=df[df['pickup_longitude']<longituderightny]
df=df[df['pickup_longitude']>longitudeleftny]
df=df[df['pickup_latitude']<latitudeupny]
df=df[df['pickup_latitude']>latitudedownny]

#save new csv
df.to_csv('/home/mfuster/Desktop/datacorrected/nyto/joint2013nyl.csv')


