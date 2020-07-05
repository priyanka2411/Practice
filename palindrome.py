#!/usr/bin/env python3
def is_palindrome(s):
    """returns true if given string s is palindrome otherwise false"""
    # by slicing string into two  halves and reversing other half and comparing it with another
    # omiting the middle character
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return j <= i

    """Algorithm 1"""
    """if s == reverse(s):
        return True
    else:
        return False
    
    n = len(s)
    """
    """algorithm 2
    if s[:n // 2] == reverse(s[n - n // 2:]):
        return True
    else:
        return False"""
    """algorithm 3"""


def reverse(s):
    """Returns Reverse of string s"""
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev


print(is_palindrome("kayaks"))
