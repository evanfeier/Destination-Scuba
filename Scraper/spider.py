import scrapy
import re
import HTMLParser


class StackOverflowSpider(scrapy.Spider):
    urls = []
    f = open('sitemap_divesites.xml','r')
    res = f.readlines()
    for d in res:
        data = re.findall('<loc>(http:\/\/.[^<]+)<\/loc>',d)
        for i in data:
            if i.endswith('/'):
                urls.append(i[:-1])
            else:
                urls.append(i)

    name = 'divebuddy'
    start_urls = urls
    #start_urls = ["http://www.divebuddy.com/divesite/2884/cook-island-australia/", "http://www.divebuddy.com/divesite/5915/audubon-aquarium-americas-new-orleans-la", "http://www.divebuddy.com/divesite/4486/dry-rocks-key-largo-key-largo-fl", "http://www.divebuddy.com/divesite/3033/ann-coleman-juneau-ak", "http://www.divebuddy.com/divesite/3029/zainab-wreck-united-arab-emirates", "http://www.divebuddy.com/divesite/3032/lima-rock-oman", "http://www.divebuddy.com/divesite/3031/aub-wall-lebanon", "http://www.divebuddy.com/divesite/3028/mariam-express-united-arab-emirates", "http://www.divebuddy.com/divesite/3023/1770-agnes-water-australia", "http://www.divebuddy.com/divesite/3022/kalithea-greece", "http://www.divebuddy.com/divesite/3021/madeira-wreck-two-harbors-mn", "http://www.divebuddy.com/divesite/3020/monti-cristi-dominican-republic-dominican-republic", "http://www.divebuddy.com/divesite/2679/david-w-mills-oswego-ny", "http://www.divebuddy.com/divesite/2676/black-rock-costa-rica", "http://www.divebuddy.com/divesite/2674/gordon-c-cookeporthole-wreck-costa-ricamd", "http://www.divebuddy.com/divesite/2672/h-buoy-wreck-southport-ncmd", "http://www.divebuddy.com/divesite/2671/schurz-morehead-city-nc", "http://www.divebuddy.com/divesite/2669/fenwick-shoals-point-pleasant-beach-njde", "http://www.divebuddy.com/divesite/2667/jakes-wreck-point-pleasant-beach-njdedede", "http://www.divebuddy.com/divesite/2666/bonaire-bonaire", "http://www.divebuddy.com/divesite/2665/lady-elliot-island-australia", "http://www.divebuddy.com/divesite/2664/scuba-jamaica-fdr-resort-jamaica", "http://www.divebuddy.com/divesite/2663/deliah-jamaicade", "http://www.divebuddy.com/divesite/2668/pattys-pitcher-wreck-point-pleasant-beach-njdede", "http://www.divebuddy.com/divesite/2518/maliko-gulch-maui-hi", "http://www.divebuddy.com/divesite/2516/fangiska-reef-destin-fl", "http://www.divebuddy.com/divesite/2513/u-853-block-island-ri", "http://www.divebuddy.com/divesite/2512/fajardo-puerto-rico", "http://www.divebuddy.com/divesite/2509/sunset-reef-house-reef-cayman-islands", "http://www.divebuddy.com/divesite/2507/anton-lizardo-mexico", "http://www.divebuddy.com/divesite/2506/veracruz-mexico", "http://www.divebuddy.com/divesite/2504/rockaway-south-haven-mi", "http://www.divebuddy.com/divesite/2502/sugarloaf-key-quarry-sugarloaf-key-fl", "http://www.divebuddy.com/divesite/2500/sistine-chapel-bahamas", "http://www.divebuddy.com/divesite/2499/tuna-alley-bahamas", "http://www.divebuddy.com/divesite/2497/chandler-hovey-marblehead-ma", "http://www.divebuddy.com/divesite/2464/crack-nw-point-providenciales-tci-turks-caicos-islands", "http://www.divebuddy.com/divesite/2422/richelieu-river-canada", "http://www.divebuddy.com/divesite/2420/indian-arm-canada", "http://www.divebuddy.com/divesite/2418/white-lake-lau-rd-montague-mi", "http://www.divebuddy.com/divesite/2417/white-lake-lakeside-inn-whitehall-mi", "http://www.divebuddy.com/divesite/2413/holbox-mexico", "http://www.divebuddy.com/divesite/2412/uss-hogan-dd-178-san-diego-ca", "http://www.divebuddy.com/divesite/2411/shark-hotel-providenciales-tci-turks-caicos-islands", "http://www.divebuddy.com/divesite/2410/football-field-pine-cay-tci-turks-caicos-islands", "http://www.divebuddy.com/divesite/2407/aquarium-west-providenciales-tci-turks-caicos-islands", "http://www.divebuddy.com/divesite/2406/whiteface-aka-anchor-or-spanish-anchor-turks-caicos-islands", "http://www.divebuddy.com/divesite/2404/driveway-west-caicos-tci-turks-caicos-islands", "http://www.divebuddy.com/divesite/2403/boat-cove-aka-rock-garden-west-caicos-tci-turks-caicos-islands", "http://www.divebuddy.com/divesite/2399/hopedale-canada", "http://www.divebuddy.com/divesite/2398/lake-belton-belton-tx", "http://www.divebuddy.com/divesite/2397/wakatobi-dive-resort-indonesia", "http://www.divebuddy.com/divesite/2396/negali-passage-aka-negale-pass-fiji", "http://www.divebuddy.com/divesite/2402/puerto-penasco-rocky-point-mexico", "http://www.divebuddy.com/divesite/2395/canyon-lake-new-braunfels-tx", "http://www.divebuddy.com/divesite/2400/cay-sal-bank-bahamas", "http://www.divebuddy.com/divesite/2394/manuel-antonio-national-park-costa-rica", "http://www.divebuddy.com/divesite/2393/lourds-camp-costa-ricany", "http://www.divebuddy.com/divesite/2392/merigui-archipelago-myanmar", "http://www.divebuddy.com/divesite/2391/plymouth-sound-united-kingdom", "http://www.divebuddy.com/divesite/2390/cesaria-israel", "http://www.divebuddy.com/divesite/2387/koh-haa-lagoon-thailand", "http://www.divebuddy.com/divesite/900/fort-worden-reef-port-townsend-wa", "http://www.divebuddy.com/divesite/896/hood-canal-bridge-port-gamble-wa", "http://www.divebuddy.com/divesite/895/fox-island-fox-island-wa", "http://www.divebuddy.com/divesite/824/heisler-park-picnic-beach-laguna-ca", "http://www.divebuddy.com/divesite/822/wood-cove-laguna-beach-ca", "http://www.divebuddy.com/divesite/821/moss-street-point-laguna-ca", "http://www.divebuddy.com/divesite/819/san-onofre-state-beach-san-onofre-ca", "http://www.divebuddy.com/divesite/825/divers-cove-laguna-ca", "http://www.divebuddy.com/divesite/748/coco-view-wall-honduras", "http://www.divebuddy.com/divesite/751/spooky-channel-honduras", "http://www.divebuddy.com/divesite/746/grey-ghost-panama-city-fl", "http://www.divebuddy.com/divesite/737/uss-strength-panama-city-fl", "http://www.divebuddy.com/divesite/733/cypress-spring-vernon-fl", "http://www.divebuddy.com/divesite/730/hole-in-wall-florida-springs-fl", "http://www.divebuddy.com/divesite/734/becton-spring-vernon-fl", "http://www.divebuddy.com/divesite/728/shangri-la-marianna-fl", "http://www.divebuddy.com/divesite/726/panther-canada", "http://www.divebuddy.com/divesite/725/dive-georgia-quarry-white-ga", "http://www.divebuddy.com/divesite/724/gilboa-quarry-gilboa-oh", "http://www.divebuddy.com/divesite/722/madison-blue-spring-lee-fl", "http://www.divebuddy.com/divesite/718/cow-spring-florida-springs-fl", "http://www.divebuddy.com/divesite/717/gunsmoke-tampa-st-petersburg-fl", "http://www.divebuddy.com/divesite/715/indian-shores-reef-tampa-st-petersburg-fl", "http://www.divebuddy.com/divesite/707/george-worthington-canada", "http://www.divebuddy.com/divesite/698/john-b-martin-canada", "http://www.divebuddy.com/divesite/696/r-tower-naples-fl", "http://www.divebuddy.com/divesite/688/mine-sweeper-naples-fl", "http://www.divebuddy.com/divesite/684/kidd-wreck-naples-fl", "http://www.divebuddy.com/divesite/689/naples-ledges-naples-fl", "http://www.divebuddy.com/divesite/667/bonnies-arch-cayman-islands", "http://www.divebuddy.com/divesite/666/orange-canyon-cayman-islands", "http://www.divebuddy.com/divesite/669/lake-denton-avon-park-sebring-fl", "http://www.divebuddy.com/divesite/668/north-west-point-cayman-islands", "http://www.divebuddy.com/divesite/395/splitville-cayman-islands", "http://www.divebuddy.com/divesite/394/briney-breezes-west-palm-beach-fl", "http://www.divebuddy.com/divesite/242/antilla-wreck-aruba", "http://www.divebuddy.com/divesite/237/mangel-halto-reef-aruba", "http://www.divebuddy.com/divesite/236/puerto-chiquito-aruba", "http://www.divebuddy.com/divesite/235/saveneta-beach-aruba", "http://www.divebuddy.com/divesite/128/brouwersdam-netherlands", "http://www.divebuddy.com/divesite/35/pulau-dayang-jetty-malaysia", "http://www.divebuddy.com/divesite/34/pulau-lang-malaysia", "http://www.divebuddy.com/divesite/33/raynors-rock-malaysia", "http://www.divebuddy.com/divesite/32/pinnicles-malaysia"]

    def parse(self, response):
        title = ""
        loc = ""
        rating = ""
        ratingnum = ""
        reviewnum = 0
        reviewtext = ""
        lat = ""
        lng = ""
        titles = response.css('#lblDiveSiteName::text').extract()
        locs = response.css('#lblLocation::text').extract()
        ratings = response.css('#lblRating::text').extract()
        ratingnums = response.css('#lblRatingTotal::text').extract()
        reviews = response.css('span[id^=dlComments_lblComment]::text').extract()
        coords = response.css('#divDiveSiteMap a[title^=Report]::attr(href)').extract()
        if titles:
            title = titles[0].encode('utf8')
        if locs:
            loc = locs[0].encode('utf8')
        else:
            locs = response.css('#lblLocation *::text').extract()
            if locs:
                loc = locs[0].encode('utf8')
        if ratings:
            rating = ratings[0].encode('utf8')
        if ratingnums:
            ratingnum = ratingnums[0].encode('utf8')
        if reviews:
            for review in reviews:
                reviewtext += review.encode('utf8')
                reviewtext += " "
        if coords:
            coord = coords[0][29:]
            firstcomma = coord.find(",")
            lat = coord[:firstcomma]
            coord = coord[firstcomma+1:]
            lng = coord[:coord.find(",")]
        print "\n" + str(title) + "\n" + str(loc) + "\n" + str(lat) + "\n" + str(lng) + "\n" + str(rating) + "\n" + str(ratingnum) + "\n" + str(reviewnum) + "\n" + str(reviewtext) + "\n"

        yield {
            'title': title,
            'location': loc,
            'lat': lat,
            'lng': lng,
            'rating': rating,
            'ratingnum': ratingnum,
            'reviewtext': reviewtext, 
            'reviewnum': reviewnum,
            'link': response.url,
        }