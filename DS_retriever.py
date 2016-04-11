# this file is used to retrieve the top n scuba diving sites and businesses for a given longitude and latitude
# the top sites and business will include title, rating, # of reviews, keywords, URL, etc? TODO

# to use this, type into the command line "python DS_retriever.py LONGITUDE LATITUDE N"
# Examples: 
# python DS_retriever.py 44.338398 -75.919733 10
# python DS_retriever.py 26.448723 -80.066601 10 
import sys
from geolocation import GeoLocation
import json
import heapq
from pprint import pprint

def main():
    # with open("diveBuddyCompleteData.json") as data_file:    
    #     site_bus = json.load(data_file)
    # print site_bus[0]
    if len(sys.argv) != 4:
        print "you must enter 3 arguments! \n1. latitude\n2. longitude\n3. number of sites and business you want retrieved\n\nExample: python DS_retriever.py 10.2 11.5 25"
        sys.exit()
    latitude = float(sys.argv[1])
    longitude = float(sys.argv[2])
    n = int(sys.argv[3])
    
    (sites, businesses) = retrieve_top_n_sites_businesses(latitude, longitude, n, "highest rating")
    print "Top " + str(n) + " sites\n"
    pprint(sites)
    print "\nTop " + str(n) + " businesses\n"
    pprint(businesses)

def retrieve_top_n_sites_businesses(latitude, longitude, n, select):
    # 
    sites = top_n(latitude, longitude, n, "diveBuddyCompleteData.json", select)
    businesses = top_n(latitude, longitude, n, "yelpCompleteData.json", select)
    return sites, businesses

def top_n(lat, lng, n, file_name, select):
    distance = 72 # 72 kilometers ~ 45 miles
    min_lat, min_lng, max_lat, max_lng = find_bounds(lat, lng, distance)
    top_n = TopN(n)
    with open(file_name) as data_file:    
        site_buss = json.load(data_file)
    
    success = 0
    fail = 0
    for place in site_buss:
        try:
            if min_lat <= float(place["lat"]) <= max_lat:
                if min_lng <= float(place["lng"]) <= max_lng:
                    s = score(float(place["rating"]), float(place["reviewnum"]), select)
                    top_n.feed((s, place["link"]))
        except ValueError:
            pass
    return top_n.result()

def find_bounds(lat, lng, d):
    loc = GeoLocation.from_degrees(lat, lng)
    SW_loc, NE_loc = loc.bounding_locations(d)
    return (SW_loc.deg_lat, SW_loc.deg_lon, NE_loc.deg_lat, NE_loc.deg_lon)
    
def score(rating, num_reviews, select):
    if select == "highest rating":
        return rating
    if select == "most reviewed":
        return num_reviews
    if select == "custom":
        return rating*num_reviews #TODO make this a better custom function
        

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

if __name__ == "__main__": main()