#شل مرعب فالبدايا
#تلت بيبان يختار منهم الباب الى هو عايزو
#الوان البيبان (احمر)(ازرق)(اسود)
#الاسود هيطلعلو عفاريت وجني وهيكون اختيار غلط
#احمر اختيار خاطء مش على مزاجي
#الازرق اختيار صحيح
#وبعد اختيار الازرق سيزهر 3هداياويختار وحدة منهم
#الوان الهدايا (بينك)(بابي بلو)(رمادي)
#البينك هيموووت
#البابي بلو اختيار صحيح
#الرمادي اختيار غير موفق
#البابي بلو سيظهر لهو نقوووود وذهب
#وبعدين جايم اوفر
#use cass


print("Welcome to Pirate Island")

print("""
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
""")
challenge= str(input("Choose one of the three doors \nred door🚪🔴 \nblue door🚪🔵 \nblack door🚪⚫ \n")).lower()
if challenge=="red door":
    print("This choice is not successful \n[The game is over]")
elif challenge=="black door":
    print("It's the goblins who have taken over you \n[The game is over]")
elif challenge=="blue door":
    box= input("Okay now choose one of the three boxes \npink box🩷🎁 \nbaby blue box🩵🎁 \ngray box🩶🎁 \n").lower()
    if box=="pink box":
        print("Nothing happened... the box was empty \n[The game is over]")
    elif box=="gray box":
        print("It's the goblins who have taken over you \n[The game is over]")
    elif box=="baby blue box":
        print("You found a treasure!🏴‍☠️💰 treasures, gold and money . Congratulations🎊!")
else:
    print(f"Please obey the rules of Pirate Island, because you wrote this {challenge} and that does not exist")