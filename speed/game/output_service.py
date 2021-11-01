from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import text
import random
class OutputService:
    """Display words of encouragement each time the user answers correctly.
    
    Stereotype:
        Service Provider
"""
    def screen(self):
        phrases = ['you did it', "great", "congrats", "good eye"]
        return print(random.choice(phrases))
