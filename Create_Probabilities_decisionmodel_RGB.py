import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#load matrix of data (thousands of times faster than load all the csv)
avt1=np.load('/home/mfuster/Desktop/datacorrected/matrix/avtime1.dat') #JFK
avt2=np.load('/home/mfuster/Desktop/datacorrected/matrix/avtime2.dat') #LaG
avt3=np.load('/home/mfuster/Desktop/datacorrected/matrix/avtime3.dat') #New

avc1=np.load('/home/mfuster/Desktop/datacorrected/matrix/avcost1.dat') #JFK
avc2=np.load('/home/mfuster/Desktop/datacorrected/matrix/avcost2.dat') #LaG
avc3=np.load('/home/mfuster/Desktop/datacorrected/matrix/avcost3.dat') #New


e=2.71828

#create matrixes of probability
p1=np.zeros((100,100))
p2=np.zeros((100,100))
p3=np.zeros((100,100))
decision=np.zeros((100,100))

#parameters
costperminute=0.35
a=0.042

#create probability
for y in range(100):
    for x in range(100):
        
        
        v1=-a*(costperminute*avt1[x,y]+avc1[x,y])
        v2=-a*(costperminute*avt2[x,y]+avc2[x,y])
        v3=-a*(costperminute*avt3[x,y]+avc3[x,y])
        print(v1,v2,v3)

        if v1 == 0. and v2==0. and v3==0. :
        #if all of them are 0 put decision and P() =0    

            decision[x,y]=0.
            p1[x,y]=0.
            p2[x,y]=0.
            p3[x,y]=0.

        else:
            norm=e**v1+e**v2+e**v3
            print(v1,v2,v3)        
            p1[x,y]=e**v1/norm
            p2[x,y]=e**v2/norm
            p3[x,y]=e**v3/norm
            



#create an matrix of space in each element an rgb (a,b,c)
p=[[(p1[x,y],p2[x,y],p3[x,y]) for y in range(100)] for x in range(100)]

"""create cercles in airports"""
div=100.
longituderightny=-73.7353
longitudeleftny=-74.215056
latitudeupny=40.915532
latitudedownny=40.5936

jfklat=40.644942
jfklon=-73.784533
xjfk=np.floor((jfklon-longitudeleftny)/(longituderightny-longitudeleftny)*div)
yjfk=np.floor((jfklat-latitudedownny)/(latitudeupny-latitudedownny)*div)

llat=40.77375
llon=-73.872524
xl=np.floor((llon-longitudeleftny)/(longituderightny-longitudeleftny)*div)
yl=np.floor((llat-latitudedownny)/(latitudeupny-latitudedownny)*div)

nlat=40.690695
nlon=-74.17752
xn=np.floor((nlon-longitudeleftny)/(longituderightny-longitudeleftny)*div)
yn=np.floor((nlat-latitudedownny)/(latitudeupny-latitudedownny)*div)
"""" """

p=np.flipud(p) #the matrix is inverted


#make lowest white
for y in range(100):
    for x in range(100):
        if p[x][y][0]==0. and p[x][y][1]==0. and p[x][y][2]==0.:
            p[x][y]=[1.,1.,1.]
        
plt.figure()        
plt.imshow(p)
plt.title('Airport decision with '+str(costperminute)+' USD per minute')
circle1=plt.Circle((xjfk,100-yjfk),1.,color='black')
circle2=plt.Circle((xl,100-yl),1.,color='black')
circle3=plt.Circle((xn,100-yn),1.,color='black')
#we create hipersmall cercles that wont be seen to put the legends

plt.gcf().gca().add_artist(circle1)
plt.gcf().gca().add_artist(circle2)
plt.gcf().gca().add_artist(circle3)

plt.gcf().gca().text(5, 5, 'Red: JFK, Green:LaG, Blue:NEW', bbox={'facecolor': 'white', 'pad': 10})
plt.savefig('/home/mfuster/Desktop/photos/choice decision/definitivenotsavedmanually.png')
plt.gca().set_axis_off()  #to store it without axis save it manually.

plt.show()

