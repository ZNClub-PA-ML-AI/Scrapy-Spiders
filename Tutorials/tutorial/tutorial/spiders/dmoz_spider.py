# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 09:50:27 2016

@author: Nevil Dsouza
"""
import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        
		# response has all scraped data
		
		# file name to be saved
		filename = response.url.split("/")[-2] + '.html'
		
		# write in html file
        with open(filename, 'wb') as f:
            f.write(response.body)
