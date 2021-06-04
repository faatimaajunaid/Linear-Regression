#!/usr/bin/env python
# coding: utf-8




import matplotlib.pyplot as plt
import numpy as np

iterations=1500
alpha=0.01
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
theta = np.zeros((2,1))

for j in range(0,iterations):
    theta = theta - alpha*(1/m)*np.dot(np.transpose(X),np.dot(X,theta)-Y)
    
    
for k in range(0,m):
    temp = theta[0] + theta[1]*x_list[k]
    y_outputlist.append(temp)

plt.scatter(x_list, y_list,color="red",marker="x")
plt.show()
plt.plot(x_list,y_outputlist,color="blue")
plt.show()



