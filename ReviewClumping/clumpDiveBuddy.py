#!/usr/bin/python -tt

import json
import math
import operator
import re

def tfIdf(data, minWordSize = 3):
  dTF = {}
  dF = {}
  wordLists = []
  biwordList = []
  for item in data:
    #print item
    wordList = re.findall(r"[a-zA-Z]+", item["reviewtext"])
    wordLists.append(wordList)
    key = item["link"]
    dTF[key] = {}
    # 1 - Find the TF (term frequency)
    for word in wordList:
      # must be certain length
      if len(word) >= minWordSize:
        index = word.lower().title()
        # try to find the word's count
        val = dTF[key].get(index, 0)
        dTF[key][index] = val + 1
        # 2 - Find DF (doc frequency)
        # if new, add to DF
        if val == 0:
          val = dF.get(index, 0)
          dF[index] = val + 1
    # Biwords
    for i in range(len(wordList) - 1):
      # must be certain length
      if len(wordList[i]) >= minWordSize and len(wordList[i+1]) >= minWordSize:
        index = ( wordList[i].lower() + " " + wordList[i+1].lower() ).title()
        # try to find the word's count
        val = dTF[key].get(index, 0)
        dTF[key][index] = val + 1
        # 2 - Find DF (doc frequency)
        # if new, add to DF
        if val == 0:
          val = dF.get(index, 0)
          dF[index] = val + 1
          biwordItem = [key, index]
          biwordList.append( biwordItem )
        i += 1
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
  #combine word scores for biwords
  for biword in biwordList:
    words = re.findall(r"[a-zA-Z]+", biword[1] )
    for word in words:
      dTF[ biword[0] ][ biword[1] ] += dTF[ biword[0] ][ word ]
    dTF[ biword[0] ][ biword[1] ] /= ( len(words) + 1 )
  #keep only highest clump or single word
  for biword in biwordList:
    words = re.findall(r"[a-zA-Z]+", biword[1] )
    keepClump = True
    for word in words:
      try:
        if dTF[ biword[0] ][ biword[1] ] < dTF[ biword[0] ][ word ]:
          keepClump = False
      except KeyError:
        pass
    if keepClump:
      for word in words:
        try:
          del dTF[ biword[0] ][ word ]
        except KeyError:
          pass
    else:
      try:
        del dTF[ biword[0] ][ biword[1] ]
      except KeyError:
        pass
  return dTF


# Reads files and prints the most common words of size n
def main():
  lists = {}
  data = []
  with open('diveBuddyFinal.json') as data_file:    
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
  for item in data:
    item["reviewtext"] = top5[ item["link"] ]

  with open('diveBuddyTop5.json', 'w') as outfile:
    json.dump(data, outfile)

  return

if __name__ == '__main__':
  main()
