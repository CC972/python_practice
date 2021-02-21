import sys
from urllib.request import urlopen


# Run following in terminal:
# from words import *
# main("http://sixty-north.com/c/t.txt")


def fetch_words(url):

    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()

    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])  # Take in command-line argument