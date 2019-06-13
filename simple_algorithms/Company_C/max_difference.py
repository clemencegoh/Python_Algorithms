"""
Given an array, return the max difference between
2 numbers in array whereby:
- larger number is after smaller number in array order

eg: [0, 1, 12] -> 12
eg: [12, 0, 1] -> 1

"""


def maxDiff(arr, n):
    # Initialize Result
    maxDiff = -1

    # Initialize max element from
    # right side
    maxRight = arr[n - 1]

    for i in range(n - 2, -1, -1):
        if arr[i] > maxRight:
            maxRight = arr[i]
        else:
            diff = maxRight - arr[i]
            if diff > maxDiff:
                maxDiff = diff
    return maxDiff

