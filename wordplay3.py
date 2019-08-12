import scrabble

#code for finding wors having all vowels in Dict
vowels="aeiou"
def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word)