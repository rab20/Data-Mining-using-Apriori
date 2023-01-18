#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori
import copy


# In[15]:


# Read the input excel sheet containing 7500 transactions
mba_dataset = pd.read_excel('Dataset.xlsx',header=None)


# In[16]:


# Create an empty list
mba_dataset_list = []


# In[17]:


# Converting the input data into a list so that Apriori function can be used
for i in range(0, 7501):
    mba_dataset_list.append([str(mba_dataset.values[i,j]) for j in range(0, 20)])   


# In[18]:


# Applying Apriosi algorithm on the input data
association_rules = apriori(mba_dataset_list, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)


# In[19]:


# Converting the rules into a list
association_results = list(association_rules)


# In[20]:


# Printing the total number of rules generated using the algorithm
print("Total number of rules generated are {}".format(len(association_results)))


# In[21]:


result_dict = {}
result_int_dict = {}
result_dict_list = []


# In[22]:


# Creating the results as a dictionary
for item in association_results:
    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    result_dict["Rule"] = str(items[0] + " -> " + items[1])
    
    #second index of the inner list
    result_dict["Support"] = str(item[1])

    #third index of the list located at 0th
    #of the third index of the inner list

    result_dict["Confidence"] = str(item[2][0][2])
    result_dict["Lift"] = str(item[2][0][3])
    
    result_int_dict = copy.deepcopy(result_dict)
    result_dict_list.append(result_int_dict)


# In[23]:


# Creating a dataframe from the dictionary
df = pd.DataFrame(result_dict_list, columns =['Rule', 'Support', 'Confidence', 'Lift'])


# In[24]:


df


# In[25]:


# Write the generated rulesets into an excel - Output.xlsx
df.to_excel("Output.xlsx")


# In[ ]:




