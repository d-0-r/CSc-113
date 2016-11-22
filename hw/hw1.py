#!/usr/bin/python3

__author__ = "Dor Rondel"
__session__ = "9:30am"

first = input("Enter first word: ")
second = input("Enter second word: ")

one = "".join([i for i in first if i in first and i not in second])
two = "".join([i for i in second if i in second and i not in first])
three = "".join(set(one+two))

print("""Results:
--------

Characters in the first word and not in the second: {}
Characters in the second word and not in the first: {}
Distinct unique characters from both sequences: {}
""".format(one, two, three))
