# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

"""
Created on Tue Aug 23 09:50:27 2016

@author: Nevil Dsouza
"""

import scrapy

class DmozItem(scrapy.Item):
	#title, href link and description
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()