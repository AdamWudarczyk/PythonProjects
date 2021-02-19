import unittest
import calc


class TestCalc(unittest.TestCase):

 def test_add(self):
     add_result = calc.add(10,5)
     self.assertEqual(add_result, 15)

 def test_substract(self):
     substract_result = calc.substract(30,2)
     self.assertEqual(substract_result, 15)

 def test_divide(self):
     divide_result = calc.divide(20,5)
     self.assertEqual(divide_result, 4)

 def test_multiply(self):
     multiply_result = calc.multiply(2,10)
     self.assertEqual(multiply_result, 60)

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
