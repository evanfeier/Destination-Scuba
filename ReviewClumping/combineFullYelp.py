#!/usr/bin/python -tt

import json
import math
import operator

# Reads files and prints the most common words of size n
def main():
  businessDict = {}
  with open('yelpFull.json') as data_file:    
    data = json.load(data_file)
    for region in data:
      for business in region["businesses"]:
        link = ""
        try:
          index = business["url"].index('?')
          link = business["url"][:index]
        except ValueError:
          link = business["url"]
        if (businessDict.get(link, 0) == 0) :
          businessDict[link] = business
  businesses = businessDict.values()

  reviewsAgg = {}
  with open('yelpReviewsTop5.json') as data_file:  
    try:
      reviewsAgg = json.load(data_file)
    except ValueError:
      pass

  full = []
  for business in businesses:
    item = {}
    link = ""
    try:
      index = business["url"].index('?')
      link = business["url"][:index]
    except ValueError:
      link = business["url"]
    
    item["link"] = link

    try:
      item["rating"] = str(business["rating"])
    except KeyError:
      item["rating"] = ""

    try:
      item["reviewnum"] = str(business["review_count"])
      item["ratingnum"] = str(business["review_count"])
    except KeyError:
      item["reviewnum"] = "0"
      item["ratingnum"] = "0"

    try:
      item["title"] = business["name"]
    except KeyError:
      item["title"] = ""

    try:
      location = business["location"]
      try:
        address = location["display_address"]
        total = ""
        for part in address:
          total = total + part + " "
        item["location"] = total
      except KeyError:
        item["location"] = ""
      try:
        item["lat"] = str(location["coordinate"]["latitude"])
        item["lng"] = str(location["coordinate"]["longitude"])
      except KeyError:
        item["lat"] = ""
        item["lng"] = ""
    except KeyError:
      item["title"] = ""

    item["reviewtext"] = reviewsAgg.get(link, [])
    full.append(item)

  with open('yelpFullWithReviews.json', 'w') as outfile:
      json.dump(full, outfile)

  return

if __name__ == '__main__':
  main()