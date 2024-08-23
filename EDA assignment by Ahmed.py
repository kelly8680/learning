
#impoert the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


#import dataset
conflicts = pd.read_csv(r'C:/Users/Victor/Documents/worldconflict.csv')


# In[5]:


#displaying the first few rows of the dataset
conflicts.head(10)


# In[6]:


#overview of the dataset
conflicts.info()


# In[7]:


#understanding the statistics
conflicts.describe()


# In[8]:


#checking the columns
conflicts.columns


# In[9]:


#rename the column Entity to Region for easy understanding

conflicts = conflicts.rename(columns={'Entity': 'Region'})


# In[10]:


#checking for missing or null values
conflicts.isnull().sum()


# In[11]:


#checking for the shape
conflicts.shape


# Data Cleaning 

# In[12]:


#Dropping code column because is irrelevant
conflicts = conflicts.drop(columns=['Code'])


# In[13]:


conflicts.head()


# Data Visualization

# In[14]:


# Histogram of conflicts over the years
plt.figure(figsize=(10, 6))
sns.histplot(conflicts['Year'], kde=False, bins=30)
plt.title('Distribution of Conflicts Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Conflicts')
plt.show()


# In[15]:


# Boxplot for different types of conflicts
plt.figure(figsize=(15, 8))
sns.boxplot(data=conflicts[['One-sided violence', 'Non-state', 'Intrastate', 'Extrasystemic', 'Interstate']])
plt.title('Distribution of Different Types of Conflicts')
plt.show()


# In[16]:


# Group by region and sum the conflicts
region = conflicts.groupby('Year').sum()

# Barplot for conflicts by region
plt.figure(figsize=(12, 6))
region.plot(kind='bar', stacked=True)
plt.title('Total Number of Conflicts by Region')
plt.ylabel('Number of Conflicts')
plt.show()


# In[17]:


# Group by region and sum the conflicts
rt = conflicts.groupby('Region').sum()

# Barplot for conflicts by region
plt.figure(figsize=(15, 8))
rt.plot(kind='bar', stacked=True)
plt.title('Total Number of Conflicts by Region')
plt.xlabel('Region')
plt.ylabel('Number of Conflicts')
plt.show()


# In[ ]:




