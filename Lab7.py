"""
CS2302
Lab 7
Purpose: Edit Distance
Created on Mon Dec 2, 2019
Diego Aguirre
@author: Nancy Hernandez
"""


def edit_distance(word1, word2, a, b):
    # If first letter in word 1 is None
    if a == 0:
        return b
    # If first letter in word 2 is None
    if b == 0:
        return a
    # If letters are the same
    if word1[a - 1] == word2[b - 1]:
        return edit_distance(word1, word2, a - 1, b - 1)
    # If letters are not the same
    return min(edit_distance(word1, word2, a, b - 1), edit_distance(word1, word2, a - 1, b),
               edit_distance(word1, word2, a - 1, b - 1)) + 1


# Users input
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
print()

# Gets final number of changes made to fully change into other word
total = edit_distance(word1, word2, len(word1), len(word2))

print("The edit distance for the strings", word1, "and", word2, "is:", total)
