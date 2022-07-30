# CSCI 381
# Summer 2022
# Homework Chapter 12 - 12.16
# Gabriel Rubio Alvarado

"""(Project: Who Authored the Works of Shakespeare) Using the spaCy
similarity detection code introduced in this chapter, compare Shakespeare’s Macbeth to one major
work from each of several other authors who might have written Shakespeare’s works (see
https://en.wikipedia.org/wiki/Shakespeare_authorship_question). Locate works
on Project Gutenberg from a few authors listed at https://en.wikipedia.org/wiki/
List_of_Shakespeare_authorship_candidates, then use spaCy to compare their works’
similarity to Macbeth. Which of the authors’ works are most similar to Macbeth?"""

import spacy

from pathlib import Path

nlp = spacy.load("en_core_web_md")

doc1 = nlp(Path('macbeth.txt').read_text())
doc2 = nlp(Path('hamlet.txt').read_text())
doc1.similarity(doc2)