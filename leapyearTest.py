import leapyear
import unittest

class leapyearTestCase(unittest.TestCase):
    def test_normalyear(self):
        self.assertEqual(leapyear.isALeapYear(1),False)
    def test_divisByFour(self):
        self.assertEqual(leapyear.isALeapYear(4),True)
    def test_divisBy100(self):
        self.assertEqual(leapyear.isALeapYear(100),False)
if __name__ == "__main__":
    unittest.main()