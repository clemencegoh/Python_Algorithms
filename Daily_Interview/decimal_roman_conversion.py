"""
Convert decimal numbers into roman numerals
Max = 3999  ->  MMMCMXCIX


Given: 1000, 48, 444
:return: M, XLVIII, CDXLIV
7 symbols corresponding:
I   1
V   5
X   10
L   50
C   100
D   500
M   1000
"""

import math


class DecimalRomanConversion:
    def __init__(self):
        self.roman_symbols = ["I", "V", "X", "L", "C", "D", "M"]
        self.decimal_symbols = [1, 5, 10, 50, 100, 500, 1000]
        self.dec_to_roman_map = dict(zip(self.decimal_symbols, self.roman_symbols))

    def decimalToRoman(self, decimal_num: int):
        val = 1
        return_val = ""

        while val <= decimal_num:
            val *= 10

        val /= 10
        current_num = decimal_num

        while current_num > 0:
            # extract most significant number
            sig_num = int(current_num/val)

            # few special cases
            if sig_num == 9:            # IX, 1 and 10
                return_val += self.dec_to_roman_map[val] + self.dec_to_roman_map[val * 10]
            elif 5 < sig_num < 9:       # VIII, 5 and 1
                return_val += self.dec_to_roman_map[val * 5] + self.dec_to_roman_map[val] * (sig_num - 5)
            elif sig_num == 5:          # V, 5
                return_val += self.dec_to_roman_map[val * 5]
            elif sig_num == 4:          # IV, 1 and 5
                return_val += self.dec_to_roman_map[val] + self.dec_to_roman_map[val * 5]
            else:                       # III, 1
                return_val += self.dec_to_roman_map[val] * sig_num

            current_num = math.floor(current_num % val)
            val /= 10

        return return_val


c = DecimalRomanConversion()

test_integers = [3999, 3549, 764, 0, 1]
test_romans = ["MMMCMXCIX", "MMMDXLIX", "DCCLXIV", "", "I", ]

for pos in range(len(test_integers)):
    assert c.decimalToRoman(test_integers[pos]) == test_romans[pos]
    print(test_integers[pos], "==", test_romans[pos])
