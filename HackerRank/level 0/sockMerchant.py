"""
John works at a clothing store.
He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

:input: [10, 20, 20, 10, 10, 30, 50, 10, 20]
:output: 3
"""


# Completed
class SockMerchantSolution:
    def solve(self, arr):
        """
        Concept:
            looking for pairs of the same color (int)
            Opt to use boolean and increment global counter instead of
                using a counter for each item in hashMap.
        """
        counter = 0
        store = {k: False for k in arr}

        for item in arr:
            if store[item]:
                counter += 1
                store[item] = False
            else:
                store[item] = True

        return counter


sol = SockMerchantSolution()
print(sol.solve([10, 20, 20, 10, 10, 30, 50, 10, 20]))
