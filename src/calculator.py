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

        self.expression = ""
        self.rpn = ""
        self.result = ""
        self.saved_variables = {}

    def start(self, expression):
        """Class constructor, which creates a new calculator. 

        Args:
            expression (str): Expression in infix notation.
            RPN (str): Expression in postfix notation.
        """

        self.expression = expression

        self.validate_expression(self.expression)
        self.infix_to_rpn(self.expression)
        self.rpn_to_result(self.rpn)

        return self.result


    def get_saved_variables(self):
        """Gets all the saved variables from the

        Returns:
            Dictionary: Includes all the saved variables
        """

        return self.saved_variables

    def validate_expression(self, expression):
        """Performs an initial validation of the infix expression, before it is
            entered to the shunting yard algorithm.
        
        Args:
            expression (str): Expression in infix notation.
        """

        pass
        # TODO: Add the necessary checks

    def infix_to_rpn(self, expression):
        """Uses the shunting yard algorithm to transform an infix expression to
            a postfix expression.

        Args: 
            expression (str): Expression in infix notation.

        Returns:
            String: Expression in postfix or Reverse Polish Notation
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

