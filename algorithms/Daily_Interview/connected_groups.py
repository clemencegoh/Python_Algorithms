"""
:Problem:
    Given an array of tuples, return the number of connected groups
:example:
    :given: [(1,2), (2,3), (4,1), (5,6)]
    :return: 2
    :explanation: The two groups are: (1, 2, 3, 4) and (5, 6)
"""


class ConnectedGroups:
    def solution(self, arr: []):
        num_groups = 0
        seen = set()
        for tup in arr:
            both_unseen = True
            for num in tup:
                if num in seen:
                    both_unseen = False
                else:
                    seen.add(num)
            if both_unseen:
                num_groups += 1
        return num_groups


conn = ConnectedGroups()
assert conn.solution([(1, 2), (2, 3), (4, 1), (5, 6)]) == 2
