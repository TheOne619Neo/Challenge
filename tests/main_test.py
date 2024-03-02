import unittest

# Import the function to be tested
from calc import evaluate_subexpression

class TestEvaluateSubexpression(unittest.TestCase):
    def test_single_digit_operand(self):
        # Test evaluating a single-digit operand
        result = evaluate_subexpression("5", 0, 1)
        self.assertEqual(result, "5")
        
    def test_addition(self):
        # Test addition operation
        result = evaluate_subexpression("2 + 3", 0, 5)
        self.assertEqual(result, "5")
        
    def test_subtraction(self):
        # Test subtraction operation
        result = evaluate_subexpression("5 - 2", 0, 5)
        self.assertEqual(result, "3")
        
    def test_multiplication(self):
        # Test multiplication operation
        result = evaluate_subexpression("2 * 3", 0, 5)
        self.assertEqual(result, "6.0")
        
    def test_division(self):
        # Test division operation
        result = evaluate_subexpression("6 / 2", 0, 5)
        self.assertEqual(result, "3.0")
        
    def test_nested_subexpression(self):
        # Test nested subexpression
        result = evaluate_subexpression("(2 * (3 + 4))", 0, 11)
        self.assertEqual(result, "14")
        
    def test_invalid_expression(self):
        # Test invalid expression
        with self.assertRaises(ValueError):
            evaluate_subexpression("2 +", 0, 3)  # Missing operand

if __name__ == "__main__":
    unittest.main()
