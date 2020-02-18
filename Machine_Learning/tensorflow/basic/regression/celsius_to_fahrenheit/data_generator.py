"""
Generation of data cos it's tedius to do it by hand
"""


class Generator:
    def __init__(self, num_datapoints: int):
        self.n = num_datapoints
        self.celcius = []
        self.farenheight = []

    def getData(self):
        for i in range(self.n):
            num = i * 2 + 1
            self.celcius.append(num)
            self.farenheight.append(num * 9 / 5 + 32)
        return self.celcius, self.farenheight
