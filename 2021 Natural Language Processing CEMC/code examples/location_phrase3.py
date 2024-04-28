"""
Token Matching with Repetation example to extract locations from text.

Sam Scott, Mohawk College, 2021
"""
import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

pattern = [
    {"LEMMA": "go"},
    {"LOWER": {"IN": ["to", "into", "toward"]}},
    {"POS": "DET"},
    {"POS": {"IN": ["ADJ", "PUNCT"]}, "OP": "*"},
    {"POS": "NOUN"}
]

matcher.add("location phrase", [pattern])

doc = nlp("We went to the store. Brody is going to go to a library. It all depends on whether she goes to the stadium. When are you going into that salon? They went into the red building and didn’t come out. I saw them go into the ugly, red building and then leave.")

matches = matcher(doc)

locations = []
for match_id, start, end in matches:
    locations.append(doc[start+2:end])
print(locations)
