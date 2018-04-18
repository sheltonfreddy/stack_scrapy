from scrapy import Spider
from scrapy.selector import Selector

from stackoverflow.items import StackoverflowItem

class StackSpider(Spider):
    name = 'stackspider'
    allowed_domains = ['www.stackoverflow.com']
    start_urls = ["http://stackoverflow.com/questions?pagesize=50&sort=newest",]

    def parse(self,response):
        print ("0000000000>>>>>>>>>>>>>>>>>>>>>>>>>Processing")
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackoverflowItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]

            yield item