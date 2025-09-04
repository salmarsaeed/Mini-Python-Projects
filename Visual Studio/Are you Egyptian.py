is_eg= input("Are you Egyptian? Choose yes or no. \n").lower()
if is_eg == "yes":
    print("Good, that’s the first step.")
    is_18= input("Are you above 18? choose yes or no. \n").lower()
    if is_18=="yes":
        print("You can have and ID.")
    else:
        print("Sorry, you have to be 18 or oider \nplease, try again when you are 18.")
else:
    print("Sorry, an Egyptian ID give only to Egyptian.")