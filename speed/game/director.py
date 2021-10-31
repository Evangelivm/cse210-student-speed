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

    def parameters (self):
        self._score = Score()
        self._snake = Randomizer()
        self._inputword = InputWord()
        
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
        def demo(self,screen):
            self.choice_01 = []
            self.x = []
            number_x = 5
            for x in range(number_x):
                number_x = random.randint(1,60)
                number_y = random.randint(2,10)
                screen.print_at("----------------------------------------------------------------------------------------", 0, 1)
                screen.print_at("----------------------------------------------------------------------------------------", 0, 15)
                screen.print_at("Buffer: ", 0, 16)
                screen.print_at(self.choice_01[x], number_x, number_y)
                #dejarlo en 0.9
                x = x + 1
            screen.refresh()
        Screen.wrapper(demo)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._handle_body_collision()
        self._handle_food_collision()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._food)
        self._output_service.draw_actors(self._snake.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

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