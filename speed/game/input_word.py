import time
from threading import Thread
class InputWord:
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

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): a"""
    def input(self):
        answer = None
        def check():
            time.sleep(2)
            if answer != None:
                return
            print("Too Slow, press enter")
        Thread(target = check).start()
        answer = input("Input something: ")
        return answer