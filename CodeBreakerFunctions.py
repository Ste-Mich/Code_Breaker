# functions for CodeBreaker.py

def inputThreeDigits():
    userInput = ""
    print("Type in your guess:")
    while(True):
        userInput = input("Input: ")
        if(userInput.isnumeric() == False):
            print("Please input just a number")
            continue
        userInput = int(userInput)
        if(userInput > 999):
            print("The number is too big")
            continue
        if(userInput < 100):
            print("The number is too small")
            continue
        if(999 >= userInput >= 100):
            break
    return str(userInput)


def compareGuessWithSecret(guess, secret):
    if guessIsNope(guess, secret) == True:
        print("Nope")
        return
    if guessIsMatch(guess, secret) == True:
        print("Match")
        return
    if guessIsClose(guess, secret) == True:
        print("Close")
        return


def guessIsNope(guess, secret):
    return not (guess[0] in secret or guess[1] in secret or guess[2] in secret)


def guessIsMatch(guess, secret):
    return (guess[0] == secret[0] or guess[1] == secret[1] or guess[2] == secret[2])


def guessIsClose(guess, secret):
    return (guess[0] in secret[1:3] or guess[1] in [secret[0], secret[2]] or guess[2] in secret[0:2])
