import sys
import json

def scoreText(scores, data):
    val = 0
    if "text" in data:
        strlist = data["text"].split(" ")
        for str in strlist:
            lstr = str.lower()
            if lstr in scores:
                val += scores[lstr]
    print val

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])	
    scores = {} # initialize an empty dictionary

    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        data = json.loads(line)
        scoreText(scores, data)


if __name__ == '__main__':
    main()
