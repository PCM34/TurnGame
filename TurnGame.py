import random

print("THE RULES\n")
print("This is a move based game, and the objective is to kill your opponent.")
print("Your health will start at 100.")
print("To play, you will have a variety of moves at your disposal.")
print("attack 1 is a moderate attack. (damage is between 18 and 25)")
print("attack 2 is an attack with a greater range of possibility. (damage is between 10 and 35)")
print("heal is a move where you heal yourself. (can heal between 18 and 25 HP")
print("")

person1 = input("Enter player one's name")
person2 = input("Enter player two's name")

whoGoesFirst = ""
x = ""
SpellingCheck = 0
attackVal = 0

if random.randint(0, 1) == 0:
    whoGoesFirst = "p1"
else:
    whoGoesFirst = "p2"

person1HP = 100
person2HP = 100

while person1HP > 0 and person2HP > 0:
    if whoGoesFirst == "p1":
        print("It is " + person1 + "'s turn")

        print("")
        print(person1 + " HP=" + str(person1HP))
        print(person2 + " HP=" + str(person2HP))

        while SpellingCheck == 0:
            print("")
            x = input(person1 + ", would you like to use attack 1, attack 2, or heal?")
            if x == "attack 1" or x == "attack 2" or x == "heal":
                SpellingCheck = 1
            else:
                print("you must have had a spelling error, try again.")
        SpellingCheck = 0

        print("")
        if x == "attack 1":
            attackVal = random.randint(18, 25)
            print("your attack is worth " + str(attackVal) + " damage")
            person2HP = person2HP - attackVal
            print("")
            print(person2 + "'s HP is now " + str(person2HP))

        elif x == "attack 2":
            attackVal = random.randint(10, 35)
            print("your attack is worth " + str(attackVal) + " damage")
            person2HP = person2HP - attackVal
            print("")
            print(person2 + "'s HP is now " + str(person2HP))

        else:
            attackVal = random.randint(18, 25)
            print("your heal is worth " + str(attackVal) + " HP")
            person1HP = person1HP + attackVal
            print("")
            print(person1 + "'s health is now " + str(person1HP))

        if person2HP > 0:
            print("It is " + person2 + "'s turn")

            print("")
            print(person1 + " HP=" + str(person1HP))
            print(person2 + " HP=" + str(person2HP))

            while SpellingCheck == 0:
                print("")
                x = input(person2 + ", would you like to use attack 1, attack 2, or heal?")
                if x == "attack 1" or x == "attack 2" or x == "heal":
                    SpellingCheck = 1
                else:
                    print("you must have had a spelling error, try again.")
            SpellingCheck = 0

            print("")
            if x == "attack 1":
                attackVal = random.randint(18, 25)
                print("your attack is worth " + str(attackVal) + " damage")
                person1HP = person1HP - attackVal
                print("")
                print(person1 + "'s HP is now " + str(person1HP))

            elif x == "attack 2":
                attackVal = random.randint(10, 35)
                print("your attack is worth " + str(attackVal) + " damage")
                person1HP = person1HP - attackVal
                print("")
                print(person1 + "'s HP is now " + str(person1HP))

            else:
                attackVal = random.randint(18, 25)
                print("your heal is worth " + str(attackVal) + " HP")
                person2HP = person2HP + attackVal
                print("")
                print(person2 + "'s health is now " + str(person2HP))
    else:
        print("It is " + person2 + "'s turn")

        print("")
        print(person2 + " HP=" + str(person2HP))
        print(person1 + " HP=" + str(person1HP))

        while SpellingCheck == 0:
            print("")
            x = input(person2 + ", would you like to use attack 1, attack 2, or heal?")
            if x == "attack 1" or x == "attack 2" or x == "heal":
                SpellingCheck = 1
            else:
                print("you must have had a spelling error, try again.")
        SpellingCheck = 0

        print("")
        if x == "attack 1":
            attackVal = random.randint(18, 25)
            print("your attack is worth " + str(attackVal) + " damage")
            person1HP = person1HP - attackVal
            print("")
            print(person1 + "'s HP is now " + str(person1HP))

        elif x == "attack 2":
            attackVal = random.randint(10, 35)
            print("your attack is worth " + str(attackVal) + " damage")
            person1HP = person1HP - attackVal
            print("")
            print(person1 + "'s HP is now " + str(person1HP))

        else:
            attackVal = random.randint(18, 25)
            print("your heal is worth " + str(attackVal) + " HP")
            person2HP = person2HP + attackVal
            print("")
            print(person2 + "'s health is now " + str(person2HP))

        if person1HP > 0:
            print("It is " + person1 + "'s turn")

            print("")
            print(person2 + " HP=" + str(person2HP))
            print(person1 + " HP=" + str(person1HP))

            while SpellingCheck == 0:
                print("")
                x = input(person1 + ", would you like to use attack 1, attack 2, or heal?")
                if x == "attack 1" or x == "attack 2" or x == "heal":
                    SpellingCheck = 1
                else:
                    print("you must have had a spelling error, try again.")
            SpellingCheck = 0

            print("")
            if x == "attack 1":
                attackVal = random.randint(18, 25)
                print("your attack is worth " + str(attackVal) + " damage")
                person2HP = person2HP - attackVal
                print("")
                print(person2 + "'s HP is now " + str(person2HP))

            elif x == "attack 2":
                attackVal = random.randint(10, 35)
                print("your attack is worth " + str(attackVal) + " damage")
                person2HP = person2HP - attackVal
                print("")
                print(person2 + "'s HP is now " + str(person2HP))

            else:
                attackVal = random.randint(18, 25)
                print("your heal is worth " + str(attackVal) + " HP")
                person1HP = person1HP + attackVal
                print("")
                print(person1 + "'s health is now " + str(person1HP))

print("")
if person1HP <= 0:
    print(person2 + " is the WINNER!!!!!!!!")

else:
    print(person1 + " is the WINNER!!!!!!!!")
