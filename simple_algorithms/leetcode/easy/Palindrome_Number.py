"""
# Complete

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


def isPalindrome(x: int) -> bool:
    # firstly, no negative integer is a palindrome
    if x < 0:
        return False
    if x < 10:
        return True
    # Also, no number that ends with 0 can be a palindrome
    if x % 10 == 0:
        return False

    # Revert back half of number
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x = x // 10
    return x == reverted or x == reverted // 10
