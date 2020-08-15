# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Band2Item(scrapy.Item):
    # define the fields for your item here like:
    artist = scrapy.Field()
    starttime = scrapy.Field()
    endtime = scrapy.Field()
    timezone = scrapy.Field()

