import unittest

def string(a, b):
    return a.endswith(b)

fixed_tests_True = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs"),
)

class TestStringFunction(unittest.TestCase):
    # Test cases where the function should return True
    def test_fixed_true_cases(self):
        for a, b in fixed_tests_True:
            with self.subTest(a=a, b=b):
                self.assertTrue(string(a, b), f"Expected True for {a} ending with {b}")

    # Test cases where the function should return False
    def test_fixed_false_cases(self):
        for a, b in fixed_tests_False:
            with self.subTest(a=a, b=b):
                self.assertFalse(string(a, b), f"Expected False for {a} ending with {b}")

# Run the tests
if __name__ == '__main__':
    unittest.main()