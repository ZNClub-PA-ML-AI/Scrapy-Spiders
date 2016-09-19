# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy import Spider
from scrapy.selector import Selector

class StackSpider(Spider):
    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]	
	def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
            yield item