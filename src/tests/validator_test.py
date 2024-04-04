import unittest
from collections import deque
from algorithms.validator import Validator

# FROM COMMAND LINE: coverage run --branch -m pytest src; coverage html


class TestValidator(unittest.TestCase):
    """Tests for Validator class, which is responsible for the initial validation
        of the expression in infix notation.

    Attributes:
        validator: Validator, gives access to class Validator
        expression_deque: Deque, holds the expressions tokens in infix notation

    """

    def setUp(self):
        self.validator = Validator()
        self.expression_deque = deque()
        self.saved_variables = {}

    def test_expression_with_single_digit_is_correct(self):
        expression = "5"
        self.expression_deque.append(expression)
        self.validator.validate(expression, self.saved_variables)
        self.assertEqual(self.validator.get_expression_deque(),
                         self.expression_deque)

    def test_token_with_multiple_numbers_is_read_correctly(self):
        expression = "19500"
        self.expression_deque.append(expression)
        self.validator.validate(expression, self.saved_variables)
        self.assertEqual(self.validator.get_expression_deque(),
                         self.expression_deque)

    def test_token_with_decimal_point_is_read_correctly(self):
        expression = "15.025"
        self.expression_deque.append(expression)
        self.validator.validate(expression, self.saved_variables)
        self.assertEqual(self.validator.get_expression_deque(),
                         self.expression_deque)

    def test_token_with_more_than_one_decimal_point_is_rejected(self):
        expression = "15.025.85"
        returned = self.validator.validate(expression, self.saved_variables)
        self.assertEqual(returned, False)

    def test_token_which_ends_with_decimal_point_is_rejected(self):
        expression = "15.025."
        returned = self.validator.validate(expression, self.saved_variables)
        self.assertEqual(returned, False)

    def test_token_with_decimal_point_must_have_numbers_after_it(self):
        expression1 = "15.a"
        expression2 = "15.B"
        expression3 = "15.+"
        expression4 = "15.&&&"
        returned = returned = self.validator.validate(
            expression1, self.saved_variables)
        self.assertEqual(returned, False)
        returned = returned = self.validator.validate(
            expression2, self.saved_variables)
        self.assertEqual(returned, False)
        returned = returned = self.validator.validate(
            expression3, self.saved_variables)
        self.assertEqual(returned, False)
        returned = returned = self.validator.validate(
            expression4, self.saved_variables)
        self.assertEqual(returned, False)

    def test_token_with_operation_is_read_correctly(self):
        valid_operations = "+-*/^(),"
        for operation in valid_operations:
            self.expression_deque = deque()
            self.expression_deque.append(operation)
            self.validator.validate(operation, self.saved_variables)
            returned = self.validator.get_expression_deque()
            self.assertEqual(returned, self.expression_deque)

    def test_token_with_correct_function_is_read_correctly(self):
        expression = "min(15)"
        self.expression_deque = deque()
        for token in ["min", "(", "15", ")"]:
            self.expression_deque.append(token)

        self.validator.validate(expression, self.saved_variables)
        returned = self.validator.get_expression_deque()
        self.assertEqual(returned, self.expression_deque)

    def test_token_with_mispelled_function_is_rejected(self):
        expression = "minn(15)"
        returned = self.validator.validate(expression, self.saved_variables)
        self.assertEqual(returned, False)

    def test_saved_variable_is_accepted_and_added_to_deque(self):
        expression = "A"
        self.saved_variables["A"] = "15"
        self.expression_deque.append("15")

        returned = self.validator.validate(expression, self.saved_variables)
        self.assertEqual(returned, True)
        self.assertEqual(self.validator.get_expression_deque(),
                         self.expression_deque)

    def test_unsaved_variable_is_rejected(self):
        expression = "A"

        returned = self.validator.validate(expression, self.saved_variables)
        self.assertEqual(returned, False)
        self.assertEqual(self.validator.get_expression_deque(),
                         self.expression_deque)
