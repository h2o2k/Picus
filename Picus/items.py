# -*- coding: utf-8 -*-
# Define here the models for your scraped items
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Here we are defining storage containers which will store the data we are gonna scrape using scrapys already existing objects, this is needed for database storage later on - Andrew

import scrapy
from scrapy.item import Item, Field

class PicusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    blurb = scrapy.Field()
    uploadtime = scrapy.Field()
    img = scrapy.Field()
