# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 10:52:43 2017

@author: ZNevzz
"""

#from bs4 import BeautifulSoup
import pandas as pd

filenames=['../result.json']

df1=pd.read_json(filenames[0])
print(df1.head())

df2=pd.DataFrame()
for k,r in df1.iterrows():
        
    price=str(r.price).replace("\n","").replace("\t","\n")
    date=str(r.date).replace("\n","").replace("\t","\n")
    
    df=pd.DataFrame({'index':[k],'date':[date],'name':[r.name],'area':[r.area],'price':[price],'href':[r.href]})
    df2=pd.concat([df2,df])
    
df2=df2.set_index('index')
df2.to_csv('../calculator.csv', sep=',', encoding='utf-8')


