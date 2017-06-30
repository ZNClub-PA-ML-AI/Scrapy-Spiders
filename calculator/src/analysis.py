# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:51:44 2017

@author: ZNevzz
"""

import pandas as pd
import numpy as np
from datetime import datetime, date, time
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

## READ FILES

filenames=['../calculator.csv']
df=pd.read_csv(filenames[0])


## ANALYSIS

## ROW X COL
#print(df.shape)
#print(df.columns)


## VIEW TOP DATA
#print(df.head())


## DROP NAM
df1= df.dropna()
df2 = df1['price']

## STD MEAN FREQ UNIQUE BOX-PLOT
#print(df1.describe(include=['object']))
#print(df1.describe(include=['number']))

## HISTOGRAM
#print(pd.Series(df2).value_counts())
#print(pd.Series(df2).mode())

## DISCRETIZATION
#print(pd.cut(df2), 10))
df3 = pd.cut(df2, [0,100,200,300,400,500,600,4000])
print(df3.describe())
#print(pd.Series(df3).value_counts())



#print(df2.apply(np.mean))
#print(df2.apply(lambda x: x.max() - x.min())) #not for FLOAT
#print(df2.apply(np.cumsum))

## DATE AND AREA ANALYSIS
dates=[]
areas=[]

for row in df1.itertuples():
    #print(row)
    d=row.date.strip()
    a=row.area.strip()
    #print(row.date)
    #print(d)
    
    dates.append(d)
    areas.append(a)

#date
df4 =pd.Series(dates)
#print(df4.describe())
print(df4.value_counts())

#area
df5 =pd.Series(areas)
#print(df5.describe())
print(df5.value_counts())



## DATE CONVERSION

# refer: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

#dt = datetime.strptime("21 Jun 2017", "%d %b %Y")
#print(dt.day,dt.month,dt.year)
    
    

## VISUALIZATION






