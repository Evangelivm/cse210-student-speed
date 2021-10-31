from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

class Final:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): a"""
    def doit(screen):
        effects =[
            Cycle(
                screen,
                FigletText("Thanks for playing",font="big"),
                int(screen.height/2-8)),
            Cycle(
                screen,
                FigletText("Close for exit",font="small"),
                int(screen.height/2-0)),
            Stars(screen,200)
        ]
        screen.play([Scene(effects,-1)])
    Screen.wrapper(doit,catch_interrupt=True)