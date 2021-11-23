#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[11]:


a = int(input('Enter a value for a: '))
b = int(input('Enter a value for b: '))
c = int(input('Enter a value for c: '))


# In[12]:


def quadSol(a,b,c):
     #d is for Discriminant
  d = (b**2)-(4*a*c)
 
  if a == 0:
    exit('a cannot equal zero !') 
    #complex
  elif d < 0: 
    i1 = math.sqrt(-d)/(2*a)
    i2 = math.sqrt(-d)/(2*a)
    print("Complex roots:")
    print(- b / (2*a), " + i",i1)
    print(- b / (2*a), " - i",i2)
    #real root
  elif d == 0: 
    x=(-b)/(2*a) 
    print('One real root:',x) 
      #two real and different
  else: 
    x1 = (-b+math.sqrt(d))/(2*a) 
    x2 = (-b-math.sqrt(d))/(2*a) 
    print('Two different real roots:',x1, 'and',x2) 
    
quadSol(a,b,c)

