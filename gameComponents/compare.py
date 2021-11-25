from gameComponents import gameVars

def total(point):

        if point == 0:
            print("Sorry, I have no idea")

        elif point <= 1:
            gameVars.characters = gameVars.characters[0]

            print("It's " + gameVars.characters)

        elif point <= 2:
            gameVars.characters = gameVars.characters[1]

            print("It's " + gameVars.characters)

        elif point <= 3:
            gameVars.characters = gameVars.characters[2]

            print("It's " + gameVars.characters)

