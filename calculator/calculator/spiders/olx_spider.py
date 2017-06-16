# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
"""
Created on Mon Nov 14 23:16:56 2016

@author: ZNevzz
"""

import scrapy
import pandas as pd
import re

from calculator.items import CalculatorItem

class Spider(scrapy.Spider):
    
    #spider name
    name = "olx_spider"
    #domains
    allowed_domains = ["olx.in"]    
    #urls
    start_urls=[]
    url_format = "https://www.olx.in/mumbai/q-scientific-calculator/?view=list&page="
    max_range = 2
    for i in range(1,max_range+1):
        url = url_format + str(i)
        start_urls.append(url)
    
    #xpath
    #[ITER]
    
    name_start="/html/body/div/div/section/div/div/div/table/tbody/tr["
    name_end="]/td/table/tbody/tr[1]/td[2]/h3/a/span/text()"
    
    price_start="/html/body/div/div/section/div/div/div/table/tbody/tr["
    price_end="]/td/table/tbody/tr[1]/td/div/p/strong/text()"
    
    area_start="/html/body/div/div/section/div/div/div/table/tbody/tr["    
    area_end="]/td/table/tbody/tr[1]/td[2]/p/small/span/text()"
    
    date_start="/html/body/div/div/section/div/div/div/table/tbody/tr["
    date_end="]/td/table/tbody/tr[2]/td[1]/p/text()"
        
    href_start="/html/body/div/div/section/div/div/div/table/tbody/tr["
    href_end="]/td/table/tbody/tr[1]/td[2]/h3/a/@href"
    ## end

    def checkEmpty(self,temp):
        return (temp==None) or (temp=='')
    
    def parse(self, response):
        
        list_range=40
        item=CalculatorItem()
        
        for i in range(3,list_range+1):
            
            
            #name
            path=self.name_start+str(i)+self.name_end
            temp=response.selector.xpath(path).extract()
            if(self.checkEmpty(temp)):
                continue
            
            item['name']= temp
            
            #price
            path=self.price_start+str(i)+self.price_end
            
            temp=response.selector.xpath(path).extract()
            if(self.checkEmpty(temp)):
                continue
            
            item['price']= temp
            
            #area
            path=self.area_start+str(i)+self.area_end
            
            temp=response.selector.xpath(path).extract()
            if(self.checkEmpty(temp)):
                continue
            
            item['area']= temp
            
            #date
            path=self.date_start+str(i)+self.date_end
            
            temp=response.selector.xpath(path).extract()
            if(self.checkEmpty(temp)):
                continue
            
            item['date']= temp
            
            #href
            path=self.href_start+str(i)+self.href_end
            
            temp=response.selector.xpath(path).extract()
            if(self.checkEmpty(temp)):
                continue
            
            item['href']= temp
            
            yield item
        
