"""
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string.

"""


def backward_string_by_word(text: str) -> str:
    word_list = text.split(" ")
    reversed_words = []
    for i in word_list:
        reversed_words.append(i[::-1])
        
    return " ".join(reversed_words)