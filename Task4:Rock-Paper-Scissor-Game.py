import random

print("Welcome to RPS game")

print("Enter either rock or paper or scissor(Enter as per your choice) and write them in the below format:")

print("Rock")

print("Paper")

print("Scissor")

count1 = 0

count2 = 0

RPS = ["Rock" , "Paper" , "Scissor"]

print("You can play this game 5 times")

for i in range (1 , 6):

    user = str(input("Enter your choice: "))

    computer = random.choice(RPS)

    print("Computer input = " + computer)

    if user == "Rock" and computer == "Scissor" or user == "Paper" and computer == "Rock" or user == "Scissor" and computer == "Paper":

        count1 += 1

        print("User wins!!")

        print("Score for user = " , count1)

    elif user == "Rock" and computer == "Paper" or user == "Paper" and computer == "Scissor" or user == "Scissor" and computer == "Rock":

        count2 += 1

        print("Computer wins!!")

        print("Score for computer = " , count2)

    elif user == "Rock" and computer == "Rock" or user == "Scissor" and computer == "Scissor" or user == "Paper" and computer == "Paper":

        print("It's a tie!!")

    else:

        print("Invalid input")

        print("")

    if i == 1:

        print("4 lives left")

    elif i == 2:

        print("3 lives left")

    elif i == 3:

        print("2 lives left")

    elif i == 4:

        print("1 lives left")

    else:

        print("Ohhh! no lives left")

    print("")

print("")

print("User score: " , count1)

print("")

print("Computer score: " , count2)

print("")

if count1 > count2:

    print("Overall User wins!!")

elif count1 < count2:

    print("Overall Computer wins!!")

elif count1 == count2:

    print("Oops!! It's a Tie")

else:

    print("No words")

print("")

a = str(input("Please Enter your Feedback for this game: "))

print("")

print("Thank you for the feedback!!")





