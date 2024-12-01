import unittest

from solution import read, distance, score

class TestDay1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(distance(*read('test.txt')), 11)

    def test_part2(self):
        self.assertEqual(score(*read('test.txt')), 31)

if __name__ == "__main__":
    unittest.main()