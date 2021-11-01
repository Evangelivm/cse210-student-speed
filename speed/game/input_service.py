
from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen

class InputService:
    """Helps with the final part to print when the user press ESC
    Stereotype: 
        Service Provider"""



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