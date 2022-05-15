#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


data = pd.read_csv("data/AAPL.csv", header = 0)
data.head(10)


# In[3]:


type(data)


# In[8]:


data.plot()


# In[13]:


data.dtypes


# In[ ]:




