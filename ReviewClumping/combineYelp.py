#!/usr/bin/python -tt

import json
import math
import operator

# Reads files and prints the most common words of size n
def main():
  reviews1 = []
  with open('yelpReviews2.json') as data_file:    
    reviews1 = json.load(data_file)

  reviewsAgg = {}
  with open('yelpReviewsAggregate.json') as data_file:  
    try:
      reviewsAgg = json.load(data_file)
    except ValueError:
      pass

  for review in reviews1:
    link = ""
    try:
      print str(review)
      index = review["link"].index('?')
      link = review["link"][:index]
    except ValueError:
      link = review["link"]
    text = review["reviewtext"]
    fullText = reviewsAgg.get(link, "") + text
    reviewsAgg[link] = fullText

  with open('yelpReviewsAggregate.json', 'w') as outfile:
      json.dump(reviewsAgg, outfile)

  return

if __name__ == '__main__':
  main()