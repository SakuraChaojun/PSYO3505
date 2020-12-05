#!/usr/bin/env python
# coding: utf-8

# # Assignment 3
# 
# ## NESC 3505
# ---
# ## Instructions
# Write code to answer each of the questions below. Remember to *replace* the lines:
#     raise NotImplementedError()
# 
# with your own code.
# 
# In a few cases, the questions ask for written answers rather than code. Those are Markdown cells.
# 
# We will collect your notebooks on the due date/time, so there is nothing specific you need to do to submit your assignment - as long as it is on time. If you want your assignment to be counted as late (with 2%/hour penalty), you must send us (Aaron and Danny) a message on Teams when you are ready for it to be counted as submitted. Be sure not to make changes after you make that request; any subsequent changes will be ignored (based on CoCalc's version tracking/Time Travel).
# 
# ---
# 
# ## Flanker Data
# 
# We'll be working with data from a similar flanker experiment as we used in Assignment 2. However, in Assignment 2 we gave you a "sanitized" version of the data, where we had done a bit of clean-up to extract just the information we wanted you to work with. In this assignment you'll get experience starting with the raw data and extracting the necessary information yourself.
# 
# We're going to import the data as a pandas DataFrame, so your first step is to import pandas with the abbreviation `pd`. Also import NumPy, as `np`, and `matplotlib.pyplot` as `plt`.

# In[1]:


# YOUR CODE HERE Question 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# this extra command ensures that you can see all the columns in a DataFrame, when there are many
pd.set_option('display.max_columns', None)


# ### Read and examine a data file
# 
# In working with a new data set, the first thing you should do is load the first data file, and see what it looks like. Does it have a header? If so, what are the column names? Do the column names seem clear in indicating what they contain? Are there any issues like missing data?
# 
# Your first challenge is that the data file you want is in a subdirectory, so you need to tell Python where to find it. I coding-world, the set of directories/sub-directories that a file is in is called it's **path**, and directory names are separated by `/` characters. Since the first subject ID is `001_2015_05_22_11_30` and the data file we want is in that, with the name `[ID]_data.txt`, the path to this file is: 
# `001_2015_05_22_11_30/001_2015_05_22_11_30_data.txt`
# 
# So, to load in the file you need to create a string like the above. Of course, you could type that in (hard-code it), but that wouldn't be very pythonic, nor would it be useful when you want to read in more subjects' data files. So the better way is to build the string for the path up from variables. Try to do this in the cell below; don't worry about loading the file yet, just create a variable called `in_file` that contains the string above, built from slicing the `subjects` variable (selecting the first entry in the list) and using the `+` operator to combine variables and strings together.

# In[2]:


subjects = ['001_2015_05_22_11_30',
            '002_2015_05_25_14_36',
            '003_2015_05_28_14_09'
           ]


# In[3]:


# YOUR CODE HERE Question 2
in_file = subjects[0]+'/'+subjects[0]+'_data.txt'

# The print command below will help you confirm you have the string right, 
# before you try to use it to read the data file
print(in_file)


# Now read the first data file into a pandas DataFrame called `df` by using `pd.read_csv()` with the `in_file` variable as the input:

# In[4]:


# YOUR CODE HERE Question 3
df = pd.read_csv(in_file)


# Look at the head of the DataFrame to see what you loaded:

# In[5]:


# YOUR CODE HERE Question 4
print(df.head())


# Well, that doesn't look right, does it? We'll need to use some additional arguments to `pd.read_csv()` in order to get it right.
# 
# The issue is that our input file is a text file, with the extension `.txt`. The function `pd.read_csv()` assumes that the input you give it is a CSV (comma-separated values) file, which uses commas to separate the entries in each row that should be in separate columns. However, our text files use tabs, rather than commas, to separate the columns. We can tell this because in the output above, the lines all have a bunch of "`\t`"s in them. The string `\t` is a special code used in Unix/linux systems and many programming languages to indicate a tab. The `\` is a special **escape character** that tells Python not to interpret the next character literally as a string, but as a code.
# 
# Take a look at [the API for pandas.read_csv()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) to get insight on how to tell pandas to use commas as the column separators. You'll see the `sep=` option, along with a note that pandas uses a comma by default. To override this default, we need to use `sep='\t'`. In the cell below, copy and paste your code from above to read the file, but add the `sep` argument.

# In[6]:


# YOUR CODE HERE Question 5
df = pd.read_csv(in_file,sep = '\t')


# Look at the head of the DataFrame to see the results:

# In[7]:


