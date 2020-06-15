###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

import random
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
print("Code is generated. Please guess the number")
dl=random.randint(100,1000)
dl=str(dl)
game=True
while game==True:
    guess = input("What is your guess? ")
    gl=str(guess)
    if gl==dl:
        print("CODE CRACKED!"+"The correct number was: "+dl)
        game=False
    elif(gl[0]==dl[0] or gl[1]==dl[1] or gl[2]==dl[2]):
        print("Match: You've guessed a correct number in the correct position.")
    elif(gl[0]==dl[1] or gl[0]==dl[2] or gl[1]==dl[0] or gl[1]==dl[2] or gl[2]==dl[0] or gl[2]==dl[1]):
        print("Close: You've guessed a correct number but in the wrong position")

print("Thanks for playing the game.")
