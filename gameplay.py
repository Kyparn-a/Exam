class Player:
    def __init__(self, user, highscore, points, isBust):
        self.user = user
        self.highscore = highscore
        self.points = points
        self.isBust = isBust
    def displayResult(self):
        return self.user, self.points
    
    def displayHighscore(self):
        return self.highscore
    
    def increaseHighscore(self, value):
        self.highscore += value
        return
    
    def resetHighscore(self):
        self.highscore = 0
        return
    
    def increaseScore(self, roll_result):
        self.points += roll_result
        if self.points > 21:
            self.goBust()
    
    def getResult(self, value):
        roundResult = self.points - value

        return roundResult

    def newRound(self):
        self.points = 0
        self.isBust = False
        return

    def goBust(self):
        self.isBust = True
        return

class Game:
    def __init__(self, filename, highscores, stop, rollresult):
        self.filename = filename
        self.highscores = highscores
        self.stop = stop
        self.roll_result = rollresult

    def play_menu(self):
        print("--- Choices ---")
        print("1. Roll the dice")
        print("2. Stop rolling")

    def reroll_menu(self):
        print("1. Roll again")
        print("2. Stop ")

    def playagain_menu(self):
        print("1. Yes")
        print("2. No")
    
    def read_file(self, name):
        print("Loading highscore")
        try:
            with open(name) as file:
                return list(map(lambda row: row.strip(), file))
        except FileNotFoundError:
            print("No Highscores available")
            return[]
            
    def save_file(self, name, highscores):
        print("Saving highscores to file")
        try:
            with open(name, "w") as file:
                for highscore in highscores:
                    file.write(f"{highscore}\n")
        except OSError:
            print("Highscore could not be saved")
        else:
            print("Highscores saved!")
    
    def roundEnd(self, user, dealer):
        print(f"Round Results:\n{user.displayResult()}\n{dealer.displayResult()}")
        result = user.getResult(dealer.points) 
        if result > 0 or dealer.isBust == True:
            print("Player Wins!")
            user.increaseHighscore(1)
            dealer.resetHighscore()
        elif result < 0 and dealer.isBust == False:
            print("WIN TEST", user.displayResult())
            print(" Dealer Wins!")
            dealer.increaseHighscore(1)
            user.resetHighscore()
        else:
            print("Draw!")




    
