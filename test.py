from time import time
from types import coroutine


print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing != "yes":
    quit()
print("Okay! Let's play:)")
score = 0

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
else:
    print("Incorrect!")
    quit()

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "Random Access Memory":
    print('Correct!')
else:
    print("Incorrect!")
    
