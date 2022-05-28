# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

first_word = str (input("What is the first word? "))
second_word = str (input("What is the second word? "))

first_word = first_word.lower()
second_word = second_word.lower()

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted (word) == sorted (anagram):
        return True
    else:
        return False
print (find_anagram (first_word, second_word))