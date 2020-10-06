"""
You need to count the number of digits in a given string.

Input: A Str.

Output: An Int.

"""


def count_digits(text: str) -> int:
    digit_count = 0
    for i in text:
        if i.isnumeric():
            digit_count += 1
            
    return digit_count
