# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 10:52:43 2017

@author: ZNevzz
"""

from bs4 import BeautifulSoup
import pandas as pd

filenames=['../result.json']

df1=pd.read_json(filenames[0])

df2=pd.DataFrame()
for k,r in df1.iterrows():
    
    #name=BeautifulSoup(str(r.name),"lxml")
    price=BeautifulSoup(str(r.price),"lxml")
    date=BeautifulSoup(str(r.date),"lxml")
    #area=BeautifulSoup(str(r.area),"lxml")
    
    
    
    df=pd.DataFrame({'index':[k],'date':[date.get_text()],'name':[r.name],'area':[r.area],'price':[price.get_text()],'href':[r.href]})
    df2=pd.concat([df2,df])
    
df2=df2.set_index('index')
df2.to_csv('../calculator.csv', sep=',', encoding='utf-8')




