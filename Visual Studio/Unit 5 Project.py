rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcom to the Rock, Paper, Scissors Game!")
chose= input("Press enter to continue or type [help] for instructions: ").lower()

if chose == "help":
    print("       **********Instructions**********")
    print("       1. You will play against the computer.")
    print("       2. Type 'rock', 'paper', or 'scissors' to make your choice.")
    print("       3. Rock smashes Scissors-> Rock wins.")
    print("       4. Scissors cut Paper-> Scissors win.")
    print("       5. Paper covers Rock-> Paper wins.")
    input("Let's start the game press enter!")
    import random

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

print("You chose:")

if user_choice == "rock":
        print(rock)
elif user_choice == "paper":
        print(paper)
else:
        print(scissors)

print("Computer chose:")

if computer_choice == "rock":
        print(rock)
elif computer_choice == "paper":
        print(paper)
else:
        print(scissors)

if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
else:
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")