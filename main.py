from gameComponents import gameVars 

print("Welcome to the Marvel Quiz Game!")

for x in range (4):

    # Print question
    print("\nLv", gameVars.questNum,"question: ", gameVars.questions[x])
    gameVars.choices = input("Iron Man, Bucky, Captain Marvel, Vision (Case-sensitive): ")

    #Print player's choice
    print("Player's answer: " + gameVars.choices)

    #Compare answer
    if gameVars.choices == gameVars.answers[x]:
        print("correct! gain", x+1, "pt!")
        gameVars.point = gameVars.point + x+1

    else:
        print("wrong! no pt!")

    print("Player's points: " + str(gameVars.point) + "\n")

    gameVars.questNum = gameVars.questNum + 1 

print("Congrats! You completed the quiz. Your total points are ", gameVars.point)