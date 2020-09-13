#atul
#A fun story game
import random
import time

def displayIntro():
    print("You are in a land full of dragons.In front of you,you see two caves.In one cave the dragon is friendly and will share his treasure with you. In other dragon is greedy and hungry,will eat you in sight.")
    print()
def chooseCave():
    cave=''
    while cave!='1' and cave!='2':
        print("Which cave will you go into?(1 or 2)")

        cave=input()

    return cave
def checkCave(chosenCave):
    print('you approach the cave')
    time.sleep(2)
    print("A large dragon jumps and opens his jaws out in front of you and....")
    time.sleep(2)

    friendlyCave=random.randint(1,2)

    if chosenCave==str(friendlyCave):
        print('gives you his treasure')
    else:
        print("gobbles you down in one bite")
playAgain='yes'

while playAgain=='yes' or playAgain=='y':
    displayIntro()
    caveNumber=chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again?')

    playAgain=input()
    
