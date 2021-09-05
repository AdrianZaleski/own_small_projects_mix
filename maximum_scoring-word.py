"""
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
"""

test_string = "man i need a taxi up to ubud"
test_string2 = "aa ba c"


def winnig(test_string):
    winning_word = ""
    max_score = 0

    # Make a split of the string
    for word in test_string.split():
        score = 0
        # Check each word separately and count its value
        # ord('a')+1 could be changed for 96 but it is better to understand what is happening
        for letter in word:
            score += ord(letter) - ord("a") + 1

        if score > max_score:
            max_score = score
            winning_word = word

    return f"Maximum score is {max_score} for the word: {winning_word}"


print(winnig(test_string))
print(winnig(test_string2))
