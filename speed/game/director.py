from time import sleep
from game import constants
from game.input_word import InputWord
from game.score import Score
import random
from game.input_service import InputService
from game.output_service import OutputService
from game.random import Randomizer
from game.intro import Intro
from asciimatics.screen import Screen
from game.final import Final



class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        self.input_service (InputService): The input mechanism.
        self._keep_playing (boolean): make the game continue
        self.output_service (OutputService): The output mechanism.
        self._random (Randomizer): The random mechanism.
        self._inputword (InputWord): The mechanism works with the input.
        self._intro (Intro): The intro mechanism.
        self._score (Score): The score mechanism.
        self.points (Number): The current score.
        self.list (List): The list of words.
        self.buffer (List): The list of the buffer.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        
        self.input_service = InputService()
        self._keep_playing = True
        self.output_service = OutputService()
        self._random = Randomizer()
        self._inputword = InputWord()
        self._intro = Intro()
        self._score = Score()
        self._final = Final()
        self.points = 0
        self.list = []
        self.buffer = []
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._intro.introduction()
        while self._keep_playing:
            self._get_inputs()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. 

        Args:
            self (Director): An instance of Director.
        """
        self.list = self._random.word_extractor()
        def demo(screen):
            choice_02 = self.list
            numbe_x = 5
            x = 0
            for x in range(numbe_x):
                number_x = random.randint(1,60)
                number_y = random.randint(2,10)
                screen.print_at("----------------------------------------------------------------------------------------", 0, 1, colour = 3)
                screen.refresh()
                screen.print_at("----------------------------------------------------------------------------------------", 0, 15, colour = 3)
                screen.refresh()
                screen.print_at(f"Buffer: {self.buffer}", 0, 16, colour = 2)
                screen.refresh()
                screen.print_at(f"Points: {self.points}", 0, 17, colour = 2)
                screen.refresh()
                screen.print_at(f"--------To exit, press ESC several times", 0, 17, colour = 4)
                screen.refresh()
                screen.print_at(choice_02[x], number_x, number_y, colour = 5)
                x = x + 1
            sleep(2)
        Screen.wrapper(demo)

        
    def _do_outputs(self):
        """Process the important game information for each round of play. 

        Args:
            self (Director): An instance of Director.
        """
        def demo(x):
            one =x.get_event()
            return one
        if Screen.wrapper(demo) != None:
            self.input_service.demo()
            self._final.final()
        else:
            self.answer = self._inputword.input()
            list_02 = self.list 
            if self.answer in list_02:
                self.buffer.append(self.answer)
                points = len(self.buffer)
                point = self._score.correct_answer(points)
                self.points = point
                self.output_service.screen()