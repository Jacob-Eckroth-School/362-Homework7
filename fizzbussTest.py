
import fizzbuzz
import unittest


class fizzbuzzTestCase(unittest.TestCase):
    def test_normalValue(self):
        self.assertEqual(fizzbuzz.getFizzBuzzResult(1),"1")


if __name__ == "__main__":
    unittest.main()