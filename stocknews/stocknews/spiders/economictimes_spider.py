# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
"""
Created on Mon Nov 15 09:10:34 2016

@author: Nevil Dsouza
"""

import scrapy
from stocknews.items import StocknewsItem

class EconomictimesSpider(scrapy.Spider):
    
    #spider name
    name = "economictimes_spider"
    #domains
    allowed_domains = ["economictimes.indiatimes.com"]
    #urls 1 to 100
    start_urls = []
    
    for i in range(100,0,-1):
        
        url_start = "http://economictimes.indiatimes.com/markets/stocks/news/articlelist/msid-2146843,page-"
        url_end = ".cms"
        temp = url_start+str(i)+url_end
        start_urls.append(temp)
    
        
    def parse(self, response):

        title_start = "/html/body/section[@id='netspidersosh']/section[@id='pageContent']/div[@class='eachStory']["
        title_end = "]/h3/a/text()"                
        intro_start = "/html/body/section[@id='netspidersosh']/section[@id='pageContent']/div[@class='eachStory']["
        intro_end = "]/p/text()"
        date_start = "/html/body/section[@id='netspidersosh']/section[@id='pageContent']/div[@class='eachStory']["
        date_end = "]/time[@class='date-format']/text()"        
        href_start = "/html/body/section[@id='netspidersosh']/section[@id='pageContent']/div[@class='eachStory']["
        href_end = "]/h3/a/@href"     
           
        result=[]        
        
        for i in range(1,33):
            
            item = StocknewsItem()

            path = title_start+str(i)+title_end
            #item['title'] = response.selector.xpath(path).extract()
            temp = response.selector.xpath(path).extract()
            
            #validity check            
            if temp is None:
                break
            else:
                item['title'] = temp
            
            path = intro_start+str(i)+intro_end
            item['intro'] = response.selector.xpath(path).extract()
            
            path = date_start+str(i)+date_end
            item['date'] = response.selector.xpath(path).extract()
            
            path = href_start+str(i)+href_end
            temp = response.selector.xpath(path).extract()
            item['href'] = ""+temp[0]
            
            result.append(item)
        
        return result

'''

'''