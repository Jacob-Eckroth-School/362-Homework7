
import fizzbuzz
import unittest


class fizzbuzzTestCase(unittest.TestCase):
    def test_normalValue(self):
        self.assertEqual(fizzbuzz.getFizzBuzzResult(1),"1")
    def test_divisibleByThree(self):
        self.assertEqual(fizzbuzz.getFizzBuzzResult(3),"Fizz")
    def test_divisibleByFive(self):
        self.assertEqual(fizzbuzz.getFizzBuzzResult(5),"Buzz")
    def test_divisibleByFiveAndThree(self):
        self.assertEqual(fizzbuzz.getFizzBuzzResult(15),"FizzBuzz")



if __name__ == "__main__":
    unittest.main()