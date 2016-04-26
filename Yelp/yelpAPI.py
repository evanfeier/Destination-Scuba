from yelpapi import YelpAPI
import argparse
from pprint import pprint
import json
from sets import Set

yelp_api = YelpAPI('HT2dPycSfSpTHWsyqt95wQ', 'uBi1MMxW4HbJn7sumEie9oLK3Jw', '2sgcGgH_Gs9UlKVQfY8uqte0lhjSpE8z', '2tItNfdQoaHzpqqh1WGJmaG85F0')

with open('location_all_latlngs.txt') as data_file:    
    location_latlngs = json.load(data_file)
with open('location_counts.txt') as data_file:    
    location_counts = json.load(data_file)

full_data = []
urls = Set()
business_keys = ["url", "rating", "review_count", "name", "location"]

for i in range(51, len(location_counts)): #0-50 already done.
#for i in range(4, 5):
    for index, ll in enumerate(location_latlngs.get(location_counts[i][0], [])):
        pass
        if index <= 20: #keep under 20
            try:
                response = yelp_api.search_query(term='scuba diving',  ll=ll)
                #full_data.append(response)
                for i in range(0, len(response['businesses'])):
                    if str(response['businesses'][i]['url']) not in urls:
                        business = response['businesses'][i]
                        business = { keep_key: response['businesses'][i][keep_key] for keep_key in business_keys }
                        # unwanted = set(business.keys()) - set(business_keys)
                        # for unwanted_key in unwanted: del business[unwanted_key] 
                        full_data.append(business)
                    urls.add(str(response['businesses'][i]['url']))
            except:
                pass
        
with open('yelp_full_data.txt', 'w') as outfile:
    json.dump(full_data, outfile)
with open('yelp_urls.txt', 'w') as outfile:
    json.dump(list(urls), outfile)