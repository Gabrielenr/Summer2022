# CSCI 381
# Summer 2022
# Homework Chapter 12 - 12.24
# Gabriel Rubio Alvarado

"""Investigate the summarize and keywords functions
from the Gensim library’s gensim.summarization module, then use them to summarize
text and extract the important words."""

from gensim.summarization import summarize, keywords
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections.abc import Mapping


url = "https://onefootball.com/en/news/update-on-the-future-of-this-barcelona-full-back-should-xavi-cut-him-loose-35546131"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

for script in soup(["script", "style"]):
    script.extract()    # rip it out

text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

print(summarize(text))
print(keywords(text))
