import random

king_write= str (random.random())
king_write >= "king","write"
print(king_write)

print("Welcome to Guess the King or Write")
print("Choose which method you want to use (1 or 2)")

the_choose= input("1.Using random.randint() \n2.Using random.random() \n").lower()
if the_choose=="1":
    rand1= str(input("Write your guess (King or Write): ")).lower()
    if rand1 != king_write:
        print(f"Sorry, your guess {rand1} was not correct")
        print(f"The computer’s creation this{king_write}")
elif the_choose=="2":
    rand2= str(input("Write your guess (King or Write): "))
    if rand2 != king_write:
        print(f"Sorry, your guess {rand2} was not correct")
        print(f"The computer’s creation this{king_write}")
else:
    print(f"You chose {the_choose} and this is not available. Please choose (1 or 2)")
