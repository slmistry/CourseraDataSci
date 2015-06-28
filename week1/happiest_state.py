from __future__ import division

import sys
import json

def scoreText(scores, text):
    val = 0
    strlist = text.split()
    for str in strlist:
        if str in scores:
            val += scores[str]
    return val

def GetState(data):
    if data['place'] != None and data['place']['country_code'] == 'US':
        if data['place']['full_name'] != None:
            namelist = data['place']['full_name'].encode('utf-8').split()
            state = namelist[-1]
            if len(state) == 2:
                return data['place']['full_name'][-2:]
    return ""

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
	
	# Build sentiment dictionary
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    # Process tweets and build state_score dictionary
    state_score = {}
    for line in tweet_file:
        score = 0
        data = json.loads(line)
        if "text" in data:
            tweet = data['text'].encode('utf-8').lower()
            score = scoreText(scores, tweet)
            state = GetState(data)
            if state != "":
                if state not in state_score:
                    state_score[state] = []
                state_score[state].append(score)

    happiest = ""
    max = -100
    for state in state_score:
        val = sum(state_score[state])/len(state_score[state])
        if val > max:
            happiest, max = state, val
            
    print happiest

if __name__ == '__main__':
    main()
