"""
Problem:
:given: An array of integers
:return: an array of indices on for the next largest number for each item in the
        given array.
        If none present, return -1
:example: [3, 2, 3, 6, 5, 9, 8]
:returns: [3, 2, 3, 5, 5, -1, -1]
"""


class FindNextLargest:
    def solution1(self, arr):
        """
        Native solution,
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        saved = []
        for pos1, i in enumerate(arr):
            for pos in range(pos1, len(arr)):
                if arr[pos] > i:
                    saved.append(pos)
                    break
            if len(saved) < pos1 + 1:
                saved.append(-1)
        return saved

    def solution2(self, arr):
        """
        Stack method
        Time complexity: O(n)
        Space complexity: O(n)
        """
        stack = [(0, arr[0])]
        solution = [-1] * len(arr)
        for pos, i in enumerate(arr):
            while True:
                if len(stack) == 0:
                    stack.append((pos, i))
                top = stack.pop()
                if i > top[1]:
                    solution[top[0]] = pos
                else:
                    stack.append(top)
                    stack.append((pos, i))
                    break
        return solution


f = FindNextLargest()

print(f.solution2([3, 2, 3, 6, 5, 9, 8]))

assert f.solution1([3, 2, 3, 6, 5, 9, 8]) == [3, 2, 3, 5, 5, -1, -1]
assert f.solution2([3, 2, 3, 6, 5, 9, 8]) == [3, 2, 3, 5, 5, -1, -1]
