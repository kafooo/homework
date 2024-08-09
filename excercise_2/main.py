import argparse
import re

def count_words(filename):
    '''Counts the occurence of each word in a text file'''
    with open(filename, 'r') as f:
        result = re.findall(r'\w+', f.read())
        counted_words = {}
        for word in result:
            if word not in counted_words:
                counted_words[word]=result.count(word)
        for count, word in sorted(counted_words.items(), key = lambda x: x[1], reverse=True):
            print(f"{count} {word}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    count_words(args.file)