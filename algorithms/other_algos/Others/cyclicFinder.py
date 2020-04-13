"""
Given a cyclic array of integers,
return an array of equal size where each item in the array
is replaced by the next highest in the array

If no higher number is available, insert -1

:input:     [1, 4, 2, 6, 7, 2]
:output:    [4, 6, 6, 7, -1, 4]


INCOMPLETE
"""


class CyclicFinderSolution:
    def solve(self, arr):
        return self.naive_sol(arr)

    def naive_sol(self, arr):
        """
        Naive solution, forward then backward fill
        """
        newarr = arr
        current_pos = 0
        for pos in range(len(arr)):
            if arr[pos] > arr[current_pos]:
                for i in range(current_pos, pos):
                    newarr[i] = arr[pos]
            current_pos += 1
        return newarr


test_cases = [
    ([1, 4, 2, 6, 7, 2], [4, 6, 6, 7, -1, 4]),
]

sol = CyclicFinderSolution()
for t in test_cases:
    print("original:", t[0])
    print("output:", sol.solve(t[0]))
    print("actual:", t[1])
