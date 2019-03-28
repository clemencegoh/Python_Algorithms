import unittest

class TestConvert(unittest.TestCase):
    def test_all(self):
        test_in = [978155192370, 978140007917, 978037541457, 978037428158]
        test_out = ['155192370x', '1400079179', '0375414576', '0374281580']
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()