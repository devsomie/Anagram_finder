# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    word1 = input("First word: ")
    word2 = input("Second word: ")
    if sorted(word1) == sorted(word2):
       print("True")
    else:
       print("False")
find_anagrams('word1', 'word2')

