from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

class Final:
    """This part is intended to show the final part of the game.
    
    Stereotype:
        Service Provider
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Final): an instance of Final"""
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