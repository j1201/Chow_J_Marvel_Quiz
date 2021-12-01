from gameComponents import gameVars
from PIL import Image

def total(point):

        if point == 0:
            print("Sorry, I have no idea")
            thinking = Image.open("images/thinking_spriderman.jpg")
            thinking.show()

        elif point <= 1:
            gameVars.characters = gameVars.characters[0]

            print("It's " + gameVars.characters)
            loki = Image.open("images/loki.jpg")
            loki.show()

        elif point <= 2:
            gameVars.characters = gameVars.characters[1]

            print("It's " + gameVars.characters)
            bp = Image.open("images/black_panther.jpg")
            bp.show()

        elif point <= 3:
            gameVars.characters = gameVars.characters[2]

            print("It's " + gameVars.characters)
            ironm = Image.open("images/iron_man.jpg")
            ironm.show()
        
        elif point <= 4:
            gameVars.characters = gameVars.characters[3]

            print("It's " + gameVars.characters)
            bw = Image.open("images/black_widow.jpg")
            bw.show()
