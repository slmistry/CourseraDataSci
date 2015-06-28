from __future__ import division

import sys
import json


def scoreText(scores, nwords, text):
    val = 0
    strlist = text.split(" ")
    for str in strlist:
        if str in scores:
            val += scores[str]
        elif str.isalpha():
            nwords.append(str)
    return val


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    new_words = []
	
	# Build sentiment dictionary
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    # Build tweets dictionary
    tweets = {}
    for line in tweet_file:
        data = json.loads(line)
        if "text" in data:
            text = data['text'].encode('utf-8').lower()
            tweets[text] = scoreText(scores, new_words, text)

    # first clean dictionary to avoid processing same word again
    # then score new words 
    new_words = set(new_words)
    for word in new_words:
        total = 0
        val = 0
        for tweet in tweets:
            if word in tweet:
                total += 1
                if tweets[tweet] > 0:
                    val += 1
                elif tweets[tweet] < 0:
                    val -= 1
        print word, ' ', val/total

if __name__ == '__main__':
    main()
