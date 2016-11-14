# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
"""
Created on Mon Nov 14 23:16:56 2016

@author: Nevil Dsouza
"""

import scrapy
from stocknews.items import StocknewsItem

class LivemintSpider(scrapy.Spider):
    name = "livemint_spider"

    allowed_domains = ["livemint.com"]
    
    start_urls = [
        "http://www.livemint.com/Query/DIoW9PdSAJUlZsu7iBevDI/companies-opinion.html?facet=subSection&page=24"
        
    ]    
    
    def parse(self, response):
        
        title_start = "/html/body/div[@id='o-wrapper']/div[@class='wrapper']/section[@class='left-col']/div[@class='listing-box-container']/div[@class='listing-box']["        
        title_end = "]/div[@class='text-box']/h2[@class='split-heading-strong']/a/text()"        
        intro_start = "/html/body/div[@id='o-wrapper']/div[@class='wrapper']/section[@class='left-col']/div[@class='listing-box-container']/div[@class='listing-box']["        
        intro_end = "]/div[@class='text-box']/p[@class='intro']/a/text()"
        date_start = "/html/body/div[@id='o-wrapper']/div[@class='wrapper']/section[@class='left-col']/div[@class='listing-box-container']/div[@class='listing-box']["        
        date_end = "]/div[@class='text-box']/p[@class='date-box']/text()"        
        
        result=[]        
        
        for i in range(1,11):
            
            item = StocknewsItem()

            path = title_start+str(i)+title_end
            item['title'] = response.selector.xpath(path).extract()
            
            path = intro_start+str(i)+intro_end
            item['intro'] = response.selector.xpath(path).extract()
            
            path = date_start+str(i)+date_end
            item['date'] = response.selector.xpath(path).extract()
            
            result.append(item)
        
        return result