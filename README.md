# Destination-Scuba
CSCE470 Project that recommends scuba diving sites and business. Each business and site with also have some defining keywords that are extracted from their reviews.

The main algorithm can be found in DS_retriever.py and in the folder ReviewClumping. The DS_retriever.py uses divebuddy and yelp data retrieved from each site, along with the review keywords generated in ReviewClumping to return the top n results in a location. For simplicity the algorithm return the rating, url, and review keywords, but for the actual website, more information will be returned.

To use DS_retriever.py you must type
python DS_retriever.py LATITUDE LONGITUDE N
Examples:
  python DS_retriever.py 44.338398 -75.919733 10
  python DS_retriever.py 26.448723 -80.066601 10 
  python DS_retriever.py 42.60132 -83.11994 10
