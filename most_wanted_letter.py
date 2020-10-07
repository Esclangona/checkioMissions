
"""
You are given a text, which contains different English letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the Latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

"""
def checkio(text: str) -> str:
    text = text.lower()
    
    
    alpha_list = []
    mwl = {}
    for i in text:
        if i.isalpha():
            count = text.count(i)
            mwl[i] = count
        

    counter = sorted(mwl.values(), reverse = True)
    if counter.count(counter[0]) == 1:
        fcounter = sorted(mwl.items(), key = lambda x : x[1], reverse = True)
        return fcounter[0][0]
    elif  counter.count(counter[0]) > 1:
        for k, v in mwl.items():
            if v == counter[0] and k.isalpha():
                alpha_list.append(k)
                alpha_list.sort()
        
    return alpha_list[0]