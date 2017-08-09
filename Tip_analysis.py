import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

df=pd.read_csv('/home/mfuster/Desktop/datacorrected/1Mrandomtip.csv',skipinitialspace=True)

#gets the percentile of a over a quantity b
def topercentile(a,b):
    return 100*(1+(a-b)/b)
    

bins=100
#ranges to plot
rangetip=[-0.25,39.75]
rangetotal=[40.25,60.25]
rangepercentile=[-0.25,39.75]
prec=0.5

#get arrays we'll use
total=np.array(df['total_amount'])
tip=np.array(df['tip_amount'])
fareminustip=total-tip

tippercentile=topercentile(tip,fareminustip)

#dolars tip plot
plt.figure()
plt.title('Tip')
weights = np.ones_like(tip)/float(len(tip))
plt.hist(100*tip,(rangetip[1]-rangetip[0])/prec, weights=weights,range=rangetip)
plt.axis([0.,20.,0,0.3])
plt.xlabel('USD')
plt.ylabel('Probability')


#percentile plot    
plt.figure()
plt.title('Tip percentile')
weights = np.ones_like(tippercentile)/float(len(tip))
plt.hist(tippercentile,(rangepercentile[1]-rangepercentile[0])/(1.1*prec), weights=100*weights,range=rangepercentile)
plt.axis([0.,35.,0,30])
#plt.axvline(topercentile(5), color='y', linestyle='dashed', linewidth=2,label='5 USD')
#plt.axvline(topercentile(10), color='c', linestyle='dashed', linewidth=2,label='10 USD')
#plt.axvline(topercentile(15), color='g', linestyle='dashed', linewidth=2,label='15 USD')
#plt.axvline(topercentile(20), color='k', linestyle='dashed', linewidth=2,label='20 USD')
#plt.axvline(topercentile(12.7), color='r',linestyle='dashed', linewidth=2,label='Total exactly 70 USD')

plt.xlabel(r'Percentile over total $\%$')
plt.ylabel(r'Probability $\%$')
#plt.legend(loc=2)




