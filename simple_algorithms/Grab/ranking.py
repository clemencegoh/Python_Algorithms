"""
Every number represents a rank
Given an array of ranks: [5, 4, 3, 1, 0, 0, 2]
Return number of people who have a superior (can only report to direct superior)

Eg. [3,4,3,0,2,2,3,0,0] => 5: 2x 2 report to 3, 3x 3 report to 4
"""



def solution(ranks):
    all_ranks = {}  # keep dict of all ranks and count
    greatest_number = 0

    # O(N)
    for number in ranks:
        if number > greatest_number:
            greatest_number = number
        if number in all_ranks:
            all_ranks[number] += 1
        else:
            all_ranks[number] = 1

    total = 0

    for i in range(1, greatest_number+1):
        if i in all_ranks:
            if (i-1) in all_ranks:
                total += all_ranks[i-1]

    return total



print(solution([3,4,3,0,2,2,3,0,0]))
