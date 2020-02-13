"""
Problem: 
    Given an array of numbers, the min number, and the max of the array,
    return an array of tuples containing the range of missing 
    numbers within the array

Example: 
    arr: [1, 3, 5, 10]
    min: 1
    max: 10
    :return: [(2,2), (4,4), (6,9)]
"""


class Solution:
    def __init__(self, arr: [int], min_num: int, max_num: int):
        self.arr = arr
        self.min_num = min_num
        self.max_num = max_num

    def setVariables(self, arr: [int], min_num: int, max_num: int):
        self.arr = arr
        self.min_num = min_num
        self.max_num = max_num

    def findAnswer(self):
        # Sort, O(NlogN)
        self.arr = sorted(self.arr)

        # set starting number, return array
        starting_num = self.min_num
        solution = []

        # loop through arr to determine what the next number is, O(N)
        for i in range(len(self.arr)):
            if starting_num != self.arr[i]:
                solution.append((starting_num, self.arr[i] - 1))
            starting_num = self.arr[i] + 1

        return solution


s = Solution([3, 20, 1, 5, 10, 12, 15], 1, 20)
print(s.findAnswer())
