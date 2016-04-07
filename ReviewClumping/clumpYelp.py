#!/usr/bin/python -tt

import json
import math
import operator
import re

def tfIdf(data, minWordSize = 3):
  dTF = {}
  dF = {}
  for key, text in data.items():
    wordList = re.findall(r"[\w']+", text)
    dTF[key] = {}
    # 1 - Find the TF (term frequency)
    for word in wordList:
      # must be certain length
      if len(word) >= minWordSize:
        index = word.lower()
        # try to find the word's count
        val = dTF[key].get(index, 0)
        dTF[key][index] = val + 1
        # 2 - Find DF (doc frequency)
        # if new, add to DF
        if val == 0:
          val = dF.get(index, 0)
          dF[index] = val + 1
  # 3 - Calculate IDF (Inverse DF) = log( #docs / df )
  dFn = len(dTF)
  for freq in dF:
    dF[freq] = math.log10(dFn / dF[freq])
  # 4 - Log-weight the TF and
  #      calculate the TF*IDF
  for key in dTF:
    for tf in dTF[key]:
      dTF[key][tf] = (1 + math.log10(dTF[key][tf])) * dF.get(tf, 0)
  # 5 - Normalize the TF*IDF
  for key in dTF:
    dNorm = 0
    # Sum the squares
    for tf in dTF[key]:
      dNorm += (dTF[key][tf]*dTF[key][tf])
    dNorm = math.sqrt(dNorm)
    # Normalize
    for tf in dTF[key]:
      dTF[key][tf] = dTF[key][tf] / dNorm
  return dTF


# Reads files and prints the most common words of size n
def main():
  lists = {}
  with open('yelpReviewsCombined.json') as data_file:    
    data = json.load(data_file)
    lists = tfIdf(data)
  top5 = {}
  for key, words in lists.items():
    sortedScores = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    words = []
    for word, score in sortedScores[:5]:
      words.append(word)
    top5[key] = words

  print top5

  with open('yelpReviewsTop5.json', 'w') as outfile:
      json.dump(top5, outfile)

  return

if __name__ == '__main__':
  main()