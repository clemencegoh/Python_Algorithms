class Magic(object):
    """
    Magic squares are 2d matrix configurations
    where every row and column add up to the same
    number
    In this case, since each number has to be unique
    from 0-9, total number is 45.
    Equal distribution between 3 rows will hence have 
    to be 15
    * Learning purposes
    ** All 8 possible configurations are as below
    in 'pre'
    """

    pre = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]

    def evaluate(self, s):
        totals = []
        for p in self.pre:
            total = 0
            for p_row, s_row in zip(p, s):
                for i, j in zip(p_row, s_row):
                    if not i == j:
                        total += max([i, j]) - min([i, j])
            totals.append(total)
        return min(totals)