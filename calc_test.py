import unittest
import calc


class TestCalc(unittest.TestCase):

 def test_add(self):
     self.assertEqual(calc.add(15,20),35)
     self.assertEqual(calc.add(10,5),15)
     self.assertEqual(calc.add(6,37),43)

 def test_substract(self):
     self.assertEqual(calc.substract(25,20),5)
     self.assertEqual(calc.substract(10,10),0)
     self.assertEqual(calc.substract(13,50),-37)

 def test_divide(self):
     self.assertEqual(calc.divide(20,20),1)
     self.assertEqual(calc.divide(40,5),8)
     self.assertEqual(calc.divide(50,25),2)

 def test_multiply(self):
     self.assertEqual(calc.multiply(10,20),200)
     self.assertEqual(calc.multiply(13,3),39)
     self.assertEqual(calc.multiply(5,5),25)

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
