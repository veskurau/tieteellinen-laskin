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
        self.output_queue = deque()
        self.operator_stack = []

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

            # Check if token is an operator, add it to operator stack accordingly
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
            
            elif token[0] == ")":
                top_operator = self.get_top_operator_from_stack()
                while top_operator != "(":
                    # If operator stack is empty, there was no left paranthesis in the stack to pair up with this right one
                    if not top_operator:
                        print("Error: Mismatched parenthesis")
                        return False
                    # Add operators from operator stack to ouput queue until ( is on top
                    self.output_queue.append(self.operator_stack.pop())
                    top_operator = self.get_top_operator_from_stack()
                # Now we have ( on top of the stack, let's discard it
                self.operator_stack.pop()

                # If top operator in stack is a function, pop it to output queue
                top_operator = self.get_top_operator_from_stack()
                if top_operator:
                    if top_operator[0] in string.ascii_lowercase:
                        self.output_queue.append(self.operator_stack.pop())

        # Pop the remaining operators from the stack to the output queue
        while True:
            top_operator = self.get_top_operator_from_stack()
            # When stack is empty, the job is done
            if not top_operator:
                break
            # There shouldn't be any parenthesesis in the stack
            if top_operator in "()":
                print("Error: Mismatched parenthesis")
                return False
            
            self.output_queue.append(self.operator_stack.pop())
            
        # TODO poista tulostukset kun et enää tarvitse
        print()
        print("Shunting yardin jälkeen:")
        print(f"Input infix muodossa: {self.input_queue}")
        print(f"Output postfix muodossa: {self.output_queue}")
        print()
        return self.output_queue


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
