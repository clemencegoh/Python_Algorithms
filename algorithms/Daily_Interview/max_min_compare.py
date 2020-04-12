"""
Given an array, return max and min with less than 2 * (n - 1) comparisons

:analysis: 
why does this work?
Since the bulk of the comparisions are between:
    max(current_max, current) &
    min(current_min, current),
2 iterations of this would result in 4 comparisons.
We can reduce this to 3 by comparing once between the current and next value first:
    next_max = max(current, next),
    current_max = max(current_max, next_max),
    current_min = min(current_min, !next_max)
"""


def find_max_min(arr: [int]):
    n = len(arr)
    print("Aim is to do this in less than {} comparisons".format(2 * (n - 1)))

    total_comparisons = 0

    # catches
    if n == 0:
        return 0, 0
    if n == 1:
        return arr[0], arr[0]
    if n == 2:
        return max(arr[0], arr[1]), min(arr[0], arr[1])

    # Assume more than 2

    # determine how to assign based on length of array
    if n % 2 == 0:  # even number
        total_comparisons += 2
        current_min = min(arr[0], arr[1])
        current_max = max(arr[0], arr[1])
        i = 2
    else:
        current_min = current_max = arr[0]
        i = 1

    while i < n - 1:
        total_comparisons += 1
        if arr[i] > arr[i+1]:
            total_comparisons += 2
            current_max = max(current_max, arr[i])
            current_min = min(current_min, arr[i+1])
        else:
            total_comparisons += 2
            current_max = max(current_max, arr[i + 1])
            current_min = min(current_min, arr[i])
        i += 2

    print("Comparisons done: {}".format(total_comparisons))

    return current_max, current_min


def run_driver():
    arr = [1, 5, 12, 0, 8, -9, 1, 10]
    max_res, min_res = find_max_min(arr)
    assert max_res == 12
    assert min_res == -9


run_driver()
