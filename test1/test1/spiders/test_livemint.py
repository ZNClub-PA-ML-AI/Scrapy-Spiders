# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 18:20:56 2016

@author: Nevil Dsouza
"""

import scrapy

class DmozSpider(scrapy.Spider):
    name = "test_livemint"

    allowed_domains = ["livemint.com"]
    
    start_urls = [
        "http://www.livemint.com/Query/DIoW9PdSAJUlZsu7iBevDI/companies-opinion.html?facet=subSection&page=0"
        
    ]

    def parse(self, response):
        
        path = "/html/body/div[@id='o-wrapper']/div[@class='wrapper']/section[@class='left-col']/div[@class='listing-box-container']/div[@class='listing-box'][1]/div[@class='text-box']/h2[@class='split-heading-strong']"
        text = response.selector.xpath(path).extract()
        with open("output.md", 'w') as f:
            f.write(text[0])