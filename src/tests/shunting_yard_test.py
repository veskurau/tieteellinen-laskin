import unittest
from collections import deque
from algorithms.shunting_yard import ShuntingYard

# FROM COMMAND LINE: coverage run --branch -m pytest src; coverage html


class TestShuntingYard(unittest.TestCase):
    """Tests for ShuntingYard class, which is responsible for transforming the infix expression to
        a postfix expression.

    Attributes:
        shunting_yard: ShuntingYard, gives access to class ShuntingYard
        input_queue: Deque, holds the expressions tokens in infix notation
        output_queue: Deque, holds the epxressions tokens in postfix notation
        operator_stack: List, used as a stack where the operators and functions 
                        are pushed and popped

    """

    def setUp(self):
        self.shunting_yard = ShuntingYard()
        self.input_queue = deque()
        self.output_queue = deque()
        self.operator_stack = []

    def test_number_is_added_to_output_queue(self):
        self.input_queue.append("501")
        self.output_queue.append("501")

        self.shunting_yard.start(self.input_queue)
        returned = self.shunting_yard.get_output_queue()
        self.assertEqual(returned, self.output_queue)

    def test_function_is_added_to_operator_stack_and_popped_to_output(self):
        self.input_queue.append("max")
        self.output_queue.append("max")

        self.shunting_yard.start(self.input_queue)
        returned1 = self.shunting_yard.get_operator_stack()
        returned2 = self.shunting_yard.get_output_queue()
        self.assertEqual(returned1, self.operator_stack)
        self.assertEqual(returned2, self.output_queue)

    def test_operator_is_pushed_to_empty_operator_stack(self):
        self.input_queue.append("+")
        self.output_queue.append("+")

        self.shunting_yard.start(self.input_queue)
        returned1 = self.shunting_yard.get_operator_stack()
        returned2 = self.shunting_yard.get_output_queue()
        self.assertEqual(returned1, self.operator_stack)
        self.assertEqual(returned2, self.output_queue)

    def test_operator_stack_top_operator_has_lower_precedence(self):
        """The operator with the higher precedence will be pushed
            on top of the stack.
        """

        self.input_queue.append("*")
        self.output_queue.append("*")
        self.output_queue.append("+")
        self.shunting_yard.operator_stack.append("+")


        self.shunting_yard.start(self.input_queue)
        returned1 = self.shunting_yard.get_operator_stack()
        returned2 = self.shunting_yard.get_output_queue()
        self.assertEqual(returned1, self.operator_stack)
        self.assertEqual(returned2, self.output_queue)

    def test_operator_stack_top_operator_has_higher_precedence(self):
        """The top operator with higher precedence will be popped off the 
            stack and to output queue. The operator with lower precedence
            will be pushed to operator stack.
        """

        self.input_queue.append("+")
        self.output_queue.append("^")
        self.output_queue.append("+")
        self.shunting_yard.operator_stack.append("^")


        self.shunting_yard.start(self.input_queue)
        returned1 = self.shunting_yard.get_operator_stack()
        returned2 = self.shunting_yard.get_output_queue()
        self.assertEqual(returned1, self.operator_stack)
        self.assertEqual(returned2, self.output_queue)

    def test_operator_stack_top_operator_has_same_precedence(self):
        """The top operator with same precedence will be popped off the 
            stack and to output queue. The operator with lower precedence
            will be pushed to operator stack.
        """
        
        self.input_queue.append("*")
        self.output_queue.append("/")
        self.output_queue.append("*")
        self.shunting_yard.operator_stack.append("/")


        self.shunting_yard.start(self.input_queue)
        returned1 = self.shunting_yard.get_operator_stack()
        returned2 = self.shunting_yard.get_output_queue()
        self.assertEqual(returned1, self.operator_stack)
        self.assertEqual(returned2, self.output_queue)

    def test_operator_stack_top_operator_has_same_precedence_and_both_are_power_operators(self):
        """The top operator is now ^ and the input operator is ^. Input operator will be pushed
            on top of the operator stack. 
        """
        
        self.input_queue.append("^")
        self.output_queue.append("^")
        self.output_queue.append("^")
        self.shunting_yard.operator_stack.append("^")


        self.shunting_yard.start(self.input_queue)
        returned1 = self.shunting_yard.get_operator_stack()
        returned2 = self.shunting_yard.get_output_queue()
        self.assertEqual(returned1, self.operator_stack)
        self.assertEqual(returned2, self.output_queue)

    def test_operator_stack_top_operator_is_left_parantheses(self):
        """The top operator is now (, so the input operator is pushed to stack."""
        
        self.input_queue.append("+")
        self.operator_stack.append("(")
        self.output_queue.append("+")
        self.shunting_yard.operator_stack.append("(")


        self.shunting_yard.start(self.input_queue)
        returned1 = self.shunting_yard.get_operator_stack()
        returned2 = self.shunting_yard.get_output_queue()
        self.assertEqual(returned1, self.operator_stack)
        self.assertEqual(returned2, self.output_queue)

    def test_if_input_operator_is_comma_all_operators_popped_from_stack_until_left_parantheses(self):        
        self.input_queue.append(",")
        self.operator_stack.append("sin")
        self.operator_stack.append("(")
        self.operator_stack.append("max")
        self.output_queue.append(self.operator_stack.pop())

        self.shunting_yard.operator_stack.append("sin")
        self.shunting_yard.operator_stack.append("(")
        self.shunting_yard.operator_stack.append("max")


        self.shunting_yard.start(self.input_queue)
        returned1 = self.shunting_yard.get_operator_stack()
        returned2 = self.shunting_yard.get_output_queue()
        self.assertEqual(returned1, self.operator_stack)
        self.assertEqual(returned2, self.output_queue)

    def test_left_paranthesis_is_pushed_to_stack(self):
        self.input_queue.append("(")
        self.operator_stack.append("(")

        self.shunting_yard.start(self.input_queue)
        returned = self.shunting_yard.get_operator_stack()
        self.assertEqual(returned, self.operator_stack)

    def test_right_paranthesis_is_processed_correctly_when_left_paranthesis_is_found(self):
        self.input_queue.append(")")
        self.output_queue.append("+")

        self.shunting_yard.operator_stack.append("+")
        self.shunting_yard.operator_stack.append("(")

        self.shunting_yard.start(self.input_queue)
        returned1 = self.shunting_yard.get_operator_stack()
        returned2 = self.shunting_yard.get_output_queue()
        self.assertEqual(returned1, self.operator_stack)
        self.assertEqual(returned2, self.output_queue)

    def test_right_paranthesis_is_processed_correctly_when_stack_empty(self):
        self.input_queue.append(")")

        returned = self.shunting_yard.start(self.input_queue)
        self.assertEqual(returned, False)

    def test_if_there_are_left_over_paranthesis_in_stack(self):
        self.input_queue.append(")")

        self.shunting_yard.operator_stack.append("(")
        self.shunting_yard.operator_stack.append("(")

        returned = self.shunting_yard.start(self.input_queue)
        self.assertEqual(returned, False)
