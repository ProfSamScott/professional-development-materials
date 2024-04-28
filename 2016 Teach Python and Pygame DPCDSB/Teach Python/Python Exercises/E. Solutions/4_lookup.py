def lookup(word,page):
    """ word is the word you are looking for, page is the word at the top
    of the current dictionary page. Note: case must match or this won't work!"""
    if word<page:
        print("Search backwards!")
    if word>page:
        print("Search forwards!")
    if word==page:
        print("You found it!")
