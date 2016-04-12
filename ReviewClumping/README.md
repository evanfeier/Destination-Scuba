##Finding Keywords within Reviews

These scripts find the keywords within the reviews.  They then store the top five keywords in a new JSON file along with the rest of the reviews.
It currently uses TFIDF for single words.  However, we will be working on making it better by adding biwords and other tactics to ensure good keywords are returned.

All of these scripts do not require arguments, but rather the files are hardcoded in the code to ensure proper order of execution.

**Yelp**

combineYelp.py is utilized before the keyword extraction.  It aggregates reviews from multiple Yelp page download into a single file, since we can only download reviews from a page in a chunk of 20 reviews.

Next, the clumping algorithm is run to find the top keywords.

combineFullYelp.py then allows data downloaded from the Yelp API to be combined with our review keywords into a single json file.

**DiveBuddy**

This just utilizes the clumping algorithm to get the keywords from the reviews
