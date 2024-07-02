"""
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once.
For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check – treat them as non-existent
Test your code using the data we've provided.


Test Data
Sample input:
Listen
Silent
Sample output:
Anagrams

Sample input:
modern
norman
Sample output:
Not anagrams
"""


def anagrams(x, y):
	i = [ord(ch) for ch in x]
	j = [ord(ch) for ch in y]
	return "Anagrams" if sorted(i) == sorted(j) else "Not anagrams"


first_word = input().lower()
second_word = input().lower()
print(anagrams(first_word, second_word))
