"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable

Output: Iterable

Example:

"""

import collections as c

def frequency_sort(items):
    final_list = []
    counter = c.Counter(items)
    sorted_list = sorted(counter.items(), key = lambda x : x[1], reverse = True)
    for k, v in sorted_list:
        for i in range(v):
            al.append(k)
    
    return final_list