##Finding Keywords within Reviews

These scripts find the keywords within the reviews.  They then store the top five keywords in a new JSON file along with the rest of the reviews.
It currently uses TFIDF for both single words and biwords.

**Yelp**

combineYelp.py is utilized before the keyword extraction.  It aggregates reviews from multiple Yelp page download into a single file, since we can only download reviews from a page in a chunk of 20 reviews.

Next, the clumping algorithm is run to find the top keywords.

combineFullYelp.py then allows data downloaded from the Yelp API to be combined with our review into a single json file.

**DiveBuddy**

This just utilizes the clumping algorithm to get the keywords from the reviews
