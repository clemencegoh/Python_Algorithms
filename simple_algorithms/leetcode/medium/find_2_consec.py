"""
Question:
Given an array containing any number of integers, find the longest
length of consecutive chain of numbers where there are only 2 types.

eg:
input: [0,1,1,0,2,2]
output: 4

input: [0,1,2,2]
output: 3

"""
class Longest2Consec:
    def solution(self, array: [int]) -> int:
        pointerA = 0
        pointerB = 0
        longest = 0
        other_elem = 0
        current_elems = dict()


        while pointerB < len(array):
            if array[pointerB] not in current_elems:
                # never seen before
                if len(current_elems) < 2:
                    # is cool
                    current_elems[array[pointerB]] = 1

                    # add to length
                    longest = max(longest, pointerB - pointerA + 1)
                else:
                    # not cool, exceeded

                    # get other elem
                    for k,val in current_elems.items():
                        if k != array[pointerB - 1]:
                            other_elem = k

                    while current_elems[other_elem] != 0:
                        current_elems[array[pointerA]] -= 1
                        pointerA += 1
                    del current_elems[other_elem]
                    current_elems[array[pointerB]] = 1

            else:
                # continuing from start
                current_elems[array[pointerB]] += 1
                longest = max(longest, pointerB - pointerA + 1)
            pointerB += 1
        print(current_elems)
        return longest

L = Longest2Consec()
print(L.solution([0,1,1,0,0,0,1,1,1,1,2,2]))