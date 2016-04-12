import json

with open("diveBuddyCompleteData.json") as data_file:    
        sites = json.load(data_file)
with open("yelpFullWithReviews.json") as data_file:    
        buss = json.load(data_file)
        
site_avg = 0
site_i = 0
buss_avg = 0
buss_i = 0
for site in sites:
    try:
        site_avg += float(site["rating"])
        site_i +=1
    except ValueError:
        pass
for bus in buss:
    try:
        buss_avg += float(bus["rating"])
        buss_i +=1
    except ValueError:
        pass    

print "Site Average Rating: " + str(site_avg/site_i)
print "Bussiness Average Rating: " + str(buss_avg/buss_i)