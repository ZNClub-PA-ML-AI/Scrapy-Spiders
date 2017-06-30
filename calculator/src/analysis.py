# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:51:44 2017

@author: ZNevzz
"""

import pandas as pd

filenames=['../calculator.csv']

df1=pd.read_csv(filenames[0])
print(df1.head())
