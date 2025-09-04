basket =[["Apples", "Bananas"],["Milk", "Water"]]

print(basket)

input("Press Enter to change the content...... \n")
print("Here is the updated basket: \n")

basket[0].insert(0, "Orange")
basket[0].insert(3,"Kiwis")

basket[1].insert(0, "Coffee")
basket[1].insert(2, "Tea")

basket.append(["1","2","3"])
basket[1].remove("Water")
print(basket)