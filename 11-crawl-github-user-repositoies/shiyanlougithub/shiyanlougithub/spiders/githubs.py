# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem 

class GithubsSpider(scrapy.Spider):
    name = 'githubs'
    allowed_domains = ['github.com']

    @property
    def start_urls(self):
        return('https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories',
                )

    def parse(self, response):
        for user in response.css('li.public'):
            item = ShiyanlougithubItem ({
                    "name": user.xpath('.//a[@itemprop="name codeRepository"]/text()').re(r'\n\s*(.*)'),
                    "update_time": user.xpath('.//relative-time/@datetime').extract()})
            yield item
