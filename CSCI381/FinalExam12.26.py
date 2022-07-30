"""Exercise 12.26
We get the first synonym of the word 'true' by calling on the function FirstSynonym
we then recursively call on the function again to find the synonym of the synonym we first obtained.
We continue this loop until we find the antonym, once we do, we print out the chain"""

from nltk.corpus import wordnet

synonyms = []
antonyms = []
initial_word = "good"


def FirstSynonym(word):
    j = 0
    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())
            if i.antonyms():
                antonyms.append(i.antonyms()[0].name())


def FindAntonym(word):
    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            if i.antonyms():
                antonyms.append(i.antonyms()[0].name())


FirstSynonym(initial_word)
FindAntonym(initial_word)

first_synonym = synonyms[0]
first_antonym = antonyms[0]
print(set(synonyms))
print(set(antonyms))
