# -*- coding: utf-8 -*-
import scrapy


class NewsbotItem(scrapy.Item):
    heading = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
