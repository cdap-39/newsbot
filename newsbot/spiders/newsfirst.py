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

        news = []

        # Main headings
        for news_block in response.xpath("//div[contains(@class, 'main-news-block')]"):
            news_item = {
                'heading': news_block.xpath("a/div[contains(@class, 'main-news-heading')]/h1/text()").extract_first(),
                'link': news_block.xpath("a/@href").extract_first()
            }
            news.append(news_item)

        # Sub headings
        # for news in response.css('div.sub-1-news-block'):
        #     headings.append({
        #         'heading': news.css('div.sub-1-news-heading>h2::text').extract_first()
        #     })

        with open(filename, 'w') as outfile:
            json.dump(news, outfile, indent=4)
