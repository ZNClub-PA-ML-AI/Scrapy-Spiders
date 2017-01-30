# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
"""
Created on Tue Nov 15 09:10:34 2016

@author: Nevil Dsouza
"""

import scrapy
import pandas as pd
import csv
from stocknews.items import StocknewsItem

class EconomictimesSpider(scrapy.Spider):
    
    #spider name
    name = "economictimes_spider"
    #domains
    allowed_domains = ["economictimes.indiatimes.com"]
    #urls 1 to 100
    start_urls = []
    
#    for i in range(100,0,-1):
#        
#        url_start = "http://economictimes.indiatimes.com/markets/stocks/news/articlelist/msid-2146843,page-"
#        url_end = ".cms"
#        temp = url_start+str(i)+url_end
#        start_urls.append(temp)
#    
    
    file_name = 'economictimes_href.csv'

    df = pd.read_csv(file_name,encoding='iso-8859-1')
    
    start_urls = df['href'].tolist()[:1]
    
    
    
#    with open('set.csv', 'w') as myfile:
#        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#        wr.writerow(temp_set)    
    
#    company_list = df['company'].tolist()[:10]
#    
#    file_name = 'output_89.csv'
#
#    df = pd.read_csv(file_name,encoding='iso-8859-1')
#    
#    date_list = df['date'].tolist()[:10]
#    title_list = df['title'].tolist()[:10]
#    intro_list = df['intro'].tolist()[:10]
#    
    
    
        
    def parse(self,response):
        #path = "/html/body[@class='bgImg ']/section[@id='netspidersosh']/div[@id='c_01']/section[@id='pageContent']/article/div[@class='artText printLiveShow']/div[@class='section1']/div[@class='Normal']"
        path = "/html/body[@class='bgImg ']/section[@id='netspidersosh']/div[@id='c_01']/section[@id='pageContent']/article/h1[@class='title']/text()"
        body = response.selector.xpath(path).extract()
#        if len(body)==0:
#            body = 'null'
#        
        return {'body':body}
'''
2016-11-15 09:45:40 [scrapy] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 28428,
 'downloader/request_count': 101,
 'downloader/request_method_count/GET': 101,
 'downloader/response_bytes': 2736170,
 'downloader/response_count': 101,
 'downloader/response_status_count/200': 101,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2016, 11, 15, 4, 15, 40, 612781),
 'item_scraped_count': 1000,
 'log_count/DEBUG': 1101,
 'log_count/ERROR': 5,
 'log_count/INFO': 8,
 'response_received_count': 101,
 'scheduler/dequeued': 100,
 'scheduler/dequeued/memory': 100,
 'scheduler/enqueued': 100,
 'scheduler/enqueued/memory': 100,
 'start_time': datetime.datetime(2016, 11, 15, 4, 15, 27, 260002)}

'''

'''
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
        ad = True
        
        for i in range(1,33):
            
            item = StocknewsItem()
            

            path = title_start+str(i)+title_end
            #item['title'] = response.selector.xpath(path).extract()
            temp = response.selector.xpath(path).extract()
            
            #validity check            
            if len(temp)==0:
                if ad is False:
                    continue
                else:                    
                    ad=False
                    continue
            else:
                ad = True
                item['title'] = temp
            
            path = intro_start+str(i)+intro_end
            item['intro'] = response.selector.xpath(path).extract()
            
            path = date_start+str(i)+date_end
            item['date'] = response.selector.xpath(path).extract()
            
            path = href_start+str(i)+href_end
            temp = response.selector.xpath(path).extract()
            item['href'] = "http://economictimes.indiatimes.com"+temp[0]
            
            result.append(item)
        
        return result

'''