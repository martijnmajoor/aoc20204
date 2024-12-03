import unittest

from solution import mulsum

class TestDay2(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(mulsum('test.txt'), 161)

if __name__ == "__main__":
    unittest.main()