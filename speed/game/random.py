import os
import random
class Randomizer:
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
    def word_extractor(self):
        PATH = os.path.dirname(os.path.abspath(__file__))
        LIBRARY = open(PATH + "/words.txt").read().splitlines()
        choice_01 = []
        x = []
        for x in range(5):
            one = random.choice(LIBRARY)
            choice_01.append(one)
        return choice_01