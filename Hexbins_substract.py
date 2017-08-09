
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#load csv
df=pd.read_csv('/home/mfuster/Desktop/datacorrected/1Mrandom.csv',skipinitialspace=True)
x1=df['pickup_longitude'].values.tolist()
y1=df['pickup_latitude'].values.tolist()

#df=pd.read_csv('/home/mfuster/Desktop/datacorrected/JFK2013jm.csv',skipinitialspace=True)
x2=df['dropoff_longitude'].values.tolist()
y2=df['dropoff_latitude'].values.tolist()

#get arrays to plot
x1=np.array(x1)
x2=np.array(x2)

y1=np.array(y1)
y2=np.array(y2)

divisions=1100
axis=[-74.1, -73.85, 40.675, 40.825]

#only pickups
plt.figure()
h1=plt.hexbin(x1, y1, extent=axis, gridsize=divisions, cmap='viridis')   #there isnt the log
plt.axis(axis)
plt.title("Pickups")
cb = plt.colorbar()
cb.set_label('N')
#get the data to later make the difference
data1=h1.get_array()
plt.show()

#only dropoffs
plt.figure()
h2=plt.hexbin(x2, y2, extent=axis, gridsize=divisions,cmap='viridis')   #there isnt the log
plt.axis(axis)
plt.title("Dropoffs")
cb = plt.colorbar()
cb.set_label('N')

data2=h2.get_array()
plt.show()

#scatter the difference
plt.figure()
h3=plt.hexbin(x1,y1, extent=axis, gridsize=divisions, bins='log', vmin=-3., vmax=3.,  cmap=plt.cm.RdBu_r)  #it is much better to have 0 white
h3.set_array(h1.get_array()-h2.get_array())
plt.title("Pickups-Dropoffs")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis(axis)
cb = plt.colorbar()
cb.set_label('log10(N)')
plt.show()

