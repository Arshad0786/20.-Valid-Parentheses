import unittest
from ValidParenthese import Solution


class ReverseIntegerTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.value = "()"
        self.assertEqual(temp.isValid(self.value), True)


if __name__ == "__main__":
    unittest.main()
