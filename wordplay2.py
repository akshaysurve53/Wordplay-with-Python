import scrabble
import string

#printing the word which contains double uu in that.
for word in scrabble.wordlist:
    if "uu" in word:
        print(word)