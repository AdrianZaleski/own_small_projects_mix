"""
Program for changing letters from text into numbers
"""


def alphabet_position(text):
    numbers = []
    for letter in text:
        if letter.isalpha():
            letter_smaller = letter.lower()
            # Using ord('a')+1 as setting value for 1 - not to use -96 as magic value.
            number = ord(letter_smaller) - ord('a')+1
            numbers.append(number)
    else:
        pass
    return " ".join(str(num) for num in numbers)


text = "The sunset sets at twelve o' clock."

print(alphabet_position(text))
print(alphabet_position("1015792501"))
