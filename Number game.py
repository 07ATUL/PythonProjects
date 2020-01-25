#This is a number guessing game which I made while learning python#
import random
num=random.randint(1,20)
print("Welcome to number guessing game you have 6 choices to win this game, All the best")
print("Enter a number between 1-20")
user_input=int(input())
print("The number you entered is ",user_input)
for i in range (0,5):
    if(user_input==num):
        print(("You Win"))
        break
    else:
        if(user_input<num):
            print("The number who entered is less the number")
        if(user_input>num):
            print("The number you have entered is greater than the number")
    print("You can try again , Enter Your Number")
    user_input=int(input())
#Happy coding