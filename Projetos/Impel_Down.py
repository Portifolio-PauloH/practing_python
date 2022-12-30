# Project of the day (day 03) - ESCAPE FROM IMPEL DOWN

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Escape from Impel Down.")
print("Your mission is to find the treasure and escape.")

play = input("Let's play the game? Y or N. ")
gold = 0
hp = 25

if play == "Y":
    print("Let's gooooo, we are pirates and we need find the treasure which is found in impel down, now we across de door in front of us.\n")
    route1 = input(
        "We found two routes left and right, which should we choise? L or R.\n ")
    if route1 == "R":
        gold += 10
        route2 = input(
            "Nice, we found 10 Golds, now we have 3 routes L, C or R.\n ")
        if route2 == "L":
            hp -= 7
            print("Oh shit we found a Minotaur!!\n")
            print("Uffa, now let's continue!\n")
        elif route2 == "C":
            gold += 5
            print("Uhuuuu, more gold!!!!!\n")
            print("Let's continue!\n")
        elif route2 == "R":
            print("Ok, we found anything here, let's continue!\n")

        print("What is that delicious smell of roasted chicken...hmmmmmm!!!!")
        print("Wait, are you listening to this song? \n")
        route4 = input(
            "Which you choise, the delicious smell (L) or the beautiful music (R)?\n ")
        if route4 == "L":
            hp -= 15
            print("Oh, the Crazy Cook is here!!\n")
            print("Let's battle!!\n ")
            if hp >= 1:
                gold += 15
                print("Yessss we did it!\n")
                print("And we found more Gold\n")
                print("Whats was that, the exit? \n Ohh that's it!!\n")
        else:
            hp -= 20
            print("Oh, the Mad Bard is here!!\n")
            print("Let's battle!!\n ")
            if hp >= 1:
                gold += 50
                print("Yessss we did it!\n")
                print("And we found more Gold\n")
                print("Whats was that, the exit? /n Ohh that's it!!\n")

        if (gold > 20) and (hp >= 1):
            print(f"We obtain {gold} Golds and health {hp}")
            print("Yess, we did it, we hove to much Gold to escape from here")
        else:
            print(f"We obtain {gold} and health {hp}")
            print("We lost guys T-T ")

    else:
        hp -= 5
        print("Oh shit we found a Minotaur!!\n")
        print("Shit I'm bleeding, but we managed\n")
        route3 = input("Found 2 routes L or R.\n ")
        if route3 == "L":
            hp += 3
            print("Nicee, we found a potion (restore 3 HP)\n")
            print("Now let's continue.\n")
            print("What is that delicious smell of roasted chicken...hmmmmmm!!!!")
            print("Wait, are you listening to this song? \n")
            route4 = input(
                "Which you choise, the delicious smell (L) or the beautiful music (R)? \n")
            if route4 == "L":
                hp -= 15
                print("Oh, the Crazy Cook is here!!\n")
                print("Let's battle!!\n ")
                if hp >= 1:
                    gold += 15
                    print("Yessss we did it!\n")
                    print("And we found more Gold\n")
                    print("Whats was that, the exit? /n Ohh that's it!!\n")
            else:
                hp -= 20
                print("Oh, the Mad Bard is here!!\n")
                print("Let's battle!!\n ")
                if hp >= 1:
                    gold += 50
                    print("Yessss we did it!\n")
                    print("And we found more Gold\n")
                    print("Whats was that, the exit? \n Ohh that's it!!\n")
        else:
            print("What is that delicious smell of roasted chicken...hmmmmmm!!!!")
            print("Wait, are you listening to this song? \n")
            route4 = input(
                "Which you choise, the delicious smell (L) or the beautiful music (R)?\n ")
            if route4 == "L":
                hp -= 15
                print("Oh, the Crazy Cook is here!!\n")
                print("Let's battle!!\n ")
                if hp >= 1:
                    gold += 15
                    print("Yessss we did it!\n")
                    print("And we found more Gold\n")
                    print("Whats was that, the exit? /n Ohh that's it!!\n")
            else:
                hp -= 20
                print("Oh, the Mad Bard is here!!\n")
                print("Let's battle!! \n")
                if hp >= 1:
                    gold += 50
                    print("Yessss we did it!\n")
                    print("And we found more Gold\n")
                    print("Whats was that, the exit? \n Ohh that's it!!\n")

        if (gold > 20) and (hp >= 1):
            print(f"We obtain {gold} Golds and health {hp}")
            print("Yess, we did it, we hove to much Gold to escape from here")
        else:
            print(f"We obtain {gold} and health {hp}")
            print("We lost guys T-T ")
else:
    print("Ok, seeya")
