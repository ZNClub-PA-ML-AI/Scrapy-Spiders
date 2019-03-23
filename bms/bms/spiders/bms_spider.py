# -*- coding: utf-8 -*-
import scrapy
import logging


class BmsSpiderSpider(scrapy.Spider):
	name = "bms_spider"
	allowed_domains = ["bookmyshow.in"]
	start_urls = (
		'https://in.bookmyshow.com',
		)

	def manage_list(self, card_list):
		for element in card_list:
			logging.info('Element={}'.format(element))

		no_of_items = len(card_list)
		logging.info('No of Element={}'.format(no_of_items))

	def parse(self, response):
		search_term = 'Bengaluru'
		parent_path = '//div[@class="cards-list"]'
		path = parent_path + '/*[contains(text(),{})]'.format(search_term)
		temp=response.selector.xpath(path).extract()
		
		if isinstance(temp, list):
			self.manage_list(temp)

