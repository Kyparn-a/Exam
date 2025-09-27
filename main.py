from gameplay import Player, Game
import random

def start():
    file_name = "highscores.txt"
    game = Game("highscores.txt", "", False, 0)
    highscores = game.read_file(file_name)
    stop = False
    user = Player("Player", 0, 0, False)
    dealer = Player("Dealer", 0, 0, False)
    roll_result = 0
    print(highscores)
    while True:
        if stop == False and user.isBust == False:
            print(f"-- Current Highscores -- \nPlayer:{user.highscore}\nDealer: {dealer.highscore}")
            game.play_menu()
            try:
                choice = int(input("Choose an option1 (1-2): "))
                if choice > 2 or choice <= 0:
                    raise ValueError()
            except ValueError:
                print("Invalid Choice, You can only choose between options 1-2")
                continue
            if choice == 1:
                print("Rolling the dice")
                roll_result = random.randrange(1,7)
                user.increaseScore(roll_result)
                while True:
                    print(f"Roll Result: {roll_result}")
                    print(f"Current total: {user.points}")
                    game.reroll_menu()
                    try: 
                        choice = int(input("Do you want to roll again?\n"))
                        if choice > 2 or choice <= 0:
                            raise ValueError()
                    except ValueError:
                        print("Invalid Choice, You can only choose between options 1-2")
                        continue              
                        
                    if choice == 1:
                        print("rolling again")
                        roll_result = random.randrange(1,7)
                        user.increaseScore(roll_result)
                        if user.points > 21:
                            print("You went bust")
                            print(f"Current total: {user.points}")
                            user.isBust = True
                            break
                    elif choice == 2:
                        stop = True
                        break
                
            elif choice == 2:
                stop = True
                print("Player turn ended\n Dealer turn starting")
                break
            else:
                print("Player total: ")
                print("\nDealer total: ")
                print("\nDo you want to play again?")

        elif stop == True and dealer.points <= 17 and dealer.isBust == False:
            
            roll_result = random.randrange(1,7)
            print(f"Dealer rolls: {roll_result}")
            dealer.increaseScore(roll_result)
            print(f"Dealer total is: {dealer.points}")
            if dealer.points > 21:
                print("Dealer went bust")
                dealer.isBust = True
                
        elif user.isBust == True:
            print("You lost")
            game.playagain_menu()
            dealer.increaseHighscore(1)
            user.resetHighscore()
            user.newRound()
            dealer.newRound()
            try:
                choice = int(input("Do you want to play again? (1-2): "))
                if choice > 2 or choice <= 0:
                    raise ValueError()
            except ValueError:
                print("Invalid Choice, You can only choose between options 1-2")
                continue
            if choice == 1:
                print("starting a new round")
            elif choice == 2:
                print("Exiting game")
                break
        else:
            print(user.displayResult())
            game.roundEnd(user,dealer)
            
            stop=False
            user.newRound()
            dealer.newRound()
            game.playagain_menu()
            try:
                choice = int(input("Do you want to play again? (1-2): "))
                if choice > 2 or choice <= 0:
                    raise ValueError()
            except ValueError:
                print("Invalid Choice, You can only choose between options 1-2")
                continue
            if choice == 1:
                print("starting a new round")
            elif choice == 2:
                print("Exiting game")
                game.save_file(file_name, highscores)
                break
            
    
print(f"__name__ {__name__}")
if __name__ == "__main__":
    start()