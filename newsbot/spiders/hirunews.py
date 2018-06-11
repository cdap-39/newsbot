# -*- coding: utf-8 -*-
import scrapy
from newsbot.items import NewsItem


class HirunewsSpider(scrapy.Spider):
    name = 'hirunews'
    allowed_domains = ['hirunews.lk']
    start_urls = ['http://www.hirunews.lk/local-news.php']

    def parse(self, response):

        # Main headings
        for news_block in response.xpath("//div[contains(@class, 'lts-cntp')]"):
            item = NewsItem()
            heading = news_block.xpath("a/text()").extract_first()
            item["heading"] = heading
            yield item
