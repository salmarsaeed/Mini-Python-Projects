import random
my_random= random.randint(1111,2222)
print("Computer generated PIN: {my_random}")

num= len(input("Enter 4_digit PIN code: \n"))
if num<4:
    print("Pleas enter 4_digit")
elif num>4:
    print("Pleas enter 4_digit")
elif num==my_random:
    print("Good, you have entered the correct number.")
else:
    print(f"Failure! PIN code did not mutch \nThe computer generated this PIN: {my_random}")