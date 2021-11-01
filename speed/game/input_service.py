import sys
from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self):

        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self.screen = Screen
        
    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        result = ""
        event = Screen.get_key(Screen)
        if not event is None:
            if event == 27:
                sys.exit()
        return result