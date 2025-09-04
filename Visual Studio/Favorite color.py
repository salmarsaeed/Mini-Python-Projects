fvc= str(input("Put your favorite color: \n"))
fvc2= str(input("Do you have another favorite color? (Yes or No):")).lower()

if fvc2 == "yes":
    fvc3 = str(input("Enter your second favorite color: \n"))
    print(f"Your favorite colors are {fvc} and {fvc3}")
else:
    print(f"Your favorite color are {fvc}")