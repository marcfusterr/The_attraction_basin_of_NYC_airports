import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

df=pd.read_csv('/home/mfuster/Desktop/datacorrected/withfare/joint2013nyjfk.csv')

#filter imposible or not likely data
df=df[df['total_amount']<400.]
df=df[df['total_amount']>1.]
df = df.reset_index(drop=True)

"""NY state until JFK"""

longituderightny=-73.7353
longitudeleftny=-74.215056
latitudeupny=40.915532
latitudedownny=40.5936

#function that manually divides space in div and assigns its bin coordinates to a certain point
def getindex(df,x,div,xmax,xmin):
    return int(np.floor(div*(x-xmin)/(xmax-xmin)))  #normalize and multiply
    
#divisions per dimension
div=100

#create the dictionary where to store it
xydict={}

#the first two numbers are x postition, the seconds y position

#structure the dictionary in XXYY
for i in range(div):
    xind=str(i)
    for j in range(div):
        yind=str(j)
        if len(xind)==1:        #to make 1 01 and be explicit
            xind=str(0)+xind
        if len(yind)==1:
            yind=str(0)+yind        
        xydict[xind+yind]=[]

#fulfil dict
for i in range(len(df)):
        xind=str(getindex(df,df['pickup_longitude'][i],div,longitudeleftny,longituderightny))
        yind=str(getindex(df,df['pickup_latitude'][i],div,latitudedownny,latitudeupny))
        if len(xind)==1:
            xind=str(0)+xind
        if len(yind)==1:
            yind=str(0)+yind
        xydict[xind+yind].append(i)
        

costavarage=[] #createtime list first two are x div and second two are y div
for k in range(len(xydict)):
    
    kindex=str(k)  #better work with strings so that you don't modify the k
    
    #make them '0000'
    if len(kindex)==1:
        kindex=str(000)+kindex
    if len(kindex)==2:
        kindex=str(00)+kindex
    if len(kindex)==3:
        kindex=str(0)+kindex
    #create aux array to make avarages
    #each loop it desappears    
    costarray=[]
    
    for i in range(len(xydict[kindex])):

        costarray.append(df['total_amount'][xydict[kindex][i]])#appends the totalamount of all points in the bin
    #empty columns and less than 4 datapoints make them 0
    #we need at least 3 points to make statistics    
    if len(costarray)<4:
        costavarage.append(0.)
    else:
        costavarage.append(np.mean(costarray)) #make the mean of 
        
#create matrix    
costmatrix= [[0 for x in range(div)] for y in range(div)] 
#fill the matrix
for i in range(div):
    for j in range(div):
        costmatrix[i][j]=costavarage[j*div+i]

#the matrix exits fliped, put it naturally
costmatrix=np.fliplr(costmatrix)
costmatrix=np.flipud(costmatrix)

#to save the matrix uncomment both below

#costmatrix=np.matrix(costmatrix)
#costmatrix.dump("/home/mfuster/Desktop/datacorrected/matrix/avcost1.dat") #savematrix


#put cercle on JFK
jfklat=40.644942
jfklon=-73.784533
xjfk=np.floor((jfklon-longitudeleftny)/(longituderightny-longitudeleftny)*div)
yjfk=np.floor((jfklat-latitudedownny)/(latitudeupny-latitudedownny)*div)



my_cmap = plt.cm.get_cmap('YlOrRd')
my_cmap.set_under('w',alpha = 0.0) #set lower color white to a better visualization

plt.figure()
plt.pcolor(costmatrix,cmap=my_cmap,vmin=1.)
plt.title('Trip Cost to JFK')
cb=plt.colorbar()
cb.set_label('Dolars')
plt.gca().set_axis_off()
circle=plt.Circle((xjfk,yjfk),1.,color='blue')
plt.gcf().gca().add_artist(circle)
plt.savefig("/home/mfuster/Desktop/photos/tojfk/avaragecost1",bbox_inches='tight')


