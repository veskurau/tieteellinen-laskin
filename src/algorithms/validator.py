import string
from collections import deque

# pylint: disable=all

class Validator:
    """Class, responsible for doing the initial check to a string-type infix expression,
        so that there are no invalid characters in the expression. The validator will parse
        the tokens and add them to a deque. 

    Attributes:
        expression_deque: Deque, holds the tokens of an expression in infix notation
        valid_operations: String, holds all valid arithmetic operations and parenthesis
        valid_functions: List, holds all valid functions in string-type

    """

    def __init__(self):
        """Class constructor, which creates a new calculator."""

        self.valid_operations = "+-*/^(),"
        self.valid_functions = ["min", "max", "sqrt", "sin"]

    def validate(self, expression):
        """Performs an initial validation of the infix expression, before it is
            entered to the shunting yard algorithm.
        
        Args:
            expression (str): Expression in infix notation.

        Returns:
            Deque: Expression in infix notation with the tokens parsed or
            False: If expression not valid
        """

        self.expression_deque = deque()

        self.expression_string = expression.replace(" ", "")
        self.i = 0

        while self.i < len(self.expression_string):

            # Situation where token is a number
            if self.expression_string[self.i] in string.digits:
                if not self._number_valid_and_processed():
                    return False
            
            # Situation where token is an operation
            elif self.expression_string[self.i] in self.valid_operations:
                self.expression_deque.append(self.expression_string[self.i])

            # Situation where a lowercase a-z is given, this might mean it is a function
            elif self.expression_string[self.i] in string.ascii_lowercase and self.i != len(self.expression_string)-1:
                if not _function_valid_and_processed():
                    return False

            # Situation where a uppercase A-Z is given, might be a saved variable, check the dict
            elif self.expression_string[self.i] in string.ascii_uppercase:
                if not _variable_valid_and_processed():
                    return False

            # Give error if an invalid character is given
            else:
                print(f"Error with character: {self.expression_string[self.i]}")
                return False
            self.i += 1
           
        return True



    def get_expression_deque(self):
        return self.expression_deque
    

    def _number_valid_and_processed(self):
        """Checks if a number is valid and if it is, then adds it as a token to the deque
        
        Returns:
            True: Number is valid and has been added to deque
            False: If number is not valid
        """

        numbers = self.expression_string[self.i]
                # Loop to check that if there are more digits or a decimal separator dot 
        while True: 
            if self.i == len(self.expression_string)-1: # Check that not the last character
                self.expression_deque.append(numbers)
                return True
            # Case if next character is a digit
            if self.expression_string[self.i+1] in string.digits:
                numbers = numbers + self.expression_string[self.i+1]
                self.i += 1
            # If it is a dot. Also checks that it is not the last character, it is followed by a digit,
            # and there is only one . in the token
            elif self.expression_string[self.i+1] == ".":
                if "." in numbers:
                    print("Error: Only one . can be in a decimal number!")
                    return False
                if self.i+1 == len(self.expression_string)-1:
                    print("Error: . cannot be the last character!")
                    return False
                if self.expression_string[self.i+2] not in string.digits:
                    print("Error: . must be followed by a digit")
                    return False
                numbers = numbers + self.expression_string[self.i+1]
                self.i += 1
            # If anything else than a digit or a dot, add the number to deque and brake
            else:
                self.expression_deque.append(numbers)
                return True

    def _function_valid_and_processed(self):
        pass
        # TODO: Check if a function is writen and add to deque
        # If function misspelled, give error
    
    def _variable_valid_and_processed(self):
        pass
        # TODO: Check the dictionary

    