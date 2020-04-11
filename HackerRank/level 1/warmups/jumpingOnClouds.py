"""
Emma is playing a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.
She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
She must avoid the thunderheads.

Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud.
It is always possible to win the game.

Avoid the "1"s

Assumptions: The problem is solvable

:input: [0, 0, 1, 0, 0, 1, 0]
:output: 4
"""


class JumpingOnCloudsSolution:
    def solve(self, c):
        """
        Concept:
            Since there are only 2 possible steps, 1 or 2, can start with 2, then 1.
        """
        steps_counter = 0
        current_pos = 0
        arr_length = len(c)
        while current_pos < arr_length - 1:
            next_pos = current_pos + 2
            if self.posExceeds(arr_length, next_pos):
                if self.nextPosFree(c, current_pos + 1):
                    current_pos += 1
                else:
                    return 0
            else:
                if self.nextPosFree(c, next_pos):
                    current_pos += 2
                else:
                    current_pos += 1
            steps_counter += 1
        return steps_counter

    def posExceeds(self, lastPos, nextPos):
        return nextPos >= lastPos

    def nextPosFree(self, arr, nextPos):
        return arr[nextPos] != 1


sol = JumpingOnCloudsSolution()
print(sol.solve([0, 0, 1, 0, 0, 1, 0]))
print(sol.solve([0, 0, 0, 1, 0, 0]))
