# this file is used to retrieve the top n scuba diving sites and businesses for a given longitude and latitude
# the top sites and business will include title, rating, # of reviews, keywords, URL, etc? TODO

# to use this, type into the command line "python DS_retriever.py LONGITUDE LATITUDE N"

import sys

def main():
    if len(sys.argv) != 4:
        print "you must enter 3 arguments! \n1. longitude\n2. latitude\n3. number of sites and business you want retrieved\n\nExample: python DS_retriever.py 10.2 11.5 25"
        sys.exit()
    longitude = float(sys.argv[1])
    latitude = float(sys.argv[2])
    n = int(sys.argv[3])
    
    (sites, businesses) = retrieve_top_n_sites_businesses(longitude, latitude, n)

def retrieve_top_n_sites_businesses(longitude, latitude, n):
    # 
    
    return sites, businesses

if __name__ == "__main__": main()