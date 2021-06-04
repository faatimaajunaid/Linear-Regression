#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import numpy as np

iterations=50
alpha=0.3
x1_list=[]
x2_list=[]
y_list=[]
y_outputlist=[]
J_x=[]
J_y=[]
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

mean1 = np.mean(x1_list)
std1 = np.std(x1_list)
x1_list_norm = (x1_list - mean1)/std1

mean2 = np.mean(x2_list)
std2 = np.std(x2_list)
x2_list_norm = (x2_list - mean2)/std2 
    
m=len(x1_list)
X = np.column_stack((np.ones(m),x1_list_norm,x2_list_norm))
Y = np.transpose(np.column_stack((y_list)))
theta = np.zeros((3,1))



for j in range(0,iterations):
    
   
    error = 1/(2*m) * np.sum((X.dot(theta) - Y)**2)
    J_y.append(error)
    J_x.append(j)
    
    theta = theta - alpha*(1/m)*np.dot(np.transpose(X),np.dot(X,theta)-Y)
    
plt.plot(J_x,J_y,color="blue")
plt.show()


# In[2]:


theta


# In[3]:


x1_list_norm


# In[4]:


x2_list_norm


# In[6]:


theta


# In[ ]:




