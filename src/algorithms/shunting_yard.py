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
        operator_precedence: Dictionary, holds the precedence-value for each operation

    """

    def __init__(self):
        """Class constructor."""

        self.input_queue = deque()
        self.output_queue = deque()
        self.operator_stack = []
        self.operator_precedence = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2}

    def start(self, input_queue):
        """Starts the shunting yard algorithm and checks the input expression in infix notation
            and adds the tokens to the output expression which is in postfix notation.

        Args:
            input_queue (deque): Expression in infix notation

        Returns:

        """

        self.input_queue = input_queue

        # while len(self.input_queue) > 0:
        # Let's go over all the tokens in the input
        for token in self.input_queue:

            # Check the first character, if it is a number, then add to output
            if token[0] in string.digits:
                self.output_queue.append(token)

            # Check the first character, if it is letter a-z,
            # then it must be a function, add to operator stack
            elif token[0] in string.ascii_lowercase:
                self.operator_stack.append(token)

            # Check if token is a operator, add it to operator stack accordingly
            elif token[0] in "+-*/^":
                while True:
                    top_operator = self.get_top_operator_from_stack()
                    if not top_operator:
                        break
                    if top_operator != "(":
                        if (self.operator_precedence[top_operator] > self.operator_precedence[token[0]] 
                        or (self.operator_precedence[top_operator] == self.operator_precedence[token[0]] and token[0] != "^")):
                            self.output_queue.append(self.operator_stack.pop())
                        else:
                            break
                    else:
                        break
                        
                self.operator_stack.append(token[0])

            elif token[0] == ",":
                while True:
                    top_operator = self.get_top_operator_from_stack()
                    if top_operator == "(":
                        break
                    self.output_queue.append(self.operator_stack.pop())

            elif token[0] == "(":
                self.operator_stack.append(token[0])



    def get_output_queue(self):
        return self.output_queue

    def get_operator_stack(self):
        return self.operator_stack

    def get_top_operator_from_stack(self):
        tokens_in_stack = len(self.operator_stack)
        if tokens_in_stack == 0:
            return None
        else:
            return self.operator_stack[tokens_in_stack-1]
