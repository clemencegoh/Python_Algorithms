

def getPairs(arr):
    # given arr of pairs, print highest, lowest, average for each item
    # first, throw everything into a map
    storage = {}
    for item in arr:
        if item[0] not in storage:
            # count, min, max, total
            storage[item[0]] = [1, item[1], item[1], item[1]] 
        else:
            current_count = storage[item[0]][0]
            current_min = storage[item[0]][1]
            current_max = storage[item[0]][2]
            current_total = storage[item[0]][3]
            # edit current entry
            storage[item[0]] = [current_count + 1, min(current_min, item[1]), max(current_max, item[1]), current_total + item[1]]
    
    # then, for each item, print output
    for key, val in sorted(storage.items()):
        print("{} {} {} {}".format(key, val[1], val[2], int(val[3]/val[0])))

# getPairs([('banana', 90), ('apple', 100), ('apple', 260)])


def maximize_loot(hval, n): 
    if n == 0: 
        return 0
  
    value1 = hval[0] 
    if n == 1: 
        return value1 
  
    value2 = max(hval[0], hval[1]) 
    if n == 2: 
        return value2 
  
    # contains maximum stolen value at the end 
    max_val = None
  
    # Fill remaining positions 
    for i in range(2, n): 
        max_val = max(hval[i]+value1, value2) 
        value1 = value2 
        value2 = max_val 
  
    return max_val 


print(maximize_loot([6, 7, 1, 3, 8, 2, 4] , 7))