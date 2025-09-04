import random

print("Welcome to Guess the King or Write")
print("Choose which method you want to use (1 or 2)")
the_choose = input("1. Using random.randint() \n2. Using random.random() \n").lower()

if the_choose == "1":
    # الطريقة الأولى: استخدام random.randint لاختيار عشوائي بين "King" و "Write"
    king_write = "King" if random.randint(0, 1) == 0 else "Write"
    user_guess = input("Write your guess (King or Write): ").capitalize()
    
    if user_guess != king_write:
        print(f"Sorry, your guess {user_guess} was not correct")
        print(f"The computer chose: {king_write}")
    else:
        print(f"Congratulations! Your guess {user_guess} was correct!")

elif the_choose == "2":
    # الطريقة الثانية: استخدام random.random لاختيار عشوائي بين "King" و "Write"
    king_write = "King" if random.random() >= 0.5 else "Write"
    user_guess = input("Write your guess (King or Write): ").capitalize()
    
    if user_guess != king_write:
        print(f"Sorry, your guess {user_guess} was not correct")
        print(f"The computer chose: {king_write}")
    else:
        print(f"Congratulations! Your guess {user_guess} was correct!")

else:
    print(f"You chose {the_choose} and this is not available. Please choose (1 or 2)")