import random
ranNumber = random.randint(1, 100)
print("Can you guess the number I am thinking? :")
#testing number, delete later
print(ranNumber)

def guessNumber(ranNumber):
    guesses = 10
    while guesses > 0:
        guessNum = int(input())
        if ranNumber > guessNum:
            print("Too low, try again")
            if (ranNumber - guessNum) > 0 and (ranNumber - guessNum) <= 5:
                print("On FIRE")
            elif (ranNumber - guessNum) > 5 and (ranNumber - guessNum) <= 10:
                print("You're hot")
            elif (ranNumber - guessNum) > 10 and (ranNumber - guessNum) <= 20:
                print("Getting warmer")
            else:
                print("ice cold")
        elif ranNumber < guessNum:
            print("Too high, try again")
            if (guessNum - ranNumber) > 0 and (guessNum - ranNumber) <= 5:
                print("On FIRE")
            elif (guessNum - ranNumber) > 5 and (guessNum - ranNumber) <= 10:
                print("You're hot")
            elif (guessNum - ranNumber) > 10 and (guessNum - ranNumber) <= 20:
                print("Getting warmer")
            else:
                print("ice cold")
        else:
            print("You got it! Your score is " + str(guesses))
            return guessNum
        guesses -= 1
        print("Your score is " + str(guesses))
    print("Out of guesses! Too bad. Number was: " + str(ranNumber))
    
guessNumber(ranNumber)
