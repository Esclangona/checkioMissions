"""
Input: Two dates as tuples of integers.

Output: The difference between the dates in days as an integer.

"""
from datetime import date

def days_diff(a, b):
    first_date = date(a[0],a[1],a[2])
    second_date = date(b[0],b[1],b[2])
    return (abs(first_date - second_date)).days