# YOUR CODE HERE Question 6
print(df.head())


# OK, that should look much better! 
# 
# You'll notice there are a lot more columns in this data file, than in the version we gave you last time. Again, this is because before you got the "sanitized" version whereas now you get the "raw" version. We'll work with some of these extra columns in this assignment, and others will just be ignored. It's not uncommon to have columns (variables) in a data set that are not of interest for a specific analysis you're running.)
# 
# There is one issue with this data file that is evident from looking at the first few lines: there are missing values (`NaN`) in the `rt`, `response`, and `error` columns. This is something we'll deal with below.
# 
# You'll also see that there is a `block` column, which has a value of `practice` for all of the first 10 rows, and a `trial` column that increases sequentially. Many experiments are composed of a series of blocks, which are sets of trials. Blocks might simply be a way of setting up the experiment so that there are breaks (e.g., a break at the end of every block of trials), or the blocks may represent different experimental conditions. At any rate, you can infer from these columns that the experiment that generated these data was organized into blocks and trials. You can also likely guess that after the `practice` block are additional blocks, probably not called "practice". You can confirm this by calling the head of the DataFrame again, but this time showing (spoiler alert) 35 rows.

# In[8]:


# YOUR CODE HERE Question 7
print(df.head(35))


# Another way to look at what might change over the course of experiment (like blocks) is to view the tail of the DataFrame. Do this in the cell below, to view the last 25 trials in the DataFrame.

# In[9]:


# YOUR CODE HERE Question 8
print(df.tail(25))


# ### Missing Values?
# 
# Since the first lines of a data file obviously don't represent its entirety, it would be good to get a summary of how many missing values there are in the data set. You can do this with `pd.isna()` (or the equivalent `pd.isnull()`), which will output `True` or `False` for every cell of the DataFrame. That alone is not any more useful than looking at the original data, however you can *chain* that command with the `.sum()` method to get the total number of `True` values in each column (remember that in Python, `true` = `1` and `False` = `0`). 
# 
# Do this below: run `isna()` on `df` and chain it with the `.sum()` method.

# In[10]:


# YOUR CODE HERE Question 9
print(pd.isna(df).sum())


# ### Data Cleaning
# 
# The next things we need to is decide how to deal with the `NaN`s. It turns out these are just trials on which the participant didn't make a button press response. We have (at least) three options:
# 1. Leave these as-is.
# 2. Remove all rows with missing data
# 3. Replace (impute) the missing values with actual values.
# 
# Option 3 was covered in the DataCamp lessons. Imputation of missing data is sometimes done in psychology and neuroscience studies, especially if we have lots of variables, and only one data point per subject (e.g., a score on a standardized test completed by each subject). Usually the reason for imputing data is that statistical methods such as ANOVAs do not allow for missing data, so without imputation we might have to discard a subject's data, even if they are only missing data from one test among many that were administered.
# 
# However, in the current case, it doesn't make sense to "make up" a reaction time on a trial when a participant didn't make a response at all. So we could remove those trials entirely. On the other hand, we might want to report how many trials, on average, our participants failed to respond to, or we might want to treat those the same as errors. 
# 
# Although missing data is problematic for things like ANOVAs, it is not an issue for EDA summary statistics in pandas. Indeed, [pandas' documentation explicitly states](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#calculations-with-missing-data) that missing data is ignored in computing values such as the mean and standard deviation.
# 
# So, we could probably safely keep the NaNs in the data. On the other hand, you learned in *Manipulating DataFrames with pandas* how to use the `.dropna()` method. And as they say, "when you have a hammer, everything looks like a nail". So use this method to drop any rows containing any `NaN` values:

# In[11]:


# YOUR CODE HERE Question 10
df = df.dropna()
print(pd.isna(df).sum())


# ### Remove practice trials
# 
# You can use the pandas `unique()` method to see what the other possible values of `block` are in this dataset. Do that in the cell below:

# In[12]:


# YOUR CODE HERE Question 11
value = df['block']
print(value.unique())


# The  point of practice is to give participants a chance to figure out the experiment (which is a bit complicated in this case), and make some errors, ask questions, etc., *before* running the experiment where we hope their data will be a valid reflection of their performance. So we should discard all the practice trials prior to doing EDA. 
# 
# The simplest way to remove all the rows from the practice block is actually to simply keep all the values that *don't* have the value of 'practice' in the `block` column. Copy and paste the command below into the next cell, and add the Python "not equals" operator in the appropriate place to do this.
# 
#     df = df[df.block  'practice']

