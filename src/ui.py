from calculator import Calculator

class UI:
    """Class, the interface which interacts with the user.
    
    Attributes:
        calculator: Calculator-object
    """
    
    def __init__(self):
        """Class constructor, which creates a new interface."""

        self._calculator = Calculator()