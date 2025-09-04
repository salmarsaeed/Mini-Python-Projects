import random

king_write = random.random()
print("Welcome to Guess the King or Write")
print("The computer picked a number between 0 and 1.")

guess = input("Write your guess (king or write): ").lower()

if (guess == "king" and king_write < 0.5) or (guess == "write" and king_write >= 0.5):
    print("🎉 Congratulations! You guessed correctly.")
else:
    print(f"❌ Wrong guess. The number was {king_write}")
