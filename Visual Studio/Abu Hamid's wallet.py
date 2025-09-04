print ("Welcome to Abu Hamid's wallet🤑💼")
benefit= input("Please enter the list of those attending the meal today and I will choose who will benefit from the wallet: \n")
benefit_list = benefit.split(", ")
if len(benefit_list) == 0:
    print("No one is attending the meal today🥲.")
else:
    print("The following people are attending the meal today:")
    for person in benefit_list:
        print(f"- {person}")
    # Randomly select a beneficiary from the list
    import random
    beneficiary = random.choice(benefit_list)
    print(f"Make {beneficiary} take out his wallet, it will be useful today😁: {beneficiary}")