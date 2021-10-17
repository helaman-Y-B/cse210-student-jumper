from game.lives import Lives

class Puzzle:
    """A code template for the puzzle that will be 
    responsible to will accept random words, will 
    hide the words from the player and will evaluate 
    the player entry letter if is true to the ramdom words
    
    Attributes:
        parachute man (list): a container for the parachute man interface
        intents (int): a number of intents for the player.
        dead main (list): a container for the parachute man inteface when it is dead
        letter (list): a container for the letter of a puzzle word.
        progress (int): for tracking the number of tries and progress of the player.
    """
    
    def __init__(self):
        """Initialize 

        Args:
            self (Puzzle): an instance of Puzzle
        """
        self.parachute_man = ["", "  ___", " /___\ ", " \   /", "  \ /", "   0", "  /|\ ", "  / \ ", "", "^^^^^^^", ""]
        self.intents = 4
        self.dead_man = ["Game over!\nSorry try again next game","", "   X", "  /|\ ", "  / \ ", "", "^^^^^^^", ""]
        self.letters = []
        self.progress = 0
            
    def set_word(self, word):
        """Sets the word to initialize the game interface.
        Args:
            word: the word chosen randomly.
        """
        self.word = word
        self.word_interface = ""
        
        for _ in word:
            self.word_interface += "_ "

    def interface(self):
        """It generates the game interface.
        Args:
            score: current score.
        """
    
        data = [self.word_interface, ]
        
        for i in self.parachute_man:
            data.append(i)
        
        if len(self.parachute_man) == 7:
            return self.dead_man
        else:
            return data

    def question(self):
        """It returns the game's question.
        """
        main_question = "Guess a letter [a-z]: "
        
        return main_question
        
    def evaluate(self, letter):
        """It compares the current letter with the word and sets the new interface.
        Args:
            letter: this is a letter inputted from the player.
        """
        if letter in self.word and letter not in self.letters:
            
            cur_index = []
            counter = 0
            for i in list(self.word):
                if letter in i:
                    cur_index.append(counter)
                counter +=1

            for i in cur_index:
                lister = list(self.word_interface)
                index = i * 2
                lister[index] = letter
                self.word_interface = "".join(lister)
                self.letters.append(letter)
                self.progress += 1
            return True
        else:
            self.intents -= 1
            self.parachute_man.pop(1)
            return False
        
    def dead_man(self):
        """Returns self.dead_man when the game ends
        
        Args: 
            self (Puzzle): an instance of Puzzle
        """
        return self.dead_man
        
    def survivor_man(self):
        """
        Return a message for the console if the player wins the game!

        Args: 
            self (Puzzle): an instance of Puzzle
        """
        survivor = "Hooray you guess it right!\nCongratulations, you survived!"
        return survivor
            
        
            
            
            
            
