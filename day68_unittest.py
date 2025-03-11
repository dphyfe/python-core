# Day 68: unit testing for my practice

import unittest

def my_add(a, b):
    return a + b

def my_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class MyMathTests(unittest.TestCase):
    def test_my_add(self):
        self.assertEqual(my_add(2, 3), 5)
        self.assertEqual(my_add(-1, 1), 0)
    
    def test_my_divide(self):
        self.assertEqual(my_divide(10, 2), 5)
        self.assertAlmostEqual(my_divide(1, 3), 0.333, places=2)
    
    def test_my_divide_by_zero(self):
        with self.assertRaises(ValueError):
            my_divide(10, 0)

class MyStringTests(unittest.TestCase):
    def setUp(self):
        self.my_text = "Hello World"
    
    def tearDown(self):
        self.my_text = None
    
    def test_my_upper(self):
        self.assertEqual(self.my_text.upper(), "HELLO WORLD")
    
    def test_my_split(self):
        self.assertEqual(self.my_text.split(), ["Hello", "World"])
    
    def test_my_contains(self):
        self.assertIn("Hello", self.my_text)
        self.assertNotIn("Goodbye", self.my_text)

class MyListTests(unittest.TestCase):
    def test_my_list_ops(self):
        my_list = [1, 2, 3]
        self.assertTrue(len(my_list) == 3)
        self.assertFalse(len(my_list) == 4)
        self.assertIsNotNone(my_list)
        self.assertIsInstance(my_list, list)

if __name__ == "__main__":
    my_suite = unittest.TestLoader().loadTestsFromModule(__import__(__name__))
    my_runner = unittest.TextTestRunner(verbosity=2)
    my_result = my_runner.run(my_suite)
    print(f"\nMy tests run: {my_result.testsRun}")
    print(f"My failures: {len(my_result.failures)}")
    print(f"My errors: {len(my_result.errors)}")

# Progress: part 3/3
