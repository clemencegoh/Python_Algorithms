"""
Given two strings, determine if they share a common substring.
A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring .
The words "be" and "cat" do not share a substring.

:input: "Hello", "World"
:output: "Yes"
"""


class TwoStringsSolution:
    def solve(self, s1, s2):
        """
        Concept:
            Look at character level
        """
        store = set([c for c in s1])
        for char in s2:
            if char in store:
                return "Yes"
        return "No"


test_cases = [
    ("hello", "world", "Yes"),
    ("hi", "world", "No"),
]

sol = TwoStringsSolution()
for t in test_cases:
    sol.solve(t[0], t[1])
