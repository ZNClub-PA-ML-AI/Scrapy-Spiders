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
    price_end="]/td/table/tbody/tr[1]/td/div/p/text()"
    
    area_start="/html/body/div/div/section/div/div/div/table/tbody/tr["    
    area_end="]/td/table/tbody/tr[1]/td[2]/p/small/span/text()"
    
    date_start="/html/body/div/div/section/div/div/div/table/tbody/tr["
    date_end="]/td/table/tbody/tr[2]/td[1]/p/text()"
        
    href_start="/html/body/div/div/section/div/div/div/table/tbody/tr["
    href_end="]/td/table/tbody/tr[1]/td[2]/h3/a/@href/text()"
    ## end

    def parse(self, response):
        
        list_range=40
        item=CalculatorItem()
        
        for i in range(3,list_range+1):
            
            
            #name
            path=self.name_start+str(i)+self.name_end
            temp = response.selector.xpath(path).extract()
            if(temp==None or temp==''):
                break
            
            item['name']= temp
            
            #price
            path=self.price_start+str(i)+self.price_end
            
            item['price']= response.selector.xpath(path).extract()
            
            #area
            path=self.area_start+str(i)+self.area_end
            
            item['area']= response.selector.xpath(path).extract()
            
            #date
            path=self.date_start+str(i)+self.date_end
            
            item['date']= response.selector.xpath(path).extract()
            
            #href
            path=self.href_start+str(i)+self.href_end
            
            item['href']= response.selector.xpath(path).extract()
            
            yield item
        
