# -*- coding: utf-8 -*-
import scrapy
from newsbot.items import NewsItem


class NewsfirstSpider(scrapy.Spider):
    name = 'newsfirst'
    allowed_domains = ['newsfirst.lk']
    start_urls = ['http://newsfirst.lk/category/local/']

    def parse(self, response):

        # Main headings
        for news_block in response.xpath("//div[contains(@class, 'main-news-block')]"):
            heading = news_block.xpath("a/div[contains(@class, 'main-news-heading')]/h1/text()").extract_first()
            content_link = news_block.xpath("a/@href").extract_first()

            # Extract content by following the link.
            item = NewsItem()

            item['heading'] = heading
            item['link'] = content_link
            request = scrapy.Request(content_link, callback=self.parse_content)
            request.meta['item'] = item
            yield request

        # Sub headings
        for news_block in response.css('div.sub-1-news-block'):
            heading = news_block.xpath("a/div[contains(@class, 'sub-1-news-heading')]/h2/text()").extract_first()
            content_link = news_block.xpath("a/@href").extract_first()

            # Extract content by following the link.
            item = NewsItem()

            item['heading'] = heading
            item['link'] = content_link
            request = scrapy.Request(content_link, callback=self.parse_content)
            request.meta['item'] = item
            yield request

    # Parse content of the news article
    def parse_content(self, response):
        item = response.meta['item']
        content = response.xpath("string(//div[contains(@class, 'text-left')])").extract_first()
        date = response.xpath("//div[contains(@class, 'emp-date-bar-main')]/p/text()").extract_first()
        item['content'] = content
        item['date'] = date
        yield item
