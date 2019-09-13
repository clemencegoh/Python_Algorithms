"""
Medium puzzle
Algorithm to find scores while climbing the leaderboard
Given 2 sorted lists:
- Scoreboard: [100, 100, 80, 60]
- Alice: [50, 60, 75, 105]

Find the scores of alice
Ans: [3, 2, 2, 1] 
"""

def countRankings(arr):
    # Gets initial rankings 
    count = 1
    if len(arr) == 1:
        return count
    for i in range(1, len(arr), 1):
        if arr[i] != arr[i - 1]:
            count += 1
    return count


# Complete the climbingLeaderboard function below.
# Overall algo: time complexity O(nm)
def climbingLeaderboard(scores, alice):
    current = countRankings(scores) + 1
    ptr = len(scores) - 1
    arr = []
    prev = 0

    # iterate through alice's scores
    for alice_score in alice:
        # while condition to move pointer
        while (ptr >= 0):
            if scores[ptr] == prev:
                ptr -= 1
                continue
            # check if larger than score
            if scores[ptr] > alice_score:
                break
            current -= 1
            prev = scores[ptr]
            ptr -= 1
        # once stop moving pointer, append to array
        arr.append(current)
    return arr


