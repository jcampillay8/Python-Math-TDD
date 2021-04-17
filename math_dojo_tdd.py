from math_dojo import MathDojo
import unittest

class MathTest(unittest.TestCase):
    def setUp(self):
        self.md = MathDojo()

    def test1(self):
        self.assertEqual(self.md.add([2,3,4]).add(2,5,1).subtract(3,[3,4]).result,7)

    def test2(self):
        self.assertEqual(self.md.add([2,2],[5,3]).add(2,5,(1,2,3)).subtract(3,2,(1,2,3)).result, 14)
  
    def test3(self):
        self.assertGreater(self.md.add([2,2],[5,3]).add(2,5,(1,2,3)).subtract(3,2,(1,2,3)).result, 2)

if __name__ == "__main__":
    unittest.main()

