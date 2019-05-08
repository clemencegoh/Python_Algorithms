def changeArray(x, y):
    """
    x: list of len x
    y: list of len y, where y > x
    This function loops through 2 lists, and 
    inserts a "blank" where there is a gap
    """
    # ensure that y is always bigger
    if len(x) > len(y):
        x, y = y, x
    
    # arrange lists
    x.sort()
    y.sort()

    # Here, we assume that x will always have missing items
    p1 = 0
    p2 = 0
    newarr = []
    while p2 < len(y):
        if x[p1] == y[p2]:
            newarr.append(x[p1])
            p1 += 1
            p2 += 1
        elif x[p1] > y[p2]:
            newarr.append('blank')
            p2 += 1
    return newarr

print(changeArray([1,4,6,8,7,3,2,9,12], [1,2,3,4,5,6,7,8,9,10,11,12]))