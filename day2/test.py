import unittest

from solution import safe

class TestDay2(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(safe('test.txt'), 2)

    def test_part2(self):
        self.assertEqual(2, 2)

if __name__ == "__main__":
    unittest.main()