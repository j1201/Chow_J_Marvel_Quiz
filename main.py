choices = ["Iron Man", "Bucky", "Captain Mavel", "Vision"]

point = 0

questNum = 1

questions = [""]*4

answers = [""]*4

questions[0] = "Who owns Stark Industries?"
answers[0] = "Iron Man"

questions[1] = "Who is the Winter Soldier?"
answers[1] = "Bucky"

questions[2] = "Who said, “What is grief, if not love persevering?”"
answers[2] = "Vision"

questions[3] = "Who rescued Iron Man and Nebula from space?"
answers[3] = "Captain Marvel"

print("Welcome to the Marvel Quiz Game!")

for x in range (4):

    # Print question
    print("\nLv", questNum,"question: ", questions[x])
    choices = input("Iron Man, Bucky, Captain Marvel, Vision (Case-sensitive): ")

    #Print player's choice
    print("Player's answer: " + choices)

    #Compare answer
    if choices == answers[x]:
        print("correct! gain", x+1, "pt!")
        point = point + x+1

    else:
        print("wrong! no pt!")

    print("Player's points: " + str(point) + "\n")

    questNum = questNum + 1 


print("Congrats! You completed the quiz. Your total points are ", point)