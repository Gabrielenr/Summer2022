# CSCI 381
# Summer 2022
# Homework Chapter 9 - 9.10
# Gabriel Rubio Alvarado

"""(Project: Analyzing a Book from Project Gutenberg)
Create a script that reads Pride and Prejudice from a text file. Produce statistics about the
book, including the total word count, the total character count, the average word length
the average sentence length, a word distribution containing frequency counts of all words,
and the top 10 longest words. In the “Natural Language Processing (NLP)” chapter, you’ll
find lots of more sophisticated techniques for analyzing and comparing such texts.
Each Project Gutenberg e-book begins and ends with some additional text, such as
licensing information, which is not part of the e-book itself. You may want to remove
that text from your copy of the book before analyzing its text """

from itertools import count
from collections import Counter


filename = "pride_and_prejudice.txt"
with open(filename, encoding='utf8') as f:
    doc = f.read()

ten_large = 10
words = doc.split()
words_length = len(words)
print('Words count :', words_length)


def count_chars(doc_chars):
    result = 0
    for char in doc_chars:
        result += 1
    return result


def average_word_count(words_in_doc):
    average_word = sum(len(words_in_speech) for words_in_speech in words_in_doc) / len(words_in_doc)
    return average_word


def average_sentence_len(doc_sentences):
    sentence = doc_sentences.split('.')
    average_sentence = sum(len(x) for x in sentence) / len(sentence)
    return average_sentence


# Top 10 longest words
def longest_word(words, ten_large):
    cnt = count()
    return sorted(words, key=lambda w: (len(w), next(cnt)), reverse=True)[:ten_large]


# Word distribution of all words
words2 = []
for word in words:
    if word not in words2:
        words2.append(word)
for i in range(0, len(words2)):
    print('Distribution of', words2[i], 'is :', words.count(words2[i]))


print('Characters count :', count_chars(doc))
print('Average word length : ', average_word_count(words))
print('Average sentence length :', average_sentence_len(doc))
print('Top 10 longest words :', longest_word(words, ten_large))
