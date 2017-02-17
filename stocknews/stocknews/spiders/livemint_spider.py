# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
"""
Created on Mon Nov 14 23:16:56 2016

@author: Nevil Dsouza
"""

import scrapy
import pandas as pd
import re

from stocknews.items import StocknewsItem

class LivemintSpider(scrapy.Spider):
    
    #spider name
    name = "livemint_spider"
    #domains
    allowed_domains = ["livemint.com"]
    #urls
    start_urls = []
        
    file_name = 'livemint_data_2.csv'

    df = pd.read_csv(file_name,encoding='iso-8859-1')
    
    start_urls = df['href'].tolist()

        
    def parse(self, response):
        
        path = "/html/body/div[@id='o-wrapper']/div[@class='wrapper']/section[@class='left-col']/div[@id='div_storyContent']/div[@class='story-content']/p"
        body = response.selector.xpath(path).extract()
        result=""
        for i in body:
            temp = re.sub("<p>", "", i)
            temp = re.sub("</p>","",temp)
            temp = re.sub("<i>The writer does not own shares in the above-mentioned companies.</i>","",temp)
            result=result+temp
        
        result = result.strip()
        return {'body':result}
        

'''
2016-11-15 09:02:44 [scrapy] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 130494,
 'downloader/request_count': 306,
 'downloader/request_method_count/GET': 306,
 'downloader/response_bytes': 2140065,
 'downloader/response_count': 306,
 'downloader/response_status_count/200': 201,
 'downloader/response_status_count/302': 105,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2016, 11, 15, 3, 32, 44, 393673),
 'item_scraped_count': 2000,
 'log_count/DEBUG': 2306,
 'log_count/ERROR': 22,
 'log_count/INFO': 8,
 'response_received_count': 201,
 'scheduler/dequeued': 305,
 'scheduler/dequeued/memory': 305,
 'scheduler/enqueued': 305,
 'scheduler/enqueued/memory': 305,
 'start_time': datetime.datetime(2016, 11, 15, 3, 32, 33, 627249)}

'''

'''

'''


"""
    for i in range(24,-1,-1):
        
        if i in range(0,4):
            url_company_opinion = "http://www.livemint.com/Query/DIoW9PdSAJUlZsu7iBevDI/companies-opinion.html?facet=subSection&page="
            temp = url_company_opinion+str(i)
            start_urls.append(temp)
    
        url_company_management = "http://www.livemint.com/Query/V1eAlpSAzt0kHm6oBnOvDI/management.html?facet=subSection&page=0"    
        temp = url_company_management+str(i)
        start_urls.append(temp)
    
        if i in range(0,18):
            url_results = "http://www.livemint.com/Query/ZtZgviOVr74zwZ37eD9uDI/results.html?facet=subSection&page=0"    
            temp = url_results+str(i)
            start_urls.append(temp)
        
        if i in range(0,14):
            url_people = "http://www.livemint.com/Query/lZy3FU0kP9Cso5deYypuDI/people.html?facet=subSection&page=0"
            temp = url_people+str(i)
            start_urls.append(temp)
        
        if i in range(0,20):
            url_infotech = "http://www.livemint.com/Query/P8RBwcvO9gvJl6xh6wTNzO/infotech.html?facet=subSection&page=0"    
            temp = url_infotech+str(i)
            start_urls.append(temp)
        
        url_finservices = "http://www.livemint.com/Query/5jCbPmmTjmX6bvfyV5XlkJ/financial-services.html?facet=subSection&page=0"    
        temp = url_finservices+str(i)
        start_urls.append(temp)
    
        url_energy = "http://www.livemint.com/Query/hHUQJ3ncBXZBGH3eVyKlkJ/energy.html?facet=subSection&page=0"    
        temp = url_energy+str(i)
        start_urls.append(temp)
        
        if i in range(0,4):
            url_industry_opinion = "http://www.livemint.com/Query/t5YPD42JdoNxoDBxwNemkJ/industry-opinion.html?facet=subSection&page=0"    
            temp = url_industry_opinion+str(i)
            start_urls.append(temp)
"""    

"""
    def parse(self, response):
        
        title_start = "/html/body/div[@id='o-wrapper']/div[@class='wrapper']/section[@class='left-col']/div[@class='listing-box-container']/div[@class='listing-box']["
        title_end = "]/div[@class='text-box']/h2[@class='split-heading-strong']/a/text()"        
        intro_start = "/html/body/div[@id='o-wrapper']/div[@class='wrapper']/section[@class='left-col']/div[@class='listing-box-container']/div[@class='listing-box']["
        intro_end = "]/div[@class='text-box']/p[@class='intro']/a/text()"
        date_start = "/html/body/div[@id='o-wrapper']/div[@class='wrapper']/section[@class='left-col']/div[@class='listing-box-container']/div[@class='listing-box']["
        date_end = "]/div[@class='text-box']/p[@class='date-box']/text()"        
        href_start = "/html/body/div[@id='o-wrapper']/div[@class='wrapper']/section[@class='left-col']/div[@class='listing-box-container']/div[@class='listing-box']["
        href_end = "]/div[@class='text-box']/h2[@class='split-heading-strong']/a/@href"     
           
        result=[]        
        
        for i in range(1,11):
            
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
            item['href'] = "http://www.livemint.com"+temp[0]
            
            result.append(item)
        
        return result
"""        