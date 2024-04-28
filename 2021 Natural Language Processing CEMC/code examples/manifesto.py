"""
Solutions to the exercises from the "Extracting Linguistic Knowledge" handout.

Sam Scott, Mohawk College, 2021
"""

## Load Language Model
import spacy
nlp = spacy.load("en_core_web_sm")
print("language model loaded")

## Load Text
text = ""
with open("manifesto.txt", encoding="utf-8") as file:
    for line in file:
        text += line;
print("text loaded")

## Run Pipeline
doc = nlp(text)
print("pipeline finished")

## Count Tokens
pos_counts = {}
for token in doc:
    try:
        pos_counts[token.pos_] += 1
    except:
        pos_counts[token.pos_] = 1

print(len(doc),"tokens")

## Number of Unique Tokens and Lemmas
lemmas = set()
vocab = set()
for token in doc:
    lemmas.add(token.lemma_)
    vocab.add(token.text)

print(len(vocab),"unique tokens")
print(len(lemmas),"unique lemmas")

## POS Tags
sorted(pos_counts)
for key in sorted(pos_counts):
    print(key,pos_counts[key])

## Longest Noun Chunk
longestnp = ""
countnp = 0
for np in doc.noun_chunks:
    countnp += 1
    if len(np.text) > len(longestnp):
        longestnp = np.text
print("number noun chunks:",countnp)
print("longest noun chunk:",longestnp)

## Longest Entity
longestent = doc.ents[0]
for ent in doc.ents:
    if len(ent.text) > len(longestent.text):
        longestent = ent
print("number entities:",len(doc.ents))
print("longest entity:",longestent.text, longestent.label_)


