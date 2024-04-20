import unittest
from collections import deque
from calculator import Calculator
from algorithms.validator import Validator
from algorithms.shunting_yard import ShuntingYard
from algorithms.result_calculator import ResultCalculator

# FROM COMMAND LINE: coverage run --branch -m pytest src; coverage html


class TestCalculator(unittest.TestCase):
    """Tests for Calculator class, which is responsible for the application logic.

    """

    def setUp(self):
        self.calculator = Calculator()
        self.validator = Validator()
        self.shunting_yard = ShuntingYard()
        self.result_calculator = ResultCalculator()
        self.saved_variables = {}
        self.single_arg_functions = ["sqrt", "sin", "cos", "tan"]
        self.double_arg_functions = ["min", "max"]
        self.all_valid_functions = self.single_arg_functions + self.double_arg_functions


    def test_expression_with_single_digit_gives_correct_answer(self):
        expression = "5"
        wanted_result = "5"

        self.validator.validate(expression, self.saved_variables, self.all_valid_functions)
        validated_expression = self.validator.get_expression_deque()
        postfix_expression = self.shunting_yard.start(validated_expression)
        result = self.result_calculator.calculate(postfix_expression, self.single_arg_functions, self.double_arg_functions)

        self.assertEqual(result, wanted_result)

    def test_expression_with_operations_gives_correct_answer(self):
        expression = "5+3*2-1"
        wanted_result = "10"

        self.validator.validate(expression, self.saved_variables, self.all_valid_functions)
        validated_expression = self.validator.get_expression_deque()
        postfix_expression = self.shunting_yard.start(validated_expression)
        result = self.result_calculator.calculate(postfix_expression, self.single_arg_functions, self.double_arg_functions)

        self.assertEqual(result, wanted_result)

    def test_expression_with_operations_and_paranthesis_gives_correct_answer(self):
        expression = "(5+3)*(2-1)+6"
        wanted_result = "14"

        self.validator.validate(expression, self.saved_variables, self.all_valid_functions)
        validated_expression = self.validator.get_expression_deque()
        postfix_expression = self.shunting_yard.start(validated_expression)
        result = self.result_calculator.calculate(postfix_expression, self.single_arg_functions, self.double_arg_functions)

        self.assertEqual(result, wanted_result)

    def test_expression_with_one_single_arg_function_gives_correct_answer(self):
        expression = "sqrt(9)"
        wanted_result = "3.0"

        self.validator.validate(expression, self.saved_variables, self.all_valid_functions)
        validated_expression = self.validator.get_expression_deque()
        postfix_expression = self.shunting_yard.start(validated_expression)
        result = self.result_calculator.calculate(postfix_expression, self.single_arg_functions, self.double_arg_functions)

        self.assertEqual(result, wanted_result)

    def test_expression_with_one_double_arg_function_gives_correct_answer(self):
        expression = "max(2,5)"
        wanted_result = "5"

        self.validator.validate(expression, self.saved_variables, self.all_valid_functions)
        validated_expression = self.validator.get_expression_deque()
        postfix_expression = self.shunting_yard.start(validated_expression)
        result = self.result_calculator.calculate(postfix_expression, self.single_arg_functions, self.double_arg_functions)

        self.assertEqual(result, wanted_result)


    def test_expression_with_multiple_functions_and_operations_gives_correct_answer(self):
        expression = "(max(2,5)+5)*3/sqrt(9)"
        wanted_result = "10.0"

        self.validator.validate(expression, self.saved_variables, self.all_valid_functions)
        validated_expression = self.validator.get_expression_deque()
        postfix_expression = self.shunting_yard.start(validated_expression)
        result = self.result_calculator.calculate(postfix_expression, self.single_arg_functions, self.double_arg_functions)

        self.assertEqual(result, wanted_result)