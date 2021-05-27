
import fizzbuzz
import unittest


class fizzbuzzTestCase(unittest.TestCase):
    def test_normalValue(self):
        self.assertEqual(fizzbuzz.getFizzBuzzResult(1),"1")
    def test_divisibleByThree(self):
        self.assertEqual(fizzbuzz.getFizzBuzzResult(3),"Fizz")
        


if __name__ == "__main__":
    unittest.main()