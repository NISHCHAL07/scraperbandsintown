# scraperbandsintown
Here I used scrapy for scraping the info of popular live streams in bandsintown,
Finally after running two scrapers two output csv's are generated named time and first,
First contains everything about the live stream except start and end times ,
Time contains the start and end time of the streams,
There are nearly 2200 items in this section ,
The reason for creating two sections is scrapy cant run two pipelines simultaneously,as time of stream is generated through javascript I used json request for scraping the data,so I used two scrapers to scrape the info 
