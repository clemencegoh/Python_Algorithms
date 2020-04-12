"""
Highest cont subarray value
"""


def moveLeftPtr(arr, posA, posB):
    total = 0
    highest = 0
    while posA != posB:
        # move left pointer and sum. If at any point sum is negative, 
        # remove all behind and try again
        total += arr[posA]
        if total > highest:
            highest = total
        if total < 0:
            return posA, highest
        posA += 1
    if total > highest:
        highest = total
    return posA, highest


def moveRightPtr(arr, posA, posB):
    total = 0
    highest = 0
    while posA != posB:
        # move left pointer and sum. If at any point sum is negative, 
        # remove all behind and try again
        total += arr[posB]
        if total > highest:
            highest = total
        if total < 0:
            return posB, highest
        posA -= 1
    if total > highest:
        highest = total
    return posB, highest


def maximumSum2(arr):
    highest = 0
    temp = 0

    ptrA = 0
    ptrB = len(arr) - 1

    while ptrA != ptrB:
        # alternate left and right
        ptrA, temp = moveLeftPtr(arr, ptrA, ptrB)
        if temp > highest:
            highest = temp
        ptrB, temp = moveRightPtr(arr, ptrA, ptrB)
        if temp > highest:
            highest = temp
    return highest



def maximumSum3(arr):
    # use double pointers to create a window
    ptrA = 0
    ptrB = len(arr) - 1

    # shift both until non negative
    while arr[ptrA] < 0:
        ptrA += 1
    
    while arr[ptrB] < 0:
        ptrB -= 1

    highest = 0
    total = 0

    ptrA = 0
    ptrB = len(arr) - 1

    while ptrA != ptrB:
        # move left pointer and sum. If at any point sum is negative, 
        # remove all behind and try again
        total += arr[ptrA]
        if total > highest:
            highest = total
        if total < 0:
            total = 0
        ptrA += 1
    if total > highest:
        highest = total

    return highest


def maximumSum(arr):
    highest = arr[0] 
    curr_highest = arr[0] 
      
    for i in range(1, len(arr)): 
        curr_highest = max(arr[i], curr_highest + arr[i]) 
        highest = max(highest, curr_highest) 
          
    return highest 



# driver code
print(maximumSum([-1, -2, 3, 4]))
