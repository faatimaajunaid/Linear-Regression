#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import numpy as np


x_list=[]
y_list=[]
y_outputlist=[]
myfile = open("ex1data1.txt","r")
contents = myfile.readlines()
myfile.close()

for line in contents:
    x,y = line.split(",")
    x_list.append(float(x))
    y_list.append(float(y))

x_list=np.array(x_list)
y_list=np.array(y_list)


m=len(x_list)
X = np.column_stack((np.ones(m),x_list))
Y = np.transpose(np.column_stack((y_list)))
T = np.matmul(np.linalg.pinv(X),Y)

for k in range(0,m):
    temp = T[0] + T[1]*x_list[k]
    y_outputlist.append(temp) 

plt.scatter(x_list, y_list,color="red",marker="x")
plt.show()
plt.plot(x_list,y_outputlist,color="blue")
plt.show()



