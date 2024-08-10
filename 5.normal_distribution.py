# -*- coding: utf-8 -*-
"""normal distribution.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CN-ZEksbXHcIaoMzzqEkqGmtubnN3M4c
"""

from scipy import stats

stats.norm.cdf(70,60,10)  #70 -distrubution value,60-mean,10=SD

stats.norm.cdf(80,60,10)  #cdf give only left hand side area

1-stats.norm.cdf(80,60,10)

stats.norm.cdf(680,711,29)   #x<680

1-stats.norm.cdf(680,711,29)  #x>680

stats.norm.cdf(750,711,29)   #x<750

1-stats.norm.cdf(750,711,29)  #x>750

stats.norm.cdf(740,711,29)    #(740>x)

stats.norm.cdf(740,711,29)-stats.norm.cdf(680,711,29)   # ib betwwen 680 and 740 calculate both and subtract each

#gain=today price-yesterday price/yesterday price

from scipy import stats
import pandas as pd
import numpy as np


import warnings
warnings.filterwarnings("ignore")

beml_df=pd.read_csv("BEML.csv")
beml_df.head()

glaxo_df=pd.read_csv("GLAXO.csv")
glaxo_df.head()

glaxo_df=glaxo_df[["Date","Close"]]
beml_df=beml_df[["Date","Close"]]

beml_df

glaxo_df

beml_df.dtypes

glaxo_df.dtypes

# '''The DataFrames have a date column, so we can
# create a DatetimeIndex index from this column Date. It will ensure that the rows are sorted by time in
# ascending order.''',set_index  help to set a date as a index
glaxo_df = glaxo_df.set_index(pd.DatetimeIndex(glaxo_df['Date']))
beml_df = beml_df.set_index(pd.DatetimeIndex(beml_df['Date']))

glaxo_df.head()

beml_df.head()

import matplotlib.pyplot as plt
import seaborn as sns
plt.plot(glaxo_df.Close)
plt.xlabel("Time")
plt.ylabel("Close Price")

plt.plot(beml_df.Close)
plt.xlabel("time")
plt.ylabel("close")

# Gain is for each day. We are assuming that gain is coming from normal distribution.
glaxo_df['gain'] = glaxo_df.Close.pct_change(periods = 1)   # inorder to add column gain ,pct change function ,period=1 one day before data
beml_df['gain'] = beml_df.Close.pct_change(periods = 1)

glaxo_df

beml_df

#drop first row since it is NaN
glaxo_df=glaxo_df.dropna()
beml_df=beml_df.dropna()

glaxo_df

beml_df

# GLAXO: Plot the gains. Over the years gain is not changing much.
# In 2014 gain was highest i.e.20% and highest loss upto 7%. Sometimes positive sometimes negative

plt.figure(figsize = (8, 5))
plt.plot(glaxo_df.gain)
plt.xlabel('Time')
plt.ylabel('gain')

# BEML: from 2010 to 2012 gain was on lower side and after that gain increased upto 2015
plt.figure(figsize = (8, 5))
plt.plot(beml_df.gain)
plt.xlabel('Time')
plt.ylabel('gain')

plt.figure(figsize=(10,5))
plt.suptitle('Distribution',fontsize=15)
plt.subplot(1,2,1)
sns.distplot(glaxo_df.gain, label = 'Glaxo')  #1st graph
plt.xlabel('gain')
plt.ylabel('Density')
plt.legend()  # to give a name glaxo and beml
plt.subplot(1,2,2)
sns.distplot(beml_df.gain, label = 'BEML')  #2nd graph
plt.xlabel('gain')
plt.ylabel('Density')
plt.legend()

#bell shaped normal distribution

plt.figure(figsize=(10,5))
sns.distplot(glaxo_df.gain, label = 'Glaxo')
sns.distplot(beml_df.gain, label = 'BEML')
plt.xlabel('Gain')
plt.ylabel('Density')
plt.legend()
# for BEML there is more variance (high risk or volatality) than GLAXO

# Glaxo Mean and Standard Deviation
print('Glaxo Mean:', round(glaxo_df.gain.mean(), 4))
print('Glaxo Standard Deviation: ', round(glaxo_df.gain.std(), 4))

glaxo_df.gain.mean()

# BEML Mean and Standard Deviation
print('BEML Mean: ', round(beml_df.gain.mean(), 4))
print('BEML Standard Deviation: ', round(beml_df.gain.std(), 4))
# BEML has high std

from scipy import stats
# import scipy
#Probability of making 2% loss or higher loss in Glaxo - left of 0 i.e.e -0.02
stats.norm.cdf(-0.02,0.0004, 0.0134) # norm.cdf(0.02,mean,std)
#loc=glaxo_df.gain.mean(),
#scale=glaxo_df.gain.std()) # there are 6% of chances having 2% or higher loss

stats.norm.cdf( -0.02,
loc=beml_df.gain.mean(),
scale=beml_df.gain.std())

1-stats.norm.cdf( 0.02,
loc=beml_df.gain.mean(),
scale=beml_df.gain.std())

# To understand difference between cdf() and ppf() execute below code.
# (Cumulative Distribution Function): norm.cdf(normal distribution value, loc, scale): calculates probability for a given normal distribution value.
# (Percent Point Function): norm.ppf(probability,loc,scale): calculates normal distribution value for a given probability.
stats.norm.ppf(0.06395593743937553,0.0004, 0.0134) # output of above command,loc,scale

#Probability of making 2% gain or higher gain in Glaxo - to the right of 0.02
1 - stats.norm.cdf(0.02,0.0004, 0.0134) # 7% chances of having at least 2% or higher gain, Glaxo seems safer than BEML

































