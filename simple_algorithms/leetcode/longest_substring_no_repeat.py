"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Planning:
- Brute force involves iterating through, O(n^2) complexity.
    - Iterates through list once
        - For each item, iterate through again to keep track of longest sequence
- Refined: O(n) complexity
    - Since no repeat, a set can be used to keep track of previously seen
    - variables needed: longest_string(int), current_length(int), seen_set (set), left_pointer, right_pointer
        - First case: Simple, no repeats
            - return length of string
        - Second case: All repeats
            - return 1
        - Third case: Mixed
            - iterate until first repeat is found, save length.
            - move left pointer until char @left == char @right.
                - This will remove all unneeded checks
            - move right pointer and repeat
        - Possible cases:
            "abcbdac"
            "bbbbbbb"
            "abcdefg"
            ""
            " "
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set = set()
        longest_string = 0
        left_pointer = 0

        for right_pointer in range(len(s)):
            if s[right_pointer] not in seen_set:
                seen_set.add(s[right_pointer])
            else:
                while s[left_pointer] != s[right_pointer]:
                    seen_set.remove(s[left_pointer])
                    left_pointer += 1
                left_pointer += 1  # set left as next index

            # catch single char, and no repeats
            longest_string = max(longest_string, right_pointer - left_pointer + 1)
        return longest_string


