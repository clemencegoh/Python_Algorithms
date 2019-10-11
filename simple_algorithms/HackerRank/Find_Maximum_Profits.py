#
# Given an array of numbers, calculate max profits
# obtained by buying and selling during each iterative time stamp.
# Examples given below
#
#



def findGlobalMax(arr):
    return max(arr)

def getMaxProfits(arr, max_num):
    loss = 0
    counter = 0
    while (counter != len(arr) - 1 and arr[counter] != max_num):
        loss += arr[counter]
        counter += 1
    return (counter, counter * max_num - loss) 

def maximumProfit(prices):
    # Assume only one share at a time can be bought per time stamp
    # Look for 'peaks'
    if len(prices) <= 1:
        return 0
    
    total_profits = 0
    new_arr = prices
    while(len(new_arr) != 0):
        max_num = findGlobalMax(new_arr)
        ind, temp_total = getMaxProfits(new_arr, max_num)
        total_profits += temp_total
        new_arr = new_arr[ind + 1:]
    return total_profits

print(maximumProfit([5,3,2]))
print(maximumProfit([1,2,100]))
print(maximumProfit([1,3,1,2]))
print(maximumProfit([6,5,4,5,3]))
print(maximumProfit([1,2,1,3]))  # this should give 5 instead of 3