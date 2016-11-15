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
    start_urls = ["http://economictimes.indiatimes.com/markets/stocks/news/articlelist/msid-2146843,page-1.cms"]
    '''
    for i in range(24,-1,-1):
        
        url_company_opinion = "http://www.livemint.com/Query/DIoW9PdSAJUlZsu7iBevDI/companies-opinion.html?facet=subSection&page="

        temp = url_company_opinion+str(i)
        start_urls.append(temp)
    
        url_company_management = "http://www.livemint.com/Query/V1eAlpSAzt0kHm6oBnOvDI/management.html?facet=subSection&page=0"
    
        temp = url_company_management+str(i)
        start_urls.append(temp)
        
        url_results = "http://www.livemint.com/Query/ZtZgviOVr74zwZ37eD9uDI/results.html?facet=subSection&page=0"
    
        temp = url_results+str(i)
        start_urls.append(temp)
        
        url_people = "http://www.livemint.com/Query/lZy3FU0kP9Cso5deYypuDI/people.html?facet=subSection&page=0"

        temp = url_people+str(i)
        start_urls.append(temp)
    
        url_infotech = "http://www.livemint.com/Query/P8RBwcvO9gvJl6xh6wTNzO/infotech.html?facet=subSection&page=0"
    
        temp = url_infotech+str(i)
        start_urls.append(temp)
        
        url_finservices = "http://www.livemint.com/Query/5jCbPmmTjmX6bvfyV5XlkJ/financial-services.html?facet=subSection&page=0"
    
        temp = url_finservices+str(i)
        start_urls.append(temp)
    
        url_energy = "http://www.livemint.com/Query/hHUQJ3ncBXZBGH3eVyKlkJ/energy.html?facet=subSection&page=0"
    
        temp = url_energy+str(i)
        start_urls.append(temp)

        url_industry_opinion = "http://www.livemint.com/Query/t5YPD42JdoNxoDBxwNemkJ/industry-opinion.html?facet=subSection&page=0"
    
        temp = url_industry_opinion+str(i)
        start_urls.append(temp)
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
        
        for i in range(1,2):
            
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