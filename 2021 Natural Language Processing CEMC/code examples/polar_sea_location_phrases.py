"""
A test of an expanded version of the location phrase pattern from
class using the novel "The Open Polar Sea", downloaded from
https://gutenberg.org

Sam Scott, Mohawk College, 2021
"""

## Load Language Model
import spacy
nlp = spacy.load("en_core_web_sm")
print("language model loaded")

## Load Text
text = ""
with open("PolarSea.txt", encoding="utf-8") as file:
    for line in file:
        text += line;
print("text loaded")

## Run Pipeline
doc = nlp(text)
print("pipeline finished")

## Find Location Phrases
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

pattern = [
    {"LEMMA": {"IN": ["go", "travel", "sail", "drive", "fly", "journey", "walk"]}},
    {"LOWER": {"IN": ["to", "into", "toward", "through", "around", "between", "under", "over"]}},
    {"POS": "DET"},
    {"POS": {"IN": ["ADJ", "PUNCT"]}, "OP": "*"},
    {"POS": "NOUN"}
]

matcher.add("location phrase", [pattern])

matches = matcher(doc)

locations = []
for match_id, start, end in matches:
    locations.append(doc[start+2:end])
print(locations)
