# Game info: Player can Choose a initial score(by cost) he want to have ,we will chosse a number a number between 1 and 20
# and player needs to guess that number in 5 chances ,and players will bw given score based
# on how much chnaces they gussed the correct output
import random

attempts = 0
number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")
score = 0
# score=int(input("\nInput the score u want to be at the beginning we will double you score if you gussed it right"))
while attempts < 5:
    guess = input("Take a guess: ")
    guess = int(guess)

    attempts += 1

    if guess < number:
        print("your guess is low , Guess higher next time")

    if guess > number:
        print("Your guess is high,Guess lower next time")

    if guess == number:
        break

if attempts == 0:
    score = 100
elif attempts == 1:
    score == 80
elif attempts == 2:
    score = 60
elif attempts == 3:
    score = 40
elif attempts == 4:
    score = 20

if guess == number:
    attempts = str(attempts)
    print(f"Good job! You guessed my number in {attempts} guesses!")
    print("your final score is :", score)

else:
    number = str(number)
    print(f"Nope. The number I was thinking of was {number}".
          print("your final score is : 0")