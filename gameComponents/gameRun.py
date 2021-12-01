from gameComponents import gameQuestions , gameVars

def gameRun():

        quest = gameQuestions.questions["q1"]["question"]
        answerUser = input(quest)
        ans = gameQuestions.questions["q1"][answerUser]
        print(ans)

        gameVars.pointTotal += ans
        print("=================\n")

        quest = gameQuestions.questions["q2"]["question"]
        answerUser = input(quest)
        ans = gameQuestions.questions["q2"][answerUser]
        print(ans)

        gameVars.pointTotal += ans
        print("=================\n")

        quest = gameQuestions.questions["q3"]["question"]
        answerUser = input(quest)
        ans = gameQuestions.questions["q3"][answerUser]
        print(ans)

        gameVars.pointTotal += ans
        print("=================\n")

        quest = gameQuestions.questions["q4"]["question"]
        answerUser = input(quest)
        ans = gameQuestions.questions["q4"][answerUser]
        print(ans)

        gameVars.pointTotal += ans
        print("=================\n")

        quest = gameQuestions.questions["q5"]["question"]
        answerUser = input(quest)
        ans = gameQuestions.questions["q5"][answerUser]
        print(ans)

        gameVars.pointTotal += ans
        print("=================\n")