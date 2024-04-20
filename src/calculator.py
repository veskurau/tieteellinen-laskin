import string
from collections import deque
from algorithms.validator import Validator
from algorithms.shunting_yard import ShuntingYard
from algorithms.result_calculator import ResultCalculator

# pylint: disable=all


class Calculator:
    """Class, responsible for the application logic.

    Attributes:
        expression: String, holds the expression in infix notation, given by the user
        validator: Validator-class, does the initial validation to the expression
        rpn: Deque, holds the expression in postfix notation or Reverse Polish notation
        saved_variables: Dictionary, keeps track of the saved results. 
                         Key is the variable name and value is the result.
        single_arg_functions: List, holds all valid single argument functions
        double_arg_functions: List, holds all valid double argument functions
        all_valid_functions: List, holds all valid functions
        stack: List, used as a stack where the operators and functions are pushed and popped

    """

    def __init__(self):
        """Class constructor, which creates a new calculator."""

        self.validator = Validator()
        self.shunting_yard = ShuntingYard()
        self.result_calculator = ResultCalculator()
        self.rpn = deque()
        self.result = ""
        self.saved_variables = {}
        self.stack = []
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

        # self.validated_expression = self.validator.validate(expression)
        # self.validated_expression = self.validate_and_change_to_deque(expression)
        if not self.validated_expression:
            print("Expression not valid")
            return False
            # TODO: Add functionality that will give an error to the user, that the expression was not valid

        # Test printing:
        print("Validated expression:")
        print(self.validated_expression)

        self.rpn = self.shunting_yard.start(self.validated_expression)
        if not self.rpn:
            print("Error: Expression not valid")
            return False


        self.result = self.result_calculator.calculate(self.rpn, self.single_arg_functions, self.double_arg_functions)

        print(f"Tulos on: {self.result}")


    def get_saved_variables(self):
        """Gets all the saved variables from the

        Returns:
            Dictionary: Includes all the saved variables
        """

        return self.saved_variables

