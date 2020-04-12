

"""
Helper functions for matrix algorithms
"""


def checkUp(matrix, y, x):
    if y - 1 < 0:
        return False  # signifies end
    if matrix[y-1][x] == '.':
        return True
    return False

def checkDown(matrix, y, x):
    if y + 1 >= len(matrix):
        return False
    if matrix[y+1][x] == '.':
        return True
    return False

def checkRight(matrix, y, x):
    if x + 1 >= len(matrix[0]):
        return False
    if matrix[y][x + 1] == '.':
        return True
    return False

def checkLeft(matrix, y, x):
    if x - 1 < 0:
        return False
    if matrix[y][x - 1] == '.':
        return True
    return False