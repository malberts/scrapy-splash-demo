# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class Track(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    user = scrapy.Field()
    tag = scrapy.Field()
    likes = scrapy.Field()
    url = scrapy.Field()


class TrackItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
