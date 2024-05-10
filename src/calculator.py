import string
from collections import deque
from algorithms.validator import Validator
from algorithms.shunting_yard import ShuntingYard
from algorithms.result_calculator import ResultCalculator

class Calculator:
    """Class, responsible for the application logic.

    Attributes:
        expression: String, holds the expression in infix notation, given by the user
        validator: Validator-class, does the initial validation to the expression
        shunting_yard: ShuntingYard-class, checks validated expression using shunting yard algorithm
        result_calculator, ResultCalculator-class, calculates the result for the postfix expression
        rpn: Deque, holds the expression in postfix notation or Reverse Polish notation
        result: String, result of the expression
        saved_variables: Dictionary, keeps track of the saved results. 
                         Key is the variable name and value is the result.
        index_of_last_saved_variable: Integer, tracks to which variable A-Z the result will be saved
        single_arg_functions: List, holds all valid single argument functions
        double_arg_functions: List, holds all valid double argument functions
        all_valid_functions: List, holds all valid functions

    """

    def __init__(self):
        """Class constructor, which creates a new calculator."""

        self.validator = Validator()
        self.shunting_yard = ShuntingYard()
        self.result_calculator = ResultCalculator()
        self.rpn = deque()
        self.result = ""
        self.saved_variables = {}
        self.index_of_variable = 0
        self.single_arg_functions = ["sqrt", "sin", "cos", "tan"]
        self.double_arg_functions = ["min", "max"]
        self.all_valid_functions = self.single_arg_functions + self.double_arg_functions

    def start(self, expression):
        """Starts the calculator. 

        Args:
            expression (str): Expression in infix notation.
            valitated_expression (deque): Expression in postfix notation.
        """

        if self.validator.validate(expression, self.saved_variables, self.all_valid_functions):
            self.validated_expression = self.validator.get_expression_deque()
        else:
            self.validated_expression = False

        if not self.validated_expression:
            print("Expression not valid")
            return False

        self.rpn = self.shunting_yard.start(self.validated_expression)
        if not self.rpn:
            print("Error: Expression not valid")
            return False

        self.result = self.result_calculator.calculate(self.rpn, self.single_arg_functions, self.double_arg_functions)

        return self.result

    def save_result_to_variable(self, result):
        """Saves the last result to the next available variable

        Args:
            result (str): Answer to the last expression which will be saved. 
        """
        variable = string.ascii_uppercase[self.index_of_variable]
        self.saved_variables[variable] = result
        self.index_of_variable += 1
        if self.index_of_variable >= 26: # If all letters have been used, start again from A
            self.index_of_variable = 0

    def get_saved_variables(self):
        """Gets all the saved variables from the dictionary

        Returns:
            Dictionary: Includes all the saved variables
        """

        return self.saved_variables

    def get_last_saved_variable(self):
        """Gets the last saved variable

        Returns:
            String: Last saved variable
        """

        return string.ascii_uppercase[self.index_of_variable-1]
