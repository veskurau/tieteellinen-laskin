import string
from collections import deque

class ShuntingYard:
    """Class, uses the shunting yard algorithm to transform an infix expression to a 
        postfix expression which is also known as the Reverse Polish Notation (RPN).

    Attributes:
        input_queue: Deque, holds the tokens of an expression in infix notation
        output_queue: Deque, holds the tokens of an expression in postfix notation
        operator_stack: List, used as a stack where the operators and functions 
                        are pushed and popped

    """

    def __init__(self):
        """Class constructor."""

        self.input_queue = deque()
        self.output_queue = deque()
        self.operator_stack = []

    def start(self, input_queue):
        """Starts the shunting yard algorithm and checks the input expression in infix notation
            and adds the tokens to the output expression which is in postfix notation.

        Args:
            input_queue (deque): Expression in infix notation

        Returns:

        """

        self.input_queue = input_queue

        #while len(self.input_queue) > 0:
        # Let's go over all the tokens in the input
        for token in self.input_queue:

            # Check the first character, if it is a number, then add to output
            if token[0] in string.digits:
                self.output_queue.append(token)

            # Check the first character, if it is letter a-z,
            # then it must be a function, add to operator stack
            elif token[0] in string.ascii_lowercase:
                self.operator_stack.append(token)

            # Check if token is a operator, add it to operator stack
            elif token[0] in "+-*/^":
                pass
                # TODO: comparison of operators in the stack etc.



    def get_output_queue(self):
        return self.output_queue

    def get_operator_stack(self):
        return self.operator_stack
