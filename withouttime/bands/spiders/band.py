# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import BandsItem

base="https://www.bandsintown.com/upcomingEvents?came_from=257&hide_homepage=true&sort_by_filter=Number+of+RSVPs&page=2&latitude=40.7128&longitude=-74.006"
class BandSpider(scrapy.Spider):
    name = 'band'
    start_urls = [base]

    def parse(self, response):
        data=response.json()
        for event in data["events"]:
            link = event["eventUrl"]
            yield scrapy.Request(url=link,callback=self.parse_event)

        nextpage=data["urlForNextPageOfEvents"]
        if nextpage:
            yield scrapy.Request(nextpage)

    def parse_event(self,response):
        items = BandsItem()
        linkofstream=response.css("._3pDnyehMrLDxx4M3COJ0nI::text").get()
        artistname=response.css('._2ewREFNd4qGa6u_PLBCY9F::text').get()
        title=response.css('._31N2YODa7GUJWZgNSc_AWl::text').get()
        date=response.css('._2AQUG7DvnqofhtG3Q5YTSm::text').get()
        fb = response.css('._3EAC_52CXB3SEGlNmW1zZM a::attr(href)').get()
        geners = response.css('._1Se_dqLEba70e_1AFsdzO3 ._1v6hYzlTV-hB2ZkAb6CiCv::text').get()
        poster = response.css('._3FxoLllHIYDsTLMcW1mAl8 img::attr(src)').get()

        items["artist"] = artistname
        items["Titleofevent"] = title
        items["date"]=date
        items["fb"] = fb
        items["geners"] = geners
        items["poster"]=poster
        items["linkofstream"]=linkofstream



        yield items










