"""
Classic question, looking for longest common subsequence
This subsequence does not have to be right next to each other
Can be obtained by deleting certain elements but preserving the order
of the other elements


Easier problem involves longest common adjacent subsequence

example:
[1, 2, 3, 4, 1]
[3, 4, 1, 2, 1, 3]
Longest = 3; [3, 4, 1], [1, 2, 3], [1, 2, 3]


Concept is to create a 2d array displaying the longest matching sequence 
  a b c d f h l
k 0 0 0 0 0 0 0
m 0 0 0 0 0 0 0 
c 0 0 1 0 0 0 0
d 0 0 1 2 2 2 2 
f 0 0 1 2 3 3 3
m 0 0 1 2 3 3 3

Longest sequence here is thus 3, with diagonal showing the sequence
Similar concept can be applied to the harder problem
"""

class longestCommonSubsequence:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2
        self.arr2D = []

    def construct2DArray(self):
        self.arr2D.append([0] + self.arr1)
        for i in self.arr2:
            self.arr2D.append([i] + [0] * len(self.arr1))

    def findMatch(self, i, j):
        # determines if x == y
        return self.arr2D[i][0] == self.arr2D[0][j]
    
    def checkUp(self, i, j):
        if i - 1 <= 0:
            return 0
        return self.arr2D[i-1][j]

    def checkLeft(self, i, j):
        if j - 1 <= 0:
            return 0
        return self.arr2D[i][j - 1]

    def checkDiag(self, i, j):
        if j - 1 <= 0:
            return 0
        if i - 1 <= 0:
            return 0
        return self.arr2D[i-1][j - 1]

    def markLocation(self, i, j, num):
        # add to max, mutates arr2D
        self.arr2D[i][j] = self.checkDiag(i,j) + num

    def markMax(self, i, j):
        self.arr2D[i][j] = max(self.checkUp(i,j), self.checkLeft(i,j))

    def run(self):
        self.construct2DArray()
        for i in range(1, len(self.arr2) + 1, 1):
            for j in range(1, len(self.arr1) + 1, 1):
                if self.findMatch(i,j):
                    self.markLocation(i, j, 1)
                else:
                    self.markMax(i,j)

        for k in self.arr2D:
            print(k)
        print()

        return self.arr2D[len(self.arr2)][len(self.arr1)]



def main():
    # Driver code
    a = [1, 2, 3, 4, 1]
    b = [5, 3, 4, 1, 2, 1, 3]
    longest = longestCommonSubsequence(a, b).run()
    print(longest)
    
    assert longest == 3

main()