# In[13]:


# YOUR CODE HERE Question 12
df = df[df.block!='practice']


# Confirm that there are no practice trials left in `df`

# In[14]:


# YOUR CODE HERE Question 13
value = df['block']
print(value.unique())


# ### Reaction Times
# 
# First off, convert the `rt` column to milliseconds

# In[15]:


# YOUR CODE HERE Question 14
df['rt'] = df['rt']*1000
print(df['rt'])


# #### Examining the RT distribution
# 
# In most behavioural studies, RTs are not normally distributed. Recall that a normal distribution has a mean and a standard deviation, and no *skew*. That is to say, there are typically an equal number and distribution of values above and below the mean. RTs tend to be skewed, because there are fundamental limits on how fast a human can process information and make a motor response, which sets a lower limit on RTs. However, the upper limit (slow RTs) has much more range. In some experiments, participants can wait as long as they want to make a response. In other experiments, there is a limited response window, but still there tends to be a wider tail on the right side of the distribution, when you plot it. 
# 
# Let's see if our RT data is skewed. First, use the pandas method `.describe()` to display descriptive stats for the RT data:

# In[16]:


# YOUR CODE HERE Question 15
df['rt'].describe()


# Next plot a histogram of RTs, using the pandas .plot() method:

# In[17]:


# put your plotting code here Question 16
# YOUR CODE HERE
df['rt'].plot(kind='hist')

