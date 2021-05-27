import leapyear
import unittest

class leapyearTestCase(unittest.TestCase):
    def test_normalyear(self):
        self.assertEqual(leapyear.isALeapYear(1),True)
if __name__ == "__main__":
    unittest.main()