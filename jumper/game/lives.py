class Lives:
    """Lives class have the responssabilitie to track and update the player lives.

       Attributes:
                Lives(Interger), the number of lives from the current player."""

    def __init__(self) -> None:
        self.lives = 4

    def lives_counter(self, user_guess):
        lives = self.lives

        if user_guess == False:
            lives -= 1
            return lives

        elif user_guess == True:
            lives = self.lives
            return lives
