from __future__ import division

import sys
import json


def main():
    tweet_file = open(sys.argv[1])

    # Parse tweet file
    tcount = 0
    terms = {}
    for line in tweet_file:
        data = json.loads(line)
        if "text" in data:
            tweet = data['text'].lower().encode('utf-8').split()
            tcount += 1
            for word in tweet:
                if word.isalnum():
                    if word in terms:
                        terms[word] += 1
                    else:
                        terms[word] = 1

    for word in sorted(terms, key=terms.get):
        print word, terms[word]/tcount
            

if __name__ == '__main__':
    main()
