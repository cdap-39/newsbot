# -*- coding: utf-8 -*-
import scrapy


class NewsItem(scrapy.Item):
    heading = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
