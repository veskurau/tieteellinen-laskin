class Calculator:
    """Class, responsible for the application logic.....
    
    Attributes:
        expression: String, holds the expression in infix notation, given by the user
    
    """

    def __init__(self):
        """Class constructor, which creates a new calculator."""

        self._expression = ""

    def start(self, expression):
        """Class constructor, which creates a new calculator. 

        Args:
            expression (str): Expression in infix notation.
        """

        self._expression = expression

