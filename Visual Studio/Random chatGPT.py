import random

# Generate a 4-digit random PIN
my_random = random.randint(1000, 9999)
print(f"(For testing) Computer generated PIN: {my_random}")

# Ask user
num_input = input("Enter 4-digit PIN code:\n")

# Validation
if len(num_input) != 4 or not num_input.isdigit():
    print("Please enter a valid 4-digit number.")
else:
    num = int(num_input)
    if num == my_random:
        print("Good, you have entered the correct number.")
    else:
        print(f"Failure! PIN code did not match.\nThe computer generated this PIN: {my_random}")
