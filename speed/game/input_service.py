
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
        
    def demo(self):
        final_text = f"  _______ _                 _                         \
\n |__   __| |               | |                        \
\n    | |  | |__   __ _ _ __ | | __  _   _  ___  _   _  \
\n    | |  | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | \
\n    | |  | | | | (_| | | | |   <  | |_| | (_) | |_| | \
\n    |_|  |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_| \
\n                                    __/ |             \
\n                                   |___/              "
        return print(final_text)