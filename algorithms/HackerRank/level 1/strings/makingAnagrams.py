"""
Alice is taking a cryptography class and finding anagrams to be very useful.
We consider two strings to be anagrams of each other if the first string's letters can be
rearranged to form the second string. In other words, both strings must contain the same exact letters
in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption
is dependent on the minimum number of character deletions required to make the two strings anagrams.
Can you help her find this number?

Given two strings, a and b, that may or may not be of the same length, determine the minimum number of
character deletions required to make a and b anagrams.
Any characters can be deleted from either of the strings.

For example, if a=cde and b=dcf,
we can delete e from string a and f from string b so that both remaining
strings are cd and dc which are anagrams.

:input: cde, abc
:output: 4
"""


class MakingAnagramsSolution:
    def solve(self, a, b):
        """
        Concept:
            Anagrams, not palindrome.
            Can simply use dictionary
        """
        a_dict = {}
        b_dict = {}
        counter = 0

        for item in a:
            a_dict.setdefault(item, 0)
            a_dict[item] += 1
        for item in b:
            if item not in a_dict:
                counter += 1
            else:
                b_dict.setdefault(item, 0)
                if b_dict[item] >= a_dict[item]:
                    counter += 1
                else:
                    b_dict[item] += 1
        for item in a:
            if item not in b_dict:
                counter += 1
            else:
                if a_dict[item] > b_dict[item]:
                    counter += a_dict[item] - b_dict[item]
                    a_dict[item] = b_dict[item]

        return counter
        
 
test_cases = [
    ('cde', 'abc', 4),
    ('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke', 30)
]

sol = MakingAnagramsSolution()
for t in test_cases:
    print(sol.solve(t[0],t[1]))
    print(t[2])
