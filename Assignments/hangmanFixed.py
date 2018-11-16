from random import randint
import sys


class Player:
    def __init__(self, name, playerId):
        self.name = name
        self.playerId = playerId
        self.guesses = 3

words = ["store", "great"]
guessed = []

# chosenWord = ""


def main():
    
    guessWord = []

    numOfPlayers = input('How many players are playing (max of 3):\n')
    while int(numOfPlayers) < 1 or int(numOfPlayers) > 3:
        if int(numOfPlayers) > 3:
            numOfPlayers = input('Too many players -- How many players are playing (MAX OF 3):\n')
        if int(numOfPlayers) < 1:
            numOfPlayers = input('There has to be at least one player to continue, Please enter the number of players:\n')
    
    for x in range(int(numOfPlayers)):
        aPlayerName = input('Please enter in a player\'s name: ')
        if x == 0:
            player0 = Player(aPlayerName, x)
        if x == 1:
            player1 = Player(aPlayerName, x)
        if x == 2:
            player2 = Player(aPlayerName, x)

    print('----------Here are the players----------\n')
    print('Player 0: ', player0.name, '---- PlayerId: ', player0.playerId)
    if int(numOfPlayers) > 1:
        print('Player 1: ', player1.name, '---- PlayerId: ', player1.playerId)
    if int(numOfPlayers) > 2:
        print('Player 2: ', player2.name, '---- PlayerId: ', player2.playerId)

    chosenWord = words[randint(0, (len(words)-1) )]
    
    for l in chosenWord:
        guessWord += "*"

    print('----------Time to start guessing!----------\n')

    while ''.join(guessWord) != chosenWord:
        
        if player0.guesses != 0:
            print("Player ", player0.name, "guesses left: ", player0.guesses)
            print("Found so far: ", guessWord)
            print("Tried so far: ", *guessed, sep=" ")
            aGuess = input("what is your guess?: ").lower()
            
            if aGuess in guessed:
                aGuess = input("You entered an already guessed letter what is your guess?: ").lower()

            if not aGuess in guessed:
                if aGuess in chosenWord:
                    print("Guess correct!")
                    # reveal the hidden letter in guessword
                    idx = chosenWord.index(aGuess)
                    guessWord[idx] = aGuess
                    # guessWord = guessWord.replace(guessWord[idx], aGuess, 1)
                    guessed.append(aGuess)
                elif not aGuess in chosenWord:
                        print("Guess incorrect!")
                        player0.guesses = (player0.guesses - 1)
            if ''.join(guessWord) == chosenWord:
                print("Player: ", player0.name, " wins!")
                sys.exit()
        else:
            print("Player: ", player0.name, " has lost and cannot guess anymore")
            break




        if int(numOfPlayers) > 1:
            if player1.guesses != 0:
                print("Player ", player1.name, "guesses left: ", player1.guesses)
                print("Found so far: ", guessWord)
                print("Tried so far: ", *guessed, sep=" ")
                aGuess = input("what is your guess?: ").lower()

                if aGuess in guessed:
                    aGuess = input("You entered an already guessed letter what is your guess?: ").lower()

                if not aGuess in guessed:
                    if aGuess in chosenWord:
                        print("Guess correct!")
                        # reveal the hidden letter in guessword
                        idx = chosenWord.index(aGuess)
                        guessWord[idx] = aGuess
                        # guessWord = guessWord.replace(guessWord[idx], aGuess, 1)
                        guessed.append(aGuess)
                    elif not aGuess in chosenWord:
                            print("Guess incorrect!")
                            player1.guesses = (player1.guesses - 1)
                    
                if ''.join(guessWord) == chosenWord:
                    print("Player: ", player0.name, " wins!")
                    sys.exit()
            else:
                print("Player: ", player1.name, " has lost and cannot guess anymore")
                
                
            


        if int(numOfPlayers) > 2:
            if player2.guesses != 0:
                print("Player ", player2.name, "guesses left: ", player2.guesses)
                print("Found so far: ", guessWord)
                print("Tried so far: ", *guessed, sep=" ")
                aGuess = input("what is your guess?: ").lower()

                if aGuess in guessed:
                    aGuess = input("You entered an already guessed letter what is your guess?: ").lower()

                if not aGuess in guessed:
                    if aGuess in chosenWord:
                        print("Guess correct!")
                        # reveal the hidden letter in guessword
                        idx = chosenWord.index(aGuess)
                        guessWord[idx] = aGuess
                        # guessWord = guessWord.replace(guessWord[idx], aGuess, 1)
                        guessed.append(aGuess)
                    elif not aGuess in chosenWord:
                            print("Guess incorrect!")
                            player2.guesses = (player2.guesses - 1)
                if ''.join(guessWord) == chosenWord:
                    print("Player: ", player2.name, " wins!")
                    sys.exit()
            else:
                print("Player: ", player2.name, " has lost and cannot guess anymore")

    if player0.guesses == 0:
        if numOfPlayers == 1:
            sys.exit()
    if numOfPlayers == 2:
        if player0.guesses == 0 and player1.guesses == 0:
            sys.exit()
    if numOfPlayers == 3:
        if player0.guesses == 0 and player1.guesses == 0 and player2.guesses == 0:
            sys.exit()
                

    sys.exit()


    
main()