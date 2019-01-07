# -*- coding:utf-8 -*-

import scrapy

class ShiyanlouGithubSpider(scrapy.Spider):
    name = 'shiyanlou-github'

    @property
    def start_urls(self):

        return ('https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories',)

    def parse(self, response):
        for user in response.css('div.user-repositories-list'):
            yield {
                    "name": user.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)'),
                    "update_time": user.xpath('.//relative-time/@datetime').extract()
                    }
