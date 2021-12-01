from gameComponents.gameQuestions import questions
from gameComponents import gameRun, gameVars , compare
from rich.console import Console
from rich.style import Style

console = Console()

base_style = Style.parse("bold white on red")
red_console = Console(style="bold red")

console.print(":superhero: Welcome to the Marvel Quiz Game! :superhero:" , style = base_style)
print("═════════════════════════════════════════ \n═════┌─┐┌─┐┌───┐┌───┐┌┐══┌┐┌───┐┌┐═══════ \n═════││└┘│││┌─┐││┌─┐││└┐┌┘││┌──┘││═══════ \n═════│┌┐┌┐│││═│││└─┘│└┐││┌┘│└──┐││═══════ \n═════│││││││└─┘││┌┐┌┘═│└┘│═│┌──┘││═┌┐════ \n═════│││││││┌─┐││││└┐═└┐┌┘═│└──┐│└─┘│════ \n═════└┘└┘└┘└┘═└┘└┘└─┘══└┘══└───┘└───┘════ \n═════════════════════════════════════════")
console.print("Think about a Marvel Character & I will try to guess who the character is! \n" , style="bold blink")

while gameVars.player is False:

    gameRun.gameRun()

    print("Total Point: " + str(gameVars.pointTotal) + "\n")

    compare.total(gameVars.pointTotal)

    playAgain = red_console.input("Do you want to play again? y/n :")

    if playAgain == "n":
        console.print("See ya!:waving_hand: \n")
        exit ()
    elif playAgain == "y":
        console.print("Another Round \n" , style = base_style)
        gameVars.pointTotal = 0
        gameVars.player = False

    gameVars.player = False