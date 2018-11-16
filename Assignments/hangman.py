from random import randint
import sys
import argparse


# An example command:
# ./hangman.py voile blame jelab alive movie olive bloke aboil -p 4

class Player:
    def __init__(self, name, playerId):
        self.name = name
        self.playerId = playerId
        self.guesses = 3


guessed = set()

# chosenWord = ""
players = {}

def main():
    numOfPlayers = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('foobar', nargs='*', default='[\'foo\', \'bar\']', help='This gathers the words inputted ')
    parser.add_argument('-p', type=int, default=3, help='This is a flag that takes an int, and will set the number of players')
    args = parser.parse_args()
    
    words = args.foobar
    numOfPlayers = args.p
    guessWord = []

    for x in range(int(numOfPlayers)):
        aPlayerName = input('Please enter in a player\'s name: ')
        players[aPlayerName] = 3
        
    print('----------Here are the players----------\n')
    print(players)

    chosenWord = words.pop()
    
    
    for l in chosenWord:
        guessWord += "*"

    print('----------Time to start guessing!----------\n')

    # while ''.join(guessWord) != chosenWord:
    while players:    
        for ind in players:
            if players.get(ind) != 0:
                print("Player ", ind, "guesses left: ", players.get(ind))
                print("Found so far: ", guessWord)
                print("Tried so far: ", *guessed, sep=" ")
                aGuess = input("what is your guess?: ").lower()
                if not aGuess in guessed:
                    if aGuess in chosenWord:
                        print("Guess correct!")
                        # reveal the hidden letter in guessword
                        idx = chosenWord.index(aGuess)
                        guessWord[idx] = aGuess
                    elif not aGuess in chosenWord:
                        print("Guess incorrect!")
                        guessTry = int(players.get(ind))-1
                        print("guessTRY =====", guessTry)
                        players[ind] = guessTry
                    
                    
                    
                    # guessed.add(aGuess)
                guessed.add(aGuess)
                if ''.join(guessWord) == chosenWord:
                    print("Player: ", ind, " wins!")
                    sys.exit()
            else:
                print("Player: ", ind, " has lost and cannot guess anymore")
 
            


    
main()