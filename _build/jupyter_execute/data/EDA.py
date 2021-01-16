#!/usr/bin/env python
# coding: utf-8

# # Exploratory data analysis 
# 

# Last updated: 2020-12-22

# ## Background
# 

# > Flanker Data
# We'll be working with data from a similar flanker experiment as we used in Assignment 2. However, in Assignment 2 we gave you a "sanitized" version of the data, where we had done a bit of clean-up to extract just the information we wanted you to work with. In this assignment you'll get experience starting with the raw data and extracting the necessary information yourself.
# 
# --PSYO 3505 Fall 2019 Assignment 2 cell1

# ## Read file and check it

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# First of all we need input and examine the data 

# In[2]:


subjects = ['001_2015_05_22_11_30',
            '002_2015_05_25_14_36',
            '003_2015_05_28_14_09'
           ]

in_file = subjects[0]+'/'+subjects[0]+'_data.txt'

#input to data_frame
df = pd.read_csv(in_file)


# In[3]:


df.head(5)


# looks like not very well, we need add escape character. Typically, I prefer read csv file directly and then check the head.

# In[4]:


df = pd.read_csv(in_file,sep = '\t')
df


# look at the head and tail again 
# 

# In[5]:


df.head(5)


# In[6]:


df.tail(5)


# Then we check have missing value 

# In[7]:


print(pd.isna(df).sum())


# ## Data cleaning

# Obviously, we need to remove missing data by appling 
# ```
# .dropna() method
# ```

# In[8]:


df = df.dropna()
print(pd.isna(df).sum())


# This experiment has ‘practice’, the main idea is giving participants a chance to figure out the experiment. But we do not need it in our EDA. Not all experiments have ‘practice’ . 

# value = df['block']
# print(value.unique())

# In[9]:


df = df[df.block!='practice']
value = df['block']
print(value.unique())


# Then we found ‘rt’ column is not milliseconds and need to convert

# In[10]:


df['rt']


# In[11]:


df['rt'] = df['rt']*1000
print(df['rt'])


# ‘rt’ is our interested variable, but In most behavioural studies, RTs are not normally distributed, so we need to Examining the RT distribution

# In[12]:


df['rt'].describe()


# plot a histogram of RTs

# In[13]:


df['rt'].plot(kind='hist')

# add a solid line at the median and dashed lines at the 25th and 75th percentiles (done for you)
plt.axvline(df['rt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['rt'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['rt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

# Rememebr to use plt.show() to see your plots (often they show anyway, but with some garbagy text at the top)
plt.show()


# ## Analyzing relationships between variables

# According to above figure, the histogram look not follow normal distribution, Looks like right skewed. Because the data sets have low ‘high value
# <br> check the cdf

# In[14]:


df['rt'].plot(kind = 'hist',cumulative = True, density =True)
# add a dashed oragne line at the median
plt.axvline(df['rt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['rt'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['rt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

plt.show()


# How should we do in this situation. The course tells me :
# <br>
# >While the skew in the RT data makes sense, for the reasons described above, it's problematic when running statistics on the data. This is because many conventional statistical tests, like t-tests and ANOVAs, assume that the data are normally distributed. Using skewed data can cause unreliable results.
# <br>
# <br>
# For this reason, many researchers apply some transformation to RTs to make their distribution more normal (statistically normal, that is). A common one is to take the logarithm of the RT values: log(RT)log(RT); another is to take the inverse: 1/RT.
# 
# 
# ---PSYO 3505 Fall 2019 Assignment 2 cell40
# 

# So, for log(RT)

# In[15]:


# log-transform the rt data (done for you) 
df['logrt'] = np.log(df['rt'])

# put your plotting code here
# YOUR CODE HERE
df['logrt'].plot(kind='hist')

# add a solid line at the median and dashed lines at the 25th and 75th percentiles (done for you)
plt.axvline(df['logrt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['logrt'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['logrt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

# Rememebr to use plt.show() to see your plots (often they show anyway, but with some garbagy text at the top)
plt.show()


# inverse: $1/RT$

# In[16]:


df['invrt'] = 1/(df['rt'])

df['invrt'].plot(kind='hist')
# add a solid line at the median and dashed lines at the 25th and 75th percentiles (done for you)
plt.axvline(df['invrt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['invrt'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['invrt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

# Rememebr to use plt.show() to see your plots (often they show anyway, but with some garbagy text at the top)
plt.show()


# After that, we want to explore the data will be on errors and reaction times (RTs).
# >Recall that these data are from a "flanker" experiment in which participants had to respond with a left or right button press, depending on whether the target (centre) arrow pointed left or right. The target arrow was flanked with two arrows on either side that were either congruent (pointed in same direction) or incongruent (opposite direction).
# 
# ---PSYO 3505 Fall 2019 Assignment 2 cell48
# 
# ```{tip} You can found more information about flanker experiment in this article 'Flanker and Simon effects interact at the response selection stage'
# ```

# In[17]:


rt_mean = df.groupby(by = 'flankers')[['rt','error']].agg('mean')
rt_mean = rt_mean.drop('neutral')
rt_mean


# Generate a table for accuracy (the error column).

# In[18]:


correct = df.groupby(by = 'flankers')[['error']].agg('sum')
correct.columns = ['Correct']
correct = correct.drop('neutral')
correct


#  showing the accuracy rate

# In[19]:


total= df.groupby(by = 'flankers')[['error']].agg('count')
correct = df.groupby(by = 'flankers')[['error']].agg('sum')
number = correct[:2]/total[:2]
number.columns = ['Accuracy']
number


# ## Visualization

# Plot box plots of the log-transformed RT data (logrt) for each flanker conditio

# In[20]:


boxplot1 = df.loc[df['flankers']=='congruent','logrt'].plot(kind = 'box',title = 'Congruent')
plt.show()
boxplot2 = df.loc[df['flankers']=='incongruent','logrt'].plot(kind = 'box',title = 'Incongruent')
plt.show()


# ## Interpretation

#  Basis of EDA, I can say incongruent flankers would lead to slower and less accurate responses. according to the participant results, the congruent condition has 100% accuracy and 452.60 (mean) response time. Incongruent condition has 85% accuracy and 466.05 (mean) response time.

# So far, we end EDA methods (basic). 
# <br>
# <br>
# Through this assignment, I learned the basic steps of data analysis. Especially,EDA methods:
# <br> Read files
# <br> Data cleaning
# <br> Analyzing relationships between variables
# <br> Visualization
# <br> Interpretation

# ## References
# 
# [1] [NESC 3505 Neural Data Science, at Dalhousie University. Textbook](https://dalpsychneuro.github.io/NESC_3505_textbook/intro.html)
# <br>
# [2] NESC 3505 Neural Data Science, at Dalhousie University. Assignment 3
# <br>
# [3] [An Extensive Step by Step Guide to Exploratory Data Analysis](https://towardsdatascience.com/an-extensive-guide-to-exploratory-data-analysis-ddd99a03199e)

# 
# <font color = red >This Demo and the attached files from course PSYO/NESC 3505 Neural Data Science, at Dalhousie University. You should not disseminate, distribute or copy. </font>
# <br><font color = red >I am NOT post inappropriate or copyrighted content, advertise or promote outside products or organizations </font>
# <br>© Copyright 2020.PSYO/NESC 3505 FAll 2020 https://dalpsychneuro.github.io/NESC_3505_textbook/intro.html
# <br>**For demonstration purposes only**

# In[ ]:




