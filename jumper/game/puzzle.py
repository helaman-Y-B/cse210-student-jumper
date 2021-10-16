# ~ will accept rambom words
# ~ will hide it from the player
# ~ will evaluate the player entry letter if is true to the ramdom words
# print guess a letter

class Puzzle:
    
    def __init__(self):
        """Initialize 
        """
        
        self.parachute_man = ["", "  ___", " /___\ ", " \   /", "  \ /", "   0", "  /|\ ", "  / \ ", "", "^^^^^^^", ""]
        # ~ for i in parachute_man:
            # ~ print(i)
        # ~ self.score = 4
        self.intents = 4
            
    def set_word(self, word):
        """Sets the word to initialize the game interface.
        Args:
            word: the word chosen randomly.
        """

        
        
        self.word = word
        self.word_interface = ""
        
        for _ in word:
            self.word_interface += "_ "

        
        
    def interface(self, lives):
        """It generates the game interface.
        Args:
            score: current score.
        """

        
        if self.intents < lives:
            
            self.parachute_man.pop(1)
        
        
        data = [self.word_interface, ]
        
        for i in self.parachute_man:
            data.append(i)
        
        return data
        
        
    def question(self):
        """It returns the game's question.
        """

        
        main_question = "Guess a letter [a-z]: "
        
        return main_question
        
    def evaluate(self, letter):
        """It compares the current letter with the word and sets the new interface.
        Args:
            letter: current score.
        """

        
        if letter in self.word:
            lister = list(self.word_interface)
            index = self.word.index(letter)* 2
            lister[index] = letter
            self.word_interface = "".join(lister)
            return True
            
        else:
            self.intents -= 1
            return False
            
            
            
            
        
        
        

        


starter = Puzzle()

starter.set_word("nicolas")
print(starter.question())
for i in starter.interface(4):
    print(i)
    
starter.evaluate("i")
for i in starter.interface(4):
    print(i)

