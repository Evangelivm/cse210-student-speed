from time import sleep
from game import constants
from game.input_word import InputWord
from game.score import Score
import random
from game.input_service import InputService
from game.output_service import OutputService
from game.random import Randomizer
from asciimatics.screen import Screen

class Director:
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
            self (Director): an instance of Director.
        """
        
        self.input_service = InputService()
        self._keep_playing = True
        self.output_service = OutputService()
        self._random = Randomizer()
        self._inputword = InputWord()
        self._score = Score()
        self.points = 0
        self.list = []
        self.buffer = []
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        self.list = self._random.word_extractor()
        def demo(screen):
            choice_02 = self.list
            numbe_x = 5
            for x in range(numbe_x):
                number_x = random.randint(1,60)
                number_y = random.randint(2,10)
                screen.print_at("----------------------------------------------------------------------------------------", 0, 1)
                screen.refresh()
                screen.print_at("----------------------------------------------------------------------------------------", 0, 15)
                screen.refresh()
                screen.print_at(f"Buffer: {self.buffer}", 0, 16)
                screen.refresh()
                screen.print_at(choice_02[x], number_x, number_y)
                x = x + 1
            sleep(2)
        Screen.wrapper(demo)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self.input_service.get_letter()
        self.answer = self._inputword.input()
        list_02 = self.list 
        self.points = 0
        if self.answer in list_02:
            self.buffer.append(self.answer)
            self.points = self.points + 1
            self._score.correct_answer(self.points)
        if self.answer == None:
            print("Come on, you can do it!!!!")
            sleep(2)
            return


    def _handle_body_collision(self):
        """Handles collisions between the snake's head and body. Stops the game 
        if there is one.

        Args:
            self (Director): An instance of Director.
        """
        head = self._snake.get_head()
        body = self._snake.get_body()
        for segment in body:
            if head.get_position().equals(segment.get_position()):
                self._keep_playing = False
                break

    def _handle_food_collision(self):
        """Handles collisions between the snake's head and the food. Grows the 
        snake, updates the score and moves the food if there is one.

        Args:
            self (Director): An instance of Director.
        """
        head = self._snake.get_head()
        if head.get_position().equals(self._food.get_position()):
            points = self._food.get_points()
            for n in range(points):
                self._snake.grow_tail()
            self._score.add_points(points)
            self._food.reset() 