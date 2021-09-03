"""
Post codes generator:
Accepts 2 strings "79-900" i "80-155" and returns list of codes in between.
How it works:
- changes the strings into int.
- calculates range of codes to generate
- basic checks which value is greater: first or last value - and if it is ok to perform actions.
- changes int into strings with '-' as separator
- makes a list of all available codes
"""


def post_code_generator():
    code_first = "79-900"
    code_last = "80-155"

    first_digit = code_first.split("-")
    first_digit = int(first_digit[0] + first_digit[1])

    last_digit = code_last.split("-")
    last_digit = int(last_digit[0] + last_digit[1])

    if first_digit > last_digit:
        return (
            f"Wpisany zakres jest błędny. \n"
            f"Pierwszy numer: {code_first} zaś koniec to: {code_last}. "
            f"\nNIE WYKONANO DZIAŁAŃ"
        )

    elif first_digit == last_digit:
        return f"Lista zawiera tylko jeden zakres kodów pocztowych: {code_first}"

    else:
        list_of_codes = [code_first]
        index = 0
        dist = last_digit - first_digit

        while index < dist:
            first_digit += 1
            new_string = str(first_digit)
            added_one = new_string[:2] + "-" + new_string[2:]
            list_of_codes.append(added_one)
            index += 1
        return f"Liczba kodów w liście: {len(list_of_codes)}. \n Pozycje: {list_of_codes}"


print(post_code_generator())
