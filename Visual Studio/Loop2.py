a=["Ahmed", "Anas", "Omer"]
for person in a:
    print(a)
    print("______")
    if person == "Ahmed":
        print("Ahmed")
        b= input("Is this person attending? (yes/no): ")
        if b.lower() == "yes":
            print(f"{person} is attending the event.")
        else:
            print(f"{person} is not attending the event.")
            print("______")
    if person == "Anas":
        print("Anas")
        c = input("Is this person attending? (yes/no): ")
        if c.lower() == "yes":
            print(f"{person} is attending the event.")
        else:
            print(f"{person} is not attending the event.")
        print("______")
    if person == "Omer":
        print("Omer")
        d = input("Is this person attending? (yes/no): ")
        if d.lower() == "yes":
            print(f"{person} is attending the event.")
        else:
            print(f"{person} is not attending the event.")