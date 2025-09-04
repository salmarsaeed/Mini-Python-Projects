age= int(input("How old are you? \n"))
license= input("Do you have a license? (yes/no) \n")
if age >= 18 and license.lower() == "yes":
    print("Wow, you can drive.")
else:
    print("Sorry, you can not drive.")