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

    def start_game(self):
        """Stats the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Get the inputs at the beginning of each round of play. In this case,
        that means asking the guesser for another letter.
        
        Args:
            self (Director): An instance of Director.
        """
        interface = self.puzzle.showinterface 
        #This one, is subejct for change depends 
        # on the puzzle class. I will get from the 
        # puzzle the name of method that will be 
        # assigned to get the to print the interface

        self.console.write(interface)
        letter = self.console.read_number("Guess a letter[a-z]: ")
        self.puzzle.letter(letter) #subject for change 

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, -------------------- add ------------------.

        Args:
            self (Director): An instance of Director.
        """

        #The lives will give an status to puzzle about the lives
        #added a comment
    
    
