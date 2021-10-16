from game.console import Console
from game.generate_word import Word
from game.lives import Lives
from game.player_guesser import Player
from game.puzzle import Puzzle

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director
        """

        self.console = Console()
        self.guesser = Player()
        self.keep_playing = True
        self.puzzle = Puzzle()
        self.lives = Lives()
        self.word = Word()