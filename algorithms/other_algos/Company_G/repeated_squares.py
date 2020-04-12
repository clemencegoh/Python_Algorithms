"""
Given 2 numbers A and B,
Return greatest number of times a sqrt can be
performed on perfect square within range

eg. 10, 20: 2 ==> 16 -> 4 -> 2
"""


import math


def solution(A, B):
    # write your code in Python 3.6
    lower = math.floor(math.sqrt(A))
    higher = math.ceil(math.sqrt(B) + 1)

    to_check = []

    if higher <= 3:
        return 0

    # check every square in between
    for num in range(int(lower), int(higher)):
        to_check.append(num)

    greatest = 0

    for i in to_check:
        initial = i

        # reduce to base, check if is perfect square
        while int(math.sqrt(initial)) * int(math.sqrt(initial)) == initial:
            initial = math.sqrt(initial)

        total = 0

        # square this until exceed B
        while initial < B:
            total += 1
            initial *= initial

        greatest = max(total - 1, greatest)

    return greatest

print(solution(2,3)) # 0
print(solution(10, 20)) #2
print(solution(6000, 7000)) #3
print(solution(80, 90)) #2
print(solution(80, 130))  #2 ?