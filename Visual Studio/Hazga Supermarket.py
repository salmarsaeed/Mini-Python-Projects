print("     --------------------------------------")
print("     *****Welcome to Hazga Supermarket*****")
print("     --------------------------------------")
items=int(input("How many items do you want in your basket today?  "))
total=0
for i in range(items):
    item_price=str(input("Enter the type of item:  "))
    item_price=float(input("Enter the price of item:  "))
    total+=item_price
print("The total price of your items is:  ", total)

#total=0
#for i in range(items):
 #   item_price=float(input("Enter the price of item:  "))
 #  total+=item_price
#print("The total price of your items is:  ", total)

