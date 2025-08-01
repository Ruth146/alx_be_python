import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the calculator before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Negative and positive
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Two negatives
        self.assertEqual(self.calc.add(-2, -3), -5)
        # Zeros
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Simple subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Negative result
        self.assertEqual(self.calc.subtract(3, 5), -2)
        # Subtracting negatives
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        # Zeros
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        """Test the multiplication method."""
        # Positive numbers
        self.assertEqual(self.calc.multiply(4, 5), 20)
        # Negative and positive
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        # Two negatives
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Multiplying with zero
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        """Test the division method, including division by zero."""
        # Normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Negative numerator
        self.assertEqual(self.calc.divide(-6, 3), -2)
        # Zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0)
        # Division by zero
        self.assertIsNone(self.calc.divide(5, 0))

if __name__ == '__main__':
    unittest.main()
