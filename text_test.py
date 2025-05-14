import collections
import multiprocessing as mp
import re

# Reading a simple natural langugage file into memory
def process(line):
    print(line)


with open("natural-ln-data.txt") as f:
    data = f.readlines()
    for line in data:
        process(line)

def split_into_words(line):
    word_regex_improved = r"(\w[\w']*\w|\w)"
    word_matcher = re.compile(word_regex_improved)
    return word_matcher.findall(line)

process_corpus = []

with open("natural-ln-data.txt") as f:
    
    for line in f:
        process_corpus.extend(split_into_words(line))
process_corpus = [w.lower() for w in process_corpus]

print(process_corpus)

