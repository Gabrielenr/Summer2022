# CSCI 381
# Summer 2022
# Homework Chapter 9 - 9.11
# Gabriel Rubio Alvarado

"""(Project: Visualizing Word Frequencies with a Word Cloud)
Using the techniques from the previous exercise, create a frequencies dictionary containing the
frequencies of the top-200 words in Pride and Prejudice. Then execute the following statements to
generate a rectangular word cloud and save its image to a file on disk:
wordcloud = wordcloud.fit_words(frequencies)
wordcloud = wordcloud.to_file('PrideAndPrejudice.png')
You can then double-click the PrideAndPrejudice.png image file on your system to view
it. In the “Natural Language Processing” chapter, we’ll show you how to place your word
clouds into shapes. For example, we placed our Romeo and Juliet word cloud into a heart."""
from collections import Counter
from wordcloud import WordCloud
from itertools import count
import matplotlib.pyplot as plt

filename = "pride_and_prejudice.txt"
with open(filename, encoding='utf8') as f:
    doc = f.read()

word_dic = dict(Counter(doc.replace(',', '').replace('.', '').split()))
sorted_x = sorted(word_dic.items(), key=lambda kv: kv[1], reverse=True)

print(sorted_x)
# for key in sorted_x[:50]:
#     print(key, sorted_x[key])

# wordcloud = WordCloud(colormap='prism', background_color='white')
# wordcloud = wordcloud.fit_words(frequencies)
# wordcloud = wordcloud.to_file('PrideAndPrejudice.png')
