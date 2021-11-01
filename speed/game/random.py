import os
import random
class Randomizer:
    """This part processes all the random processes of the words.
    
    Stereotype:
        Service Provider

    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Randomizer): an instance of Randomizer"""
        self.word_list = []

    def word_extractor(self):
        PATH = os.path.dirname(os.path.abspath(__file__))
        LIBRARY = open(PATH + "/words.txt").read().splitlines()
        choice_01 = []
        x = []
        for x in range(5):
            one = random.choice(LIBRARY)
            choice_01.append(one)
            self.word_list.append(one)
        return choice_01
