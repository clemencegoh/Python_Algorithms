"""
Similar to max profits, but restricted to only buying and selling once
Buy must be done before sell

example1: [1, 2, 4, 1, 3, 7] -> 6
example2: [7, 1, 5, 3, 6, 4] -> 5
example3: [7, 6, 5, 4, 3, 2, 1] -> 0
"""

class MaxSingleProfit:
    def solution(self, arr):
        
        # keep in memory:
        biggest_diff = 0
        current_max = arr[len(arr)-1]
        current_min = arr[len(arr)-1]

        # back to front
        for i in range(len(arr)-1, 0, -1):
            # update current max and min
            if arr[i] > current_max:
                current_max = arr[i]
                current_min = current_max
            
            # update current min
            if arr[i] < current_min:
                current_min = arr[i]
            
            # update difference
            if biggest_diff < current_max - current_min:
                    biggest_diff = current_max - current_min
        return biggest_diff


m = MaxSingleProfit()
print(m.solution([1, 2, 4, 1, 3, 7]))
print(m.solution([7, 1, 5, 3, 6, 4]))
print(m.solution([7, 6, 5, 4, 3, 2, 1]))


