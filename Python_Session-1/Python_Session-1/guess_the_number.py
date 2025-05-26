# GAME : Guess the number

# Computer generated number should be guessed by us.--> done
# if output of our guess matches, a message saying: you have guessed, else message generated, with lower or higher value --> done
# challenge -> magesh, if we enter a number and press enter, computer guessed number might get change.
# trial -> 3 times --> done
# get user input --> done
# condition to validate --> done
# restricting user input to a fixed range --> done
# declare a variable to store value --> done

import random
random_number = random.randrange(1,5)
guessed_number = int(input("Please enter number between 1 and 10: - "))
trial = 1
while trial <5:
    if random_number == guessed_number:
        print("Hooray!! You have guessed it right")
        break
    elif random_number < guessed_number:
        print("OOps!! You have guessed a higher number")
    else:
        print("OOps!! You have guessed a lower number")
    trial +=1
    guessed_number = int(input("Please enter number between 1 and 100: - "))
print(f"Trial Over, better next time,The generated number was {random_number}")