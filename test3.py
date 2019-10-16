import num3
import unittest

class TestSum(unittest.TestCase):
    def test_product(self):
        num1 = '12'
        num2 = '11'
        result = num3.product(num1,num2)
        self.assertEqual(result, '132')

    def test_StrToInt(self):
        num1 = '12'
        result = num3.StrToInt(num1)
        self.assertEqual(result, 12)

    def test_IntToStr(self):
        num1 = 12
        result = num3.IntToStr(num1)
        self.assertEqual(result, '12')
        
if __name__ == '__main__':
    unittest.main()
