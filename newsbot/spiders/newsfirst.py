# -*- coding: utf-8 -*-
import scrapy


class NewsfirstSpider(scrapy.Spider):
    name = 'newsfirst'
    allowed_domains = ['newsfirst.lk']
    start_urls = ['http://newsfirst.lk/']

    def parse(self, response):
        page = response.url.split("/")[-2]
        self.log('**********************************************************************')
        self.log(response.url)
        self.log('**********************************************************************')
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
