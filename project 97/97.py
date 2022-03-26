import numbers
import random
print("NUMBER GUESSING GAME")
number = random.randint(1,9)
chances=0
print("Guess a number(between 1 and9):")
while chances<5:
    guess=int(input("Enter your guess:-"))
    if guess== number:
        print("**congratulations you won**")
        break

    elif guess<number:
        print("your guess is too low; Guess a number higher number")
    else:
        print("your guess was too high: Guess a lower number")
        chances+=1


if not chances< 5:
    print("You Lose!!! The number is",number)
    