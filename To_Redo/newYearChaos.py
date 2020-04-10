"""
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride!
There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue.
Initial positions increment by 1 from 1 at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap positions.
If two people swap positions,
they still wear the same sticker denoting their original places in line.
One person can bribe at most two others.
For example, if n=8 and person 5 bribes person 4, the queue will look like this: 1, 2, 3, 5, 4, 6, 7, 8.

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get
the queue into its current state!

:input: 2 1 5 3 4
:output: 3

:input: 2 5 1 3 4
:output: Too chaotic

^ one person can at most bribe 2 others
"""


class NewYearChaosSolution:
    def solve2(self, q):
        # TODO
        pass
                    

test_cases = [
    ([2, 1, 5, 3, 4], 3),
    ([2, 5, 1, 3, 4], "Too chaotic"),
    # custom tests
    ([1, 2, 3, 4, 5], 0),
    ([2, 3, 4, 5, 1], 4),
    ([1, 2, 5, 4, 3], 3),
    ([3, 2, 1, 5, 4], 4),
    ([3, 2, 5, 1, 4], 5),
    ([3, 2, 5, 4, 1], 6),
    ([3, 4, 5, 6, 1, 2], 8),
    ([2, 4, 3, 5, 6, 1], 6),
    ([1, 2, 5, 3, 7, 8, 6, 4], 7),
]
# [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 2, 5, 3, 4, 6, 7, 8]  # 2
# [1, 2, 5, 3, 7, 4, 6, 8]  # 4
# [1, 2, 5, 3, 7, 8, 4, 6]  # 6
# [1, 2, 5, 4, 7, 8, 6, 4]  # 7

sol = NewYearChaosSolution()
for t in test_cases:
    sol.solve2(t[0])
    print("actual:", t[1])
    print()
