# -*- coding: utf-8 -*-
"""day4 pandas visualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RX7S85qD3fnHA48lFWzuKEd-lxykcaqE
"""

import pandas as pd

df=pd.read_csv('Salaries.csv')

import matplotlib.pyplot as plt

df.columns

df

df['discipline'].value_counts()

df['discipline'].value_counts().plot.bar()

#scatter plot :gives relation between variables
ages=[30,38,45,29,50,47]
salary=[30000,38000,40000,29000,60000,50000]
plt.xlabel("age of person")
plt.ylabel("Salary of person")
plt.title("Salary distribution of employees")
plt.scatter(ages,salary,color="red")

x=[-5,-2,-1,2,4,6,7,10]
y=[35,34,60,50,20,70,90,80]
plt.figure(figsize=(6,4))   # dimension of a figure
plt.suptitle("learning visualization",size=25)
plt.xlim(-20,20)
plt.ylim(10,100)
plt.plot(x,y)

#plot graph of number (-100 to 100) and its square. using range function
x=list(range(-100,101))
y=[i*i for i in x]#list comparision
plt.plot(x,y)

from math import exp
x=list(range(0,30))
y=[exp(i) for i in x]
plt.plot(x,y)

# Plot multiple graphs at a time: eg 12 graphs at a time - 3X4 Grid
from math import *
plt.figure(figsize = (16,9))  #width and height
x=list(range(-10,11))   #remains same
y=[i**2 for i in x]
plt.subplot(3,4,1) # 3 X 4 grid, 1=position of graph 1   2   3   4
#                                                    5   6   7   8
#                                                    9  10  11  12
plt.plot(x,y)
#plt.title=("Graph of Squares")

y=[i**3 for i in x]
plt.subplot(3,4,8) # 8 - position of graph
plt.plot(x,y)
#plt.title=("Graph of Cubes")

y=[sin(i) for i in x]
plt.subplot(3,4,10) # 10 - position of graph
plt.plot(x,y)
#plt.title=("Graph of sin(x)")

#Upload mtcars.csv
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("mtcars.csv")
data



data.shape  # Total no. of rows and columns in dataset, 32 rows, 11 columns

# Find no of cars having certain no of cylinders and certain no of gears
pd.crosstab(data['cyl'],data['gear'])   #unique values in cyl and gear
# eg crosstable shows There are 4 cars with 6 cylinders and 4 gears

pd.crosstab(data['gear'],data['cyl'])

pd.crosstab(data['cyl'],data['gear']).plot(kind='bar')
# Refer below link to see plot() function in pandas - kind parameter
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html

data["gear"].value_counts()

data.gear.value_counts().plot(kind="pie")

# Scatter plot between 2 columns (mpg and qsec)
plt.scatter(data.mpg,data.qsec,color="red")

# Histogram - inbuilt function for histogram is hist()
plt.hist(data.mpg,edgecolor="red")  # single column is enough
# google - plt.hist in matplotlib
# mpg             no. of cars
# 10.4 to 12.75   2
# 12.75 to 15.1   4 and so on... such 10 bins/bars/categories are created by default

# Histogram data distribution
plt.hist(data.mpg,facecolor="yellow",edgecolor="green",bins=6)
# 6 categories are created

# Boxplot  :only single column is enough
plt.boxplot(data.mpg)
plt.show()
# returns result in the form of dictionary {}
# Always refer official documentation
# check 'boxplot in matplotlib documentation' in google, parameter and its explanation is given

