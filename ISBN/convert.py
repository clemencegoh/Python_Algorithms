import argparse
import math


def convert(productID):
    """
    ISBN number here generated will be a standard ISBN-10 number
    """
    # get last 9 numbers
    last9 = productID%1000000000
    ISBN = last9

    # sum numbers with multiplier
    multiplier = 2
    total = 0
    while last9 > 0:
        total += last9%10 * multiplier
        multiplier += 1
        last9 = int(last9/10)

    # find closeness to nearest 11 multiple
    nearest_multiple = 11 * math.ceil((total)/11)
    additional = nearest_multiple - total
    if additional == 10:
        ISBN = str(ISBN) + "x"
        return ISBN

    ISBN *= 10
    ISBN += additional   
    return str("{:010d}".format(ISBN))


def test_convert():
    test_in = [978155192370, 978140007917, 978037541457, 978037428158]
    test_out = ['155192370x', '1400079179', '0375414576', '0374281580']
    for i in range(len(test_in)):
        expected = convert(test_in[i])
        assert expected == test_out[i]



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Converts product number to corresponding ISBN number')
    parser.add_argument('-p', type=int, 
                        help='product number')
    parser.add_argument('-t',
                        help='test all test cases')
    args = parser.parse_args()
    productID = args.p
    testflag = args.t
    if testflag:
        test_convert()
    else:
        print('converting {}...'.format(productID))
        print(convert(productID))


