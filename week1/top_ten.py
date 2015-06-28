from __future__ import division

import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    hashtags = {}

    # Parse tweet file
    for line in tweet_file:
        data = json.loads(line)
        if 'entities' in data and data['entities'] != None:
            if 'hashtags' in data['entities'] and data['entities']['hashtags'] != None:
                tags = data['entities']['hashtags']
                for tag in tags:
                    hashtag = tag['text'].encode('utf-8')
                    if hashtag not in hashtags:
                        hashtags[hashtag] = 0
                    hashtags[hashtag] += 1

    # print out top ten
    top_ten_tags = sorted(hashtags, key=hashtags.get, reverse=True)
    for tag in top_ten_tags[0:10]:
        print tag, hashtags[tag]
            

if __name__ == '__main__':
    main()
