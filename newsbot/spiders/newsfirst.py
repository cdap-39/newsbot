# -*- coding: utf-8 -*-
import scrapy
import json


class NewsfirstSpider(scrapy.Spider):
    name = 'newsfirst'
    allowed_domains = ['newsfirst.lk']
    start_urls = ['http://newsfirst.lk/category/local/']

    def parse(self, response):
        # Web page name
        page = 'newsfirst-local'
        filename = '%s.json' % page

        headings = []

        # Main headings
        for news in response.css('div.main-news-heading'):
            headings.append({
                'heading': news.css('h1::text').extract_first()
            })

        # Sub headings
        for news in response.css('div.sub-1-news-heading'):
            headings.append({
                'heading': news.css('h2::text').extract_first()
            })

        with open(filename, 'w') as outfile:
            json.dump(headings, outfile, indent=4)