plt.boxplot(data.mpg,vert=False,notch=True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv("/content/mtcars.csv")

mtcars.columns

mtcars.shape

mtcars.head()

mtcars.tail()

mtcars.describe()

mtcars.info()

mtcars.hist(figsize=(15,5)) # figsize is a tuple - in inches 15 X 5 inch, Try changing size
plt.tight_layout()
plt.show()

plt.figure(facecolor='yellow')
plt.scatter(mtcars.mpg,mtcars.qsec,marker='*')## scatter plot of two variables, Try different markers
# markers: https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers

plt.show()

#Violin Plot
#help(plt.violinplot)
plt.violinplot(mtcars["mpg"])
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips =sns.load_dataset('tips')
#tips is an inbuilt dataset of seaborn
#sns.get_dataset_names()

tips

tips

sns.get_dataset_names()

tips.head()

tips.shape

tips.describe()

tips.shape[0]

tips.columns

pd.crosstab(tips['smoker'],tips['sex'])    #gives an unique value

pd.crosstab(tips['smoker'],tips['sex']).plot(kind="bar")

# seaborn plots documentaion - https://seaborn.pydata.org/tutorial/function_overview.html
#strip plot
sns.stripplot(y='tip', data=tips) # try jitter=False / True

sns.stripplot(x='sex',y='tip', data=tips,jitter=False)    #jitter is optional default it is true

sns.stripplot(x='day',y='tip', data=tips,jitter=True)

sns.stripplot(x='day',y='tip', data=tips,jitter=True,size=3)    #size of circle in a graph

#swarm plot
sns.swarmplot(x='day',y='tip',data=tips,size=6)   #size is optional

#high amount of tip is given by male and specifically on saturday
sns.swarmplot(x='day',y='tip',data=tips,hue='sex')  #
plt.show()

sns.swarmplot(x='day',y='tip',data=tips,hue='time')  #
plt.show()

# subplot
plt.subplot(2,2,1) # nrows,ncols,position
sns.boxplot(x='day', y='tip', data=tips)

plt.subplot(2,2,2) # nrows,ncols,position
sns.boxplot(x='day', y='tip', data=tips)
#plt.ylabel=('tip ($)')
#plt.title=("Boxplot of tips")

plt.subplot(2,2,3)
sns.violinplot(x='day', y='tip', data=tips)

plt.subplot(2,2,4)
sns.violinplot(x='day', y='tip', data=tips)
#plt.ylabel=('tip ($)')
#plt.title=("violin plot of tips")

plt.show()

sns.scatterplot(data=tips,x="total_bill",y="tip")



sns.scatterplot(data=tips,x="total_bill",y="tip",hue="time")

sns.histplot(x="total_bill",data=tips)
# here we get frequecy also in histogram

sns.jointplot(x="total_bill",y="tip",data=tips)
plt.show()

pd.plotting.scatter_matrix(tips)  #this is from pandas
plt.show()

#pair plot:if dataset has many numeric column you can plot many plots of diff.combination using pairplot
#diagonally it gives histo or bar plot of individual plot of total_bill,tip and size
sns.pairplot(tips)
plt.show()

sns.pairplot(tips,hue="sex") #diagonally male female distribution
plt.show()#try hue=time ,smoker,day,etc .to check diff.pattern,gain more information

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

data=pd.read_csv("train.csv")
data.head()

data

data.info()

data.describe()

data.groupby("Survived")["PassengerId"].count()

pd.crosstab(data['Survived'],data['Sex'])

pd.crosstab(data['Survived'],data['Sex']).plot(kind='bar')

plt.figure(figsize=(10,5))
sns.boxplot(x='Survived', y="Age",  data=data);

#plt.figure(figsize=(11,5))
sns.boxplot(x="Sex", y="Age", hue="Survived", data=data)





sns.barplot(x="Pclass", y="Survived", data=data)

sns.barplot(x="Pclass", y="Survived", data=data)

sns.barplot(x="SibSp", y="Survived", data=data)

sns.barplot(x="Parch", y="Survived", data=data)

#data.loc[data['Survived']==1,"Age"] # age col contains some na values
sns.distplot(data.loc[data['Survived']==1,"Age"])

survived = data.loc[data['Survived']==1,"Age"].dropna()
sns.distplot(survived)
# plt.title=("Survived");

not_survived = data.loc[data['Survived']==0,"Age"].dropna()
sns.distplot(not_survived)
# plt.title=("Not Survived");

sns.pairplot(data) #scatterplot of all variables

# Pclass vs Survive
grid = sns.FacetGrid(data, col='Survived', row='Pclass', height=2.4, aspect=1.5)
grid.map(plt.hist, 'Age', alpha=0.9, bins=20)# alpha: shade of graph, try alpha=0.1 or 0.9 Range: 0 to 1,bin menas number of bars
#grid.add_legend()

fig,ax=plt.subplots(nrows=2,ncols=2) # empty spaces for plots, change nrows and ncols

# subplots():- creates a figure and a grid of subplots
# subplots() without arguments returns a Figure and a single Axes
fig, ax = plt.subplots()
ages=[30,38,45,29,50,47]
salary=[30000,38000,40000,29000,60000,50000]
ax.plot(ages,salary)
ax.set_title('A single plot')

figbi, axesbi = plt.subplots(2, 4, figsize=(18, 10))
data.groupby('Pclass')['Survived'].mean().plot(kind='bar',ax=axesbi[0,0],xlim=[0,1])
data.groupby('SibSp')['Survived'].mean().plot(kind='bar',ax=axesbi[0,1],xlim=[0,1])
data.groupby('Parch')['Survived'].mean().plot(kind='bar',ax=axesbi[0,2],xlim=[0,1])
data.groupby('Sex')['Survived'].mean().plot(kind='bar',ax=axesbi[0,3],xlim=[0,1])
data.groupby('Embarked')['Survived'].mean().plot(kind='bar',ax=axesbi[1,0],xlim=[0,1])
sns.boxplot(x="Survived", y="Age", data=data,ax=axesbi[1,1])
sns.boxplot(x="Survived", y="Fare", data=data,ax=axesbi[1,2])
plt.show()
figbi.savefig("myfig.png") # or ("my1stfig.jpeg")
from google.colab import files
files.download("myfig.png")

data.groupby('Pclass')['Survived'].mean()

Plotly.express: Additional Code
List item

import plotly.express as px
ages=[30,38,45,29,50,47]
salary=[30000,38000,40000,29000,60000,50000]
fig = px.line(x=ages, y=salary) #,title="layout.hovermode='closest' (the default)"
#fig.update_traces(mode="markers+lines")
fig.show()

#df = px.data.gapminder().query("continent=='Oceania'") # built in dataset
fig = px.scatter(df,x='service',y='salary')
fig.show()



ages=[15,15,20,20,20,20,20,20,20,20,22,22,22,22]
marks=[45,50,30,30,30,30,60,65,80,90,95,80,70,50]
marks_dict={'ages':ages,'marks':marks}
mkdf=pd.DataFrame(marks_dict)
mkdf

fig =px.bar(mkdf,x='marks',y='ages',text_auto=True)
fig.show()

























#

























































