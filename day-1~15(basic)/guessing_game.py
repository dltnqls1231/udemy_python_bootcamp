import random
EASY_TURN = 10
HARD_TURN = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
answer = random.randrange(1, 101)

def is_right(guess):
    global answer
    if guess > answer:
        print("Too high")
        print("Guess again")
    elif guess < answer:
        print("Too low")
        print("Guess again")
    else:
        return True


if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while attempts:
    print(f"You have {attempts} attemps remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if is_right(guess):
        break
    attempts -= 1

if attempts == 0:
    print("You've run out of guesses, you lose")
else:
    print(f"You got it! The answer was {answer}")
