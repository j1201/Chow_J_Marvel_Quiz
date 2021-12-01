from gameComponents.gameQuestions import questions
from gameComponents import gameRun, gameVars , compare

print("Welcome to the Marvel Quiz Game!")
print("Think about a Marvel Character & I will try to guess who the character is\n")

while gameVars.player is False:

    gameRun.gameRun()

    print("Total Point: " + str(gameVars.pointTotal) + "\n")

    compare.total(gameVars.pointTotal)

    playAgain = input("Do you want to play again? yes/no :")

    if playAgain == "no":
        print("See ya!")
        exit ()
    elif playAgain == "yes":
        print("=================\n")
        gameVars.pointTotal = 0
        gameVars.player = False

    gameVars.player = False