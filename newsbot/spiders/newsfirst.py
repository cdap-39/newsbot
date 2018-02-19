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
        # for news in response.css('div.sub-1-news-block'):
        #     headings.append({
        #         'heading': news.css('div.sub-1-news-heading>h2::text').extract_first()
        #     })

    # Parse content of the news article
    def parse_content(self, response):
        item = response.meta['item']
        item['content'] = 'content'
        yield item