# add a solid line at the median and dashed lines at the 25th and 75th percentiles (done for you)
plt.axvline(df['rt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['rt'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['rt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

# Rememebr to use plt.show() to see your plots (often they show anyway, but with some garbagy text at the top)
plt.show()


# Does the histogram look normally distributed, or skewed? Explain.

# <font color = '#AA5500'> # YOUR ANSWER HERE Question 17</font>
# <br>
# <font color = '#FFA07A'>According to above figure, the histogram look not follow normal distribution, Looks like right skewed. Because the data sets have low ‘high value’ (>500).</font>

# Plot the normed cumulative density function (CDF) of the RTs:

# In[18]:


# put your plotting code here Question 18
# YOUR CODE HERE 

df['rt'].plot(kind = 'hist',cumulative = True, density =True)
# add a dashed oragne line at the median
plt.axvline(df['rt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['rt'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['rt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

plt.show()


# How can you tell from the CDF whether or not the data are skewed?
# 

# <font color = 'AA5500'> #YOUR ANSWER HERE Question 19</font>
# <br>
# <font color = '#FFA07A'>From the CDF figure, I can say the data are skewed. The Y value corresponding to 450 on the horizontal axis in CDF is about 0.60. so the proportion of all data points greater than 450 is about 40% The y-value corresponding to 400 on the horizontal axis in CDF is about 0.4, so 400-450 about 0.2. Similarly, we can get the following relation:  300-400:40%, 400-450:20%,450-500:20%. 500 above 20%;  For normal distribution, the median 450 should about 50% but in this case we get 60%. </font>

# ### RT transformations
# 
# While the skew in the RT data makes sense, for the reasons described above, it's problematic when running statistics on the data. This is because many conventional statistical tests, like *t*-tests and ANOVAs, assume that the data are normally distributed. Using skewed data can cause unreliable results. 
# 
# For this reason, many researchers apply some transformation to RTs to make their distribution more normal (statistically normal, that is). A common one is to take the logarithm of the RT values: $log(RT)$; another is to take the inverse: $1/RT$.
# 
# The code below will add a column to your DataFrame called `logrt`. Add a line to plot the histogram of the log-transformed data:

# In[19]:


# log-transform the rt data (done for you) Question 20
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


# Create an `invrt` column containing the inverse transform of RT.

# In[20]:


# YOUR CODE HERE Question 21
df['invrt'] = 1/(df['rt'])


# Plot the histogram of `invrt`

# In[21]:


# YOUR CODE HERE Question 22

df['invrt'].plot(kind='hist')
# add a solid line at the median and dashed lines at the 25th and 75th percentiles (done for you)
plt.axvline(df['invrt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['invrt'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['invrt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

# Rememebr to use plt.show() to see your plots (often they show anyway, but with some garbagy text at the top)
plt.show()


# Does one of these two transforms produce a more normal-looking distribution? If so, which one? 

# <font color = 'AA5500'> #YOUR ANSWER HERE Question 23</font>
# <br>
# <font color = '#FFA07A'>Both of above two figures more normal-looking distributions than original one. Compare logrt figure and invert figure, the invert figure more normal-looking distribution. </font>

# ### Grouping by experimental condition
# 
# Recall that these data are from a "flanker" experiment in which participants had to respond with a left or right button press, depending on whether the target (centre) arrow pointed left or right. The target arrow was flanked with two arrows on either side that were either congruent (pointed in same direction) or incongruent (opposite direction). 
# 
# Our focus in exploring the data will be on errors and reaction times (RTs).
# 
# Let's start by finding out how many trials we have in each condition. Use the `groupby()` method, chained with the `.count()` method, to group the DataFrame by `flankers` and count the number of data points (rows) in each flanker condition.

# In[22]:


# YOUR CODE HERE Question 24
df.groupby(by='flankers').count()


# You should get a DataFrame with two rows (congruent and incongruent), and a count in each of the columns of the original DataFrame. A good start, but a bit TMI and less focused on what we might actually want to know (about errors and RTs).
# 
# Following the examples in Chapter 4 of *Manipulating DataFrames with pandas*, use the "split-apply-combine" approach to show the counts only for `rt` and `error`. 

# In[23]:


# YOUR CODE HERE Question 25
group = df.groupby(by = 'flankers')[['rt','error']].agg('count')
group


# Surprise! There's a third condition: neutral. We're just going to ignore that one for now, so remove all trials (rows) from the DataFrame that have a value of `neutral` in the `flankers` column

# In[24]:


# YOUR CODE HERE Question 26
group = group.drop('neutral')
group


# Now we can get a bit interesting and EDA-ish. Generate a table showing mean RT for each flanker condition.

# In[25]:


# YOUR CODE HERE Question 27
rt_mean = df.groupby(by = 'flankers')[['rt','error']].agg('mean')
rt_mean = rt_mean.drop('neutral')
rt_mean


# Now generate a table for accuracy (the `error` column). Note that in this experiment (counterintuitively), values of `True` in this column indicate *correct* responses, and `False` indicates an error. Also remember that Python treats `True` as having a value of 1, and `False` as 0, when applying mathematical operations to Boolean values.
# 
# In the cell below, show a table with the number of correct trials in each condition. 

# In[26]:


# YOUR CODE HERE Question 28
correct = df.groupby(by = 'flankers')[['error']].agg('sum')
correct.columns = ['Correct']
correct = correct.drop('neutral')
correct


# Now draw a similar table, but showing the accuracy *rate* - i.e., the proportion of trials that were correct in each condition (number of correct trials divided by total number of trials in that condition). 

# In[27]:


# YOUR CODE HERE Question 29
total= df.groupby(by = 'flankers')[['error']].agg('count')
correct = df.groupby(by = 'flankers')[['error']].agg('sum')
number = correct[:2]/total[:2]
number.columns = ['Accuracy']
number


# ### Visualization
# 
# We've been doing a fair bit of EDA already, such as looking at histograms, descriptive statistics, and RTs by condition. But, visualization of data is often more helpful than tables like the ones above. Box plots are a nice way to look at the distribution of variables, and make some visual comparisons between conditions. 
# 
# Plot box plots of the log-transformed RT data (`logrt`) for each flanker condition. Remember that pandas DataFrames have methods for generating plots.
# 
# <div class="alert alert-block alert-info">
# Note: there's no easy way to add titles to the sublpots, or control their arrangement (e.g., making them all appear in one row), but the plots appear in the same order as the conditions are listed in the table you generated above. </div>
# 
# 

# In[28]:


# YOUR CODE HERE Question 30
boxplot1 = df.loc[df['flankers']=='congruent','logrt'].plot(kind = 'box',title = 'Congruent')
plt.show()
boxplot2 = df.loc[df['flankers']=='incongruent','logrt'].plot(kind = 'box',title = 'Incongruent')
plt.show()


# ---
# ### Interpretation
# 
# Recall that the hypothesis for this experiment was that incongruent flankers would lead to slower and less accurate responses. Are the data from this one participant consistent with this hypothesis? Of course, one participant isn't enough to answer the question with any confidence, and we haven't performed any statistics. But simply on the basis of EDA, what can you conclude, and how/why? 

# <font color = 'AA5500'> #YOUR ANSWER HERE Question 31 </font>
# <br>
# <font color = '#FFA07A'> Basis of EDA, I can say incongruent flankers would lead to slower and less accurate responses. according to the participant results, the congruent condition has 100% accuracy and 452.60 (mean) response time. Incongruent condition has 85% accuracy and 466.05 (mean) response time.   </font>

# # The End
