import scrabble
import string
#print all letter which does not apper twice in eng word from dict.
for letter in string.ascii_lowercase:
    exits=False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            exits=True
            break
    if not exits:
        print("there is no english word with double "+letter)