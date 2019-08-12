import scrabble

#code for finding longest palindrom in the Dist
longest=""

#Method 1
""" for word in scrabble.wordlist:

    is_palindrom=True
    for index in range(len(word)):
        if word[index]  != word[-(index+1)]:
            is_palindrom=False
    if is_palindrom and len(word)> len(longest):
         longest=word
print("Longest palimdrom in the dist:"+longest) """


#Method 2 easy one

for word in scrabble.wordlist:
    is_palindrom=True
    if list(word)==list(reversed(word)) and len(word)>len(longest):
        longest=word
print("Longest palimdrom in the dist:"+longest)

#Method 3 

""" for word in scrabble.wordlist:
    is_palindrom=True
    if word==word[::-1] and len(word)>len(longest):
        longest=word
print("Longest palimdrom in the dist:"+longest)
 """