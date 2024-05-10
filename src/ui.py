from calculator import Calculator


class UI:
    """Class, the interface which interacts with the user.

    Attributes:
        calculator: Calculator-object
    """

    def __init__(self):
        """Class constructor, which creates a new interface."""

        self._calculator = Calculator()

    def start(self):
        """Starts up the interface for the user."""
        
        print()
        print("Welcome to the Scientific Calculator!")

        while True:
            print()
            print("Actions:")
            print()
            print("1) Enter expression")
            print("2) Show saved variables")
            print("I) Show instructions")
            print("X) Exit calculator")
            print()
            user_input = input("Enter action: ")

            if user_input == "X":
                print("Good bye!")
                break
            elif user_input == "I":
                self._show_instructions()
            elif user_input == "1":
                self._enter_expression()
            elif user_input == "2":
                print()
                print("Saved variables:")
                print(self._get_saved_variables())
            else:
                print("Incorrect input, please try again!")

    def _show_instructions(self):
        print()
        print("The allowed inputs:")
        print()
        print("- Integers")
        print("- Decimal numbers using a decimal point")
        print("- Parenthesis ()")
        print("- Operations +, -, *, /, ^")
        print("- One argument functions sqrt, sin, cos, tan (e.g. sqrt(9))")
        print("- Two argument functions max, min (e.g. max(1,2))")
        print()

    def _enter_expression(self):
        expression = input("Enter expression: ")
        result = self._calculator.start(expression)
        if result:
            print()
            print(f"The result is: {result}")
            print()
            save_result = input("Do you want to save the result (y)? ")
            if save_result == "y":
                self._calculator.save_result_to_variable(result)
                variable = self._calculator.get_last_saved_variable()
                print()
                print(f"The result {result} has been saved to variable {variable}")

    def _get_saved_variables(self):
        return self._calculator.get_saved_variables()
