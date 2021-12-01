from rich import console
from gameComponents import gameQuestions , gameVars
from rich.console import Console

blue_console = Console(style="bold blue on white")
console = Console()

def gameRun():

        quest = gameQuestions.questions["q1"]["question"]
        answerUser = blue_console.input(quest)
        ans = gameQuestions.questions["q1"][answerUser]
        print(ans)

        gameVars.pointTotal += ans
        console.print("==========:thinking_face:========== \n")

        quest = gameQuestions.questions["q2"]["question"]
        answerUser = blue_console.input(quest)
        ans = gameQuestions.questions["q2"][answerUser]
        print(ans)

        gameVars.pointTotal += ans
        console.print("==========:thinking_face:========== \n")

        quest = gameQuestions.questions["q3"]["question"]
        answerUser = blue_console.input(quest)
        ans = gameQuestions.questions["q3"][answerUser]
        print(ans)

        gameVars.pointTotal += ans
        console.print("==========:thinking_face:========== \n")

        quest = gameQuestions.questions["q4"]["question"]
        answerUser = blue_console.input(quest)
        ans = gameQuestions.questions["q4"][answerUser]
        print(ans)

        gameVars.pointTotal += ans
        console.print("==========:thinking_face:========== \n")

        quest = gameQuestions.questions["q5"]["question"]
        answerUser = blue_console.input(quest)
        ans = gameQuestions.questions["q5"][answerUser]
        print(ans)

        gameVars.pointTotal += ans
        console.print("==========:thinking_face:========== \n")