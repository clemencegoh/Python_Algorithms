"""
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.

For example, if the string s = 'abcac' and n=10,
the substring we consider is abcacabcac,
the first 10 characters of her infinite string.
There are 4 occurrences of a in the substring.

:input: s: aba n: 10
:output: 7
"""

import math

class RepeatedStringSolution:
    def solve(self, s: str, n: int):
        """
        Concept:
            Mathematically, this can be found by first finding number of a's
            in substring given.
            Then, if there is a remainder, count from there
        """
        substring_length = len(s)
        quotient = math.floor(n / substring_length)
        remainder = n % substring_length

        # count number of a's in substring
        num_a_in_substring = s.count('a')
        extra_count = 0
        if remainder != 0:
            extra_count = s[0:remainder].count('a')
        return num_a_in_substring * quotient + extra_count
        
 
sol = RepeatedStringSolution()
print(sol.solve('aba', 10))             # 7
print(sol.solve('a', 1000000000000))    # 1000000000000
