a= str(input("Enter the name of your book: \n"))
b= str(input("Enter the author of your book (or press enter to skip): \n"))

if b == "":
    print(f"You have a \n[{a}] \nbook in your library.")
else:
    print(f"You have \n[{a}] and [{b}] \nbooks In your library.")


inf= str(input("Enter the name of a book you wish to have in the future: \n"))
inf2= str(input("Enter the author of the book you wish to have in the future (or press enter to skip): \n"))

if inf2 == "":
    print(f"You wish to have a \n[{inf}] \nbook in your library.")
else:
    print(f"You wish to have \n[{inf}] \n[{inf2}] \nbooks in your library.")


c= str(input("Enter a book from your dream list that you have obtained (or press enter to skip): \n"))

if c == "":
    print(f"Your library is in it \n[{c}] \n[{a}] \nbooks.")
    print(f"Your dream list is in it \n[{inf}] \nbook.")
else:
    print(f"Your library is in it \n[{c}] \n[{a}] \n[{b}] \nbooks.")
    print(f"Your dream list is in it \n[{inf}] \nbook.")

d= str(input("Do you currently have any of your books that you would like to donate? (or press enter to skip): \n"))

if d == "":
    print(f"Your library is in it \n[{b}] \n[{a}] \nbooks.")
    print(f"Your dream list is in it \n[{inf}] \nbook.")
else:
    print(f"Your library is in it \n[{b}] \n[{a}] \nbooks.")
    print(f"Your dream list is in it \n[{inf}] \nbook.")