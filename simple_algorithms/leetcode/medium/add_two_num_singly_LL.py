"""
# Complete

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

Workings:
    - Bruteforce way: iterate through each O(n) complexity
        - init 2 pointers, create carry variable
        - Create new linked list, add and carry
        - Cases to consider:
            - l1 [9,9,9,9], l2 [0]
            - l1 [9,9,9], l2 [1]
            - l1 [1,8,7], l2 [2,3,3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0

    summation = l1.val + l2.val

    current_node = ListNode((summation % 10) + carry)
    start_node = current_node

    if summation >= 10:
        carry = 1

    while l1.next is not None:
        l1 = l1.next
        l2 = l2.next

        if l1 is None:
            l1_val = 0
        else:
            l1_val = l1.val
        if l2 is None:
            l2_val = 0
        else:
            l2_val = l2.val

        summation = l1_val + l2_val

        current_node.next = ListNode((summation % 10) + carry)
        current_node = current_node.next

        if summation >= 10:
            carry = 1

    return start_node
