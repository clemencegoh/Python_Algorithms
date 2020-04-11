"""
You are given an unordered array consisting of consecutive
integers  E[1, 2, 3, ..., n] without any duplicates.
You are allowed to swap any two elements.
You need to find the minimum number of swaps required to sort the array in ascending order.

:input: [7, 1, 3, 2, 4, 5, 6]
:output: 5
"""


class MinimumSwapsSolution:
    def solve(self, arr):
        """
        Concept:
            Just swap to the item in the index
        """

        # convert to indices for sanity
        arr = [i-1 for i in arr]
        pointer = 0
        counter = 0

        while pointer != len(arr) - 1:
            if arr[pointer] == pointer:
                pointer += 1
            else:
                get = arr[pointer], arr[arr[pointer]]
                arr[arr[pointer]], arr[pointer] = get
                counter += 1
        return counter
        

test_cases = [
    ([7, 1, 3, 2, 4, 5, 6], 5),
    ([4, 3, 1, 2], 3),
    ([2, 3, 4, 1, 5], 3),
]

sol = MinimumSwapsSolution()
for t in test_cases:
    print('output:', sol.solve(t[0]))
    print('actual:', t[1])
    print()
