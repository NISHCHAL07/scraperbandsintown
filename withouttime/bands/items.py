# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BandsItem(scrapy.Item):

    artist = scrapy.Field()
    Titleofevent = scrapy.Field()
    date=scrapy.Field()
    linkofstream = scrapy.Field()
    fb = scrapy.Field()
    geners = scrapy.Field()
    poster = scrapy.Field()





