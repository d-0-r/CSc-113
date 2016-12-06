#!/usr/bin/python3

__author__ = "Dor Rondel"
__session__ = "9:30am"

class Word:
    VOWELS = "AEIOU"
    CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZ"

    def __init__(self):
        ''' Constructor for class '''
        self.word = input("Enter a word to be analyzed:\t")
        self.analysis(self.word)

    def analysis(self, word):
        ''' Prints string with amount of vowels and consonants in word argument '''
        v_count = 0
        c_count = 0
        for i in word.upper():  # letter-case is irrelevant,
            if i in self.VOWELS:
                v_count += 1
            elif i in self.CONSONANTS:
                c_count += 1
            else:  # in case of number or non-latin-letter character
                pass
        print("{} has {} vowels and {} consonants".format(word, v_count, c_count))

# Test class
if __name__ == "__main__":
    print("Test:\n----- ")
    t1 = Word()
