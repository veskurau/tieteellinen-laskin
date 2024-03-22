import string
from collections import deque

# pylint: disable=all

class Calculator:
    """Class, responsible for the application logic.
    
    Attributes:
        expression: String, holds the expression in infix notation, given by the user
        rpn: String, holds the expression in postfix notation or Reverse Polish notation
        saved_variables: Dictionary, keeps track of the saved results. 
                         Key is the variable name and value is the result.

    """

    def __init__(self):
        """Class constructor, which creates a new calculator."""

        self.rpn = deque()
        self.result = ""
        self.saved_variables = {}
        self.stack = []


    def start(self, expression):
        """Class constructor, which creates a new calculator. 

        Args:
            expression (str): Expression in infix notation.
            RPN (str): Expression in postfix notation.
        """

        validated_expression = self.validate_and_change_to_deque(expression)
        if not validated_expression:
            print("Expression not valid")
            return False
            # TODO: Add functionality that will give an error to the user, that the expression was not valid

        
        # Test printing:
        print("Valitated expression:")
        print(validated_expression)


        # self.infix_to_rpn(validated_expression)
        # self.rpn_to_result(self.rpn)

        # return self.result


    def get_saved_variables(self):
        """Gets all the saved variables from the

        Returns:
            Dictionary: Includes all the saved variables
        """

        return self.saved_variables

    def validate_and_change_to_deque(self, expression):
        """Performs an initial validation of the infix expression, before it is
            entered to the shunting yard algorithm.
        
        Args:
            expression (str): Expression in infix notation.

        Returns:
            Deque: Expression in infix notation or
            False: If expression not valid
        """


        valid_non_numbers = "+-*/^(),"
        valid_functions = ["min", "max", "sqrt", "sin"]

        expression_deque = deque()

        expression_string = expression.replace(" ", "")
        
        for i in range(0, len(expression_string)):
            # Situation where token is a number
            if expression_string[i] in string.digits:
                numbers = expression_string[i]
                # Loop to check that if there are more digits or a decimal separator dot 
                while True: 
                    if i == len(expression_string)-1: # Check that not the last character
                        expression_deque.append(numbers)
                        break
                    # Case if next character is a digit
                    if expression_string[i+1] in string.digits:
                        numbers = numbers + expression_string[i+1]
                        i += 1
                    # If it is a dot. Also checks that it is not the last character, it is followed by a digit,
                    # and there is only one . in the token
                    elif expression_string[i+1] == "." and "." not in numbers:
                        if i+1 == len(expression_string):
                            print("Error: . cannot be the last character!")
                            return False
                        if expression_string[i+2] not in string.digits:
                            print("Error: . must be followed by a digit")
                            return False
                        numbers = numbers + expression_string[i+1]
                        i += 1
                    # If anything else than a digit or a dot, add the number to deque and brake
                    else:
                        expression_deque.append(numbers)
                        break
            
            # Situation where token is a non number
            elif expression_string[i] in valid_non_numbers:
                expression_deque.append(expression_string[i])

            # Situation where a lowercase a-z is given, this might mean a function
            elif expression_string[i] in string.ascii_lowercase:
                pass
                # TODO: Check if a function is writen and add to deque
                # If function misspelled, give error

            # Situation where a uppercase A-Z is given, might be a saved variable, check the dict
            elif expression_string[i] in string.ascii_uppercase:
                pass
                # TODO: Check the dictionary

            # Give error if an invalid character is given
            else:
                print(f"{expression_string[i]} is not a valid character")
                return False
                
            

        # test printing
        print("Expression string:")
        print(expression_string)

        return expression_string



    def infix_to_rpn(self, expression):
        """Uses the shunting yard algorithm to transform an infix expression to
            a postfix expression.

        Args: 
            expression (str): Expression in infix notation.

        Returns:
            Deque: Expression in postfix / Reverse Polish Notation
        """
        pass
        # TODO: Shunting yard algorithm comes here

    def rpn_to_result(self, rpn):
        """Uses a stack to calculate the result of a postfix expression.

        Args: 
            rpn (str): Expression in postfix notation.

        Returns:
            String: Result of the expression
        """
        pass 
        # TODO: Create the function

