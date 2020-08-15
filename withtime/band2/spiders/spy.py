import scrapy
import json
from ..items import Band2Item

base="https://www.bandsintown.com/upcomingEvents?came_from=257&hide_homepage=true&sort_by_filter=Number+of+RSVPs&page=2&latitude=40.7128&longitude=-74.006"
class BandSpider(scrapy.Spider):
    name = 'band'

    start_urls = [base]

    def parse(self, response):
        items = Band2Item()
        data=response.json()

        for event in data["events"]:

            artist= event["artistName"]
            starttime= event["streamStart"]
            date=event["eventDate"]
            if 'streamEnd' not in event:

                endtime="--------"
            else:
                endtime=event["streamEnd"]
            timezone=event["timezone"]






            items["artist"]=artist
            items["starttime"] = starttime[-8:]
            items["endtime"] = endtime[-8:]
            items["timezone"] = timezone



            yield items


        nextpage=data["urlForNextPageOfEvents"]
        if nextpage:
            yield scrapy.Request(nextpage)