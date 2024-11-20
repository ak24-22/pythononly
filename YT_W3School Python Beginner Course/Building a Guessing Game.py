#19) BUILDING A GUESSING GAME
print("19. BUILDING A GUESSING GAME\n")

secretword = "ALIS"
guess = ""
guesscount = 0
guesslimit = 5
outofguesses = False

while guess != secretword and not (outofguesses):
    if guesscount < guesslimit:
        guess = input ("Guess the Word: ")
        guesscount += 1
    else:
        outofguesses = True

if outofguesses:
     print("Out of guess, You Lose!")
else:
    print("You Win!")

