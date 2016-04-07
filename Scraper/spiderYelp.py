import scrapy
import re
import HTMLParser
import json

class StackOverflowSpider(scrapy.Spider):
    urls = []
    with open('newYelpList.txt') as data_file:    
        urls = json.load(data_file)

    name = 'yelp'
    start_urls = urls
    #start_urls = ["http://www.yelp.com/biz/dive-and-recreation-center-avalon", "http://www.yelp.com/biz/hawaii-convertible-tours-waipahu", "http://www.yelp.com/biz/daveys-dive-buddies-kihei", "http://www.yelp.com/biz/oahu-private-scuba-diving-tours-honolulu", "http://www.yelp.com/biz/big-kahuna-water-sports-honolulu", "http://www.yelp.com/biz/reef-pirates-diving-honolulu"]

    def parse(self, response):
        reviewnum = 0
        reviewtext = ""
        reviewnums = response.css('span[itemprop^=reviewCount]::text').extract()
        reviews = response.css('p[itemprop^=description]::text').extract()
        if reviewnums:
            reviewnum = int(reviewnums[0].encode('utf8'))
            #count = 20
            #while count < reviewnum:
            #    print str(count) + " " + str(reviewnum)
            #    f = open('newYelpList.txt','a')
            #    f.write( response.url+"?start="+str(count)+"\n" )
            #    f.close()
            #    count = count + 20
        if reviews:
            for review in reviews:
                reviewtext += review.encode('utf8')
                reviewtext += " "

        yield {
            'reviewtext': reviewtext, 
            'reviewnum': reviewnum,
            'link': response.url,
        }