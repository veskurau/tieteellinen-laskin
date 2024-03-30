import unittest
from calculator import Calculator
from collections import deque

# FROM COMMAND LINE: coverage run --branch -m pytest src; coverage html

class TestCalculator(unittest.TestCase):
    """Tests for Calculator class, which is responsible for the application logic.

    Attributes:
        calculator: Calculator, gives access to to class Calculator
        expression_deque: Deque, holds the expressions tokens in infix notation
        
    """

    def setUp(self):
        self.calculator = Calculator()
        self.expression_deque = deque()

    def test_expression_with_single_digit_is_correct(self):
        expression = "5"
        self.expression_deque.append(expression)
        returned = self.calculator.validate_and_change_to_deque(expression)
        self.assertEqual(returned, self.expression_deque)

    def test_token_with_multiple_numbers_is_read_correctly(self):
        expression = "19500"
        self.expression_deque.append(expression)
        returned = self.calculator.validate_and_change_to_deque(expression)
        self.assertEqual(returned, self.expression_deque)

    def test_token_with_decimal_point_is_read_correctly(self):
        expression = "15.025"
        self.expression_deque.append(expression)
        returned = self.calculator.validate_and_change_to_deque(expression)
        self.assertEqual(returned, self.expression_deque)

    def test_token_with_more_than_one_decimal_point_is_rejected(self):
        expression = "15.025.85"
        returned = self.calculator.validate_and_change_to_deque(expression)
        self.assertEqual(returned, False)

    def test_token_which_ends_with_decimal_point_is_rejected(self):
        expression = "15.025."
        returned = self.calculator.validate_and_change_to_deque(expression)
        self.assertEqual(returned, False)

    def test_token_with_decimal_point_must_have_numbers_after_it(self):
        expression1 = "15.a"
        expression2 = "15.B"
        expression3 = "15.+"
        expression4 = "15.&&&"
        returned = self.calculator.validate_and_change_to_deque(expression1)
        self.assertEqual(returned, False)
        returned = self.calculator.validate_and_change_to_deque(expression2)
        self.assertEqual(returned, False)
        returned = self.calculator.validate_and_change_to_deque(expression3)
        self.assertEqual(returned, False)
        returned = self.calculator.validate_and_change_to_deque(expression4)
        self.assertEqual(returned, False)




