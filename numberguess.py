
import random

computer=random.randint(0,5)
userInput=0
score=0

print("Welcome to the Number Guessing Game!!")

while (userInput !="q"):

    userInput=input("Enter a number: or q to quit the game: ")
    cleanInput=0
    if userInput=="q":
        break
    else:
        try:
            cleanInput=int(userInput)
        except ValueError as e:
            print("Use numbers only")

    if cleanInput==computer:
        score+=5
        print("Hurray!!You win!")
        print(f"Your score is: {score}")
    else:
        if score>0:
            score-=5
        print(f"The computer chose: {computer} Try again")
        print(f"Your score is: {score}")
