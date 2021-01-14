#################################################################
#                                                               #
#   project: Code Breaker game                                  #
#   author: Štěpán Michálek                                     #
#   purpose: create a Code Breaker game                         #
#                                                               #
# Features:                                                     #
# - Guess a randomly generated three digit number               #
# - The user input is validated                                 #
# - You get three clues to help you:                            #
# - Nope, Match, Close                                          #
# - The functions are imported from CodeBreakerFunctions.py     #
#                                                               #
#################################################################

import random
from CodeBreakerFunctions import inputThreeDigits
from CodeBreakerFunctions import compareGuessWithSecret

print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Welcome to code breaker. The rules are simple, guess the secret.")
print("The secret is a three digit number. You will get the following clues:")
print(" ")
print("Close means you guessed a correct number, but in the wrong position")
print("Match means you guessed a correct number in the correct position")
print("Nope means no numbers are guessed correctly")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

secret = random.randint(100, 999)
secret = str(secret)

# print(secret)

while(True):
    guess = inputThreeDigits()
    if guess == secret:
        print("Your guess is correct!")
        print("You have won!")
        break
    compareGuessWithSecret(guess, secret)
