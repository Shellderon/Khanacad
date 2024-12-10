import numpy as np 
import matplotlib.pyplot as plt
data=[-5,-3,-2,-1,0,0.3,0.1,0.5,1,2,3,5]




n,bins,patches= plt.hist(data,edgecolor='black',bins=7,color='white')


patches[-3].set_facecolor('red')



patches[-4].set_facecolor('black')



plt.xticks([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])


plt.title("penis")
plt.xlabel("length")
plt.ylabel("height")


plt.show()