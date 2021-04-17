from math_dojo import MathDojo
import unittest

class MathTest(unittest.TestCase):
    def setUp(self):
        self.md = MathDojo()

    def testAdd(self):
        self.assertEqual(self.md.add([2,3,4]).add(2,5,1).subtract(3,[3,4]).result,7)

    def testSubstract(self):
        self.assertEqual(self.md.add([2,2],[5,3]).add(2,5,(1,2,3)).subtract(3,2,(1,2,3)).result, 14)
  

if __name__ == "__main__":
  unittest.main()

