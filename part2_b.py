#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import numpy as np

x1_list=[]
x2_list=[]
y_list=[]
myfile = open("ex1data2.txt","r")
contents = myfile.readlines()
myfile.close()

for line in contents:
    x1,x2,y = line.split(",")
    x1_list.append(float(x1))
    x2_list.append(float(x2))
    y_list.append(float(y))

x1_list=np.array(x1_list)
x2_list=np.array(x2_list)
y_list=np.array(y_list)


m=len(x1_list)
X = np.column_stack((np.ones(m),x1_list,x2_list))
Y = np.transpose(np.column_stack((y_list)))
T = np.matmul(np.linalg.pinv(X),Y)

predicted_price = T[0] + 1650*T[1] + 3*T[2]
print(predicted_price)

