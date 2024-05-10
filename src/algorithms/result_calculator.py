import math
import string
from collections import deque

class ResultCalculator:
    """Class, uses a list as a stack to calculate the result from a postfix expression.
    
    Attributes:
        postfix_queue: Deque, holds the tokens of an expression in postfix notation
        token_stack: List, used as a stack where the tokens
        single_arg_functions (list): All valid single argument functions
        double_arg_functions (list): All valid double argument functions

    """

    def __init__(self):
        self.postfix_queue = deque()
        self.token_stack = []
        self.single_arg_functions = []
        self.double_arg_functions = []


    def calculate(self, expression, single_arg_functions, double_arg_functions):
        """Uses a stack to calculate the result of a postfix expression.

        Args: 
            expression (deque): Expression in postfix notation.
            single_arg_functions (list): All valid single argument functions
            double_arg_functions (list): All valid double argument functions

        Returns:
            String: Result of the expression
        """

        self.postfix_queue = expression
        self.single_arg_functions = single_arg_functions
        self.double_arg_functions = double_arg_functions
        self.token_stack = []

        for token in self.postfix_queue:
            try:
                if token[0] in string.digits:
                    self.token_stack.append(token)
                elif token in self.single_arg_functions:
                    if len(self.token_stack) < 1:
                        print(f"Error: One argument must be given to function {token}")
                        return False
                    first_number = self.token_stack.pop()
                    if len(self.token_stack) > 0 and token == self.postfix_queue[-1]:
                        if self.token_stack[len(self.token_stack)-1] in string.digits:
                            print(f"Error: Too many arguments given to function {token}")
                            return False
                    self.token_stack.append(str(eval(f"math.{token}({first_number})")))
                elif token in self.double_arg_functions:
                    if len(self.token_stack) < 2:
                        print(f"Error: Two arguments must be given to function {token}")
                        return False
                    first_number = self.token_stack.pop()
                    second_number = self.token_stack.pop()
                    if len(self.token_stack) > 0 and token == self.postfix_queue[-1]:
                        if self.token_stack[len(self.token_stack)-1] in string.digits:
                            print(f"Error: Too many arguments given to function {token}")
                            return False
                    self.token_stack.append(str(eval(f"{token}({second_number, first_number})")))
                elif token == "^":
                    first_number = self.token_stack.pop()
                    if len(self.token_stack) == 0:
                        print("Error: Operations used incorrectly")
                        return False
                    second_number = self.token_stack.pop()
                    self.token_stack.append(str(eval(f"{second_number}**{first_number}")))
                else: # All other operations besides power
                    first_number = self.token_stack.pop()
                    if len(self.token_stack) == 0:
                        print("Error: Operations used incorrectly")
                        return False
                    second_number = self.token_stack.pop()
                    if token == "/" and first_number == "0":
                        print("Error: You can not divide by zero")
                        return False
                    self.token_stack.append(str(eval(f"{second_number}{token}{first_number}")))
            except ValueError:
                print("Error: Result is too large")
                return False
            except:
                print("Error: Input incorrect, try again")
                return False

        return self.token_stack[0]
