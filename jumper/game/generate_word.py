import random

class Word:
    """A code template for a random word generator. It will responsible for the randomly picking a word 
    from a list or a file.
    
    Stereotype:
        Information Holder

    Attributes:
        list_words (list): The list of words that will randomly pick a word from it.

    """

    def __init__(self):
        """Class constructor. Declare and initializes instance attributes.

        Args:
            self (Word): An instance of Word
        """
        self.list_words = []

        with open("../wordlist.txt", "rt") as words:
        
            for word in words:
                clean_line = word.strip()
                if len(clean_line) <=3:
                    pass
                else:
                    self.list_words.append(clean_line)

        self.random_number = random.randint(0, len(self.list_words)-1)

    def random_word(self):
        """Pick random words from the list of words
            
        Args:
            self(Word) : An instance of Word
                
        Return:
            string: A randomly picked word"""

        return self.list_words[self.random_number]