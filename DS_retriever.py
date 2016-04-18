# this file is used to retrieve the top n scuba diving sites and businesses for a given longitude and latitude
# the top sites and business will include rating, keywords, and URL

# to use this, type into the command line "python DS_retriever.py LONGITUDE LATITUDE N"
# Examples: 
# python DS_retriever.py 44.338398 -75.919733 10
# python DS_retriever.py 26.448723 -80.066601 10 
# python DS_retriever.py 42.60132 -83.11994 10   

import sys
from geolocation import GeoLocation
import json
import heapq
from pprint import pprint

#remove when running with website stuff
def main():
    if len(sys.argv) != 4:
        print "you must enter 3 arguments! \n1. latitude\n2. longitude\n3. number of sites and business you want retrieved\n\nExample: python DS_retriever.py 10.2 11.5 25"
        sys.exit()
    latitude = float(sys.argv[1])
    longitude = float(sys.argv[2])
    n = int(sys.argv[3])
    
    (sites, businesses) = retrieve_top_n_sites_businesses(latitude, longitude, n, "most reviewed")
    print "**Top " + str(n) + " sites (within 45 miles)**\n"
    pprint(sites)
    print "\n**Top " + str(n) + " businesses (within 45 miles)**\n"
    pprint(businesses)

def retrieve_top_n_sites_businesses(latitude, longitude, n, select):
    sites = top_n(latitude, longitude, n, "diveBuddyCompleteData.json", select)     
    businesses = top_n(latitude, longitude, n, "yelpFullWithReviews.json", select)
    return sites, businesses

def top_n(lat, lng, n, file_name, select):
    distance = 72 # 72 kilometers ~ 45 miles
    min_lat, min_lng, max_lat, max_lng = find_bounds(lat, lng, distance)
    top_n = TopN(n)
    custom_select = 1 if file_name == "diveBuddyCompleteData.json" else 0 #only used if using "custom"
    with open(file_name) as data_file:    
        site_buss = json.load(data_file)
    
    for place in site_buss:
        try:
            if min_lat <= float(place["lat"]) <= max_lat:
                if min_lng <= float(place["lng"]) <= max_lng:
                    s = score(float(place["rating"]), float(place["reviewnum"]), select, custom_select)
                    title = place.get("title", "")
                    reviewtext = place.get("reviewtext", "")
                    location = place.get("location", "")
                    rating = int(float(place.get("rating", 0)))
                    top_n.feed((s, title, place["link"], reviewtext, location, rating, place["lat"], place["lng"]))
        except ValueError:
            pass
            
    return top_n.result()
        
def find_bounds(lat, lng, d):
    loc = GeoLocation.from_degrees(lat, lng)
    SW_loc, NE_loc = loc.bounding_locations(d)
    return (SW_loc.deg_lat, SW_loc.deg_lon, NE_loc.deg_lat, NE_loc.deg_lon)

# allows for different variations of scores    
def score(rating, num_reviews, select, custom_select):
    if select == "highest rating":
        return rating
    if select == "most reviewed":
        return num_reviews
    if select == "custom simple":
        return rating*num_reviews
    if select == "custom": # good when decent amount of reviews, > 50
        # averages were found using find_avg_rating.py
        if custom_select == 1: 
            avg = 3.83960619585 #divebuddy avg
        else:
            avg = 3.86466165414  #yelp avg
        m = 5 #min reviews to be considered
        return (num_reviews*rating + m*avg) / (num_reviews + m)

# container for heapq to limit the size to n
class TopN(object):
    # v format: (num, value)
    def __init__(self, N):
        self.N = N
        self.h = []        

    def feed(self, v):  
        if len(self.h) < self.N:
            heapq.heappush(self.h, v)
        else:
            heapq.heappushpop(self.h, v)

    def result(self):
        self.h.sort(reverse=True)
        return self.h

#remove when running with website stuff
if __name__ == "__main__": main()
