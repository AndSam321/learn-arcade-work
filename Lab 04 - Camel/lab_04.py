<<<<<<< HEAD
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_miles_traveled = -20
canteens_left = 3
import random
def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    done = False
    while not done:
        print("A. Drink from your canteen. ")
        print("B. Ahead moderate speed. ")
        print("C. Ahead full speed. ")
        print("D. Stop for the night. ")
        print("E. Status check. ")
        print("Q. Quit. ")


        user_input = input("What is your choice? ")
        if user_input.lower() == "q":
            print("Thanks for playing! ")
            done = True
        elif user_input.lower() == "e":
            print("You've traveled", miles_traveled, "miles.")
            print("Canteens left ", canteens_left)
            print("The natives are", natives_miles_traveled, "miles behind you")
        elif user_input.lower() == "d":
            print("Your camel is happy")
            natives_miles_traveled + random.randrange(7, 14)
            print("The Natives are", natives_miles_traveled)

















main()
=======

import random
def main():
    print("Welcome to Spongebob")
    print("You have stolen the burger-mobile and have to make your way to Jellyfish Fields!")
    print("Mr. Krabs want his car back and is chasing you down! Survive your")
    print("oceanic journey, reach 200 miles, and out run the krab.\n")

    # Starting Variables
    miles_traveled = 0
    hungrieness = 0
    burger_tiredness = 0
    mr_krabs_miles_traveled = -20
    krabby_patties = 3

    # User Options
    done = False
    while not done:
        print("A. Eat a Krabby Patty. ")
        print("B. Ahead Moderate Speed. ")
        print("C. Ahead Full Speed. ")
        print("D. Stop for the night. ")
        print("E. Status Check. ")
        print("Q. Quit ")

        # User choice and Quit Value
        user_choice = input("What is your choice? ")
        if user_choice.upper() == "Q":
            print("Thanks for playing!")
            done = True

        # Status Check E
        elif user_choice.upper() == "E":
            print("\nYou've traveled", miles_traveled, "miles.")
            print("Krabby Patties left ", krabby_patties)
            print("Mr. Krabs is " + str(miles_traveled - mr_krabs_miles_traveled) + " miles behind you.")

        # Stop for the night D
        elif user_choice.upper() == "D":
            print("\nYou have stopped for the night to rest.")
            print("Your burger mobile is rested and happy!")
            burger_tiredness = 0
            mr_krabs_miles_traveled = mr_krabs_miles_traveled + random.randrange(7, 14)
            print("Mr. Krabs is " + str(miles_traveled - mr_krabs_miles_traveled) + "miles behind you.\n")

        # Ahead full speed C
        elif user_choice.upper() == "C":
            print("\nYou are moving fast!")
            miles_traveled = miles_traveled + random.randrange(10, 20)
            hungrieness = hungrieness + 1
            burger_tiredness = burger_tiredness + random.randrange(1, 3)
            mr_krabs_miles_traveled= mr_krabs_miles_traveled + random.randrange(7, 14)

            # Oasis
            oasis = random.randrange(20)
            if oasis == 1:
                print("You have found a kelp factory! You and your burger mobile are rested and ready to go!")
                hungrieness = 0
                burger_tiredness = 0
                krabby_patties = 3

        # Ahead Moderate Speed B
        elif user_choice.upper() == "B":
            print("\nI guess we'll get there soon...\n")
            miles_traveled = miles_traveled + random.randrange(5, 12)
            print("\nYou've traveled", miles_traveled, "miles.\n")
            hungrieness = hungrieness + 1
            burger_tiredness = burger_tiredness + 1
            mr_krabs_miles_traveled = mr_krabs_miles_traveled + random.randrange(7, 14)

           # Oasis
            oasis = random.randrange(20)
            if oasis == 1:
                print("You have found an kelp factory! You and your burger mobile are rested and ready to go!")
                hungrieness = 0
                burger_tiredness = 0
                krabby_patties = 3

        # Eat a Krabby Patty
        elif user_choice.upper() == "A":
            if krabby_patties > 0:
                hungrieness = 0
                krabby_patties = krabby_patties - 1
            print("That was a good Krabby Patty, let's get moving!")
            print("\nYou have", krabby_patties, "Krabby Patties left.\n")

            # Hungriness
            if krabby_patties == 0:
                print("\nYou are out of Krabby Patties!\n")

       # Global Loops

        # Hungrieness
        if not done:
            if hungrieness >= 3:
                print("You are hungry! Get some food!")
        elif hungrieness >= 6:
                print("\nYou have died of hunger!")
                done = True

        # Tiredness
        if not done:
            if burger_tiredness >= 8:
                print("\nYour burger mobile is shutting down and the tires popped off! Looks like Mr. Krabs caught ya!\n")
                done = True
        elif burger_tiredness >= 3:
            print("\nYour burger mobile is getting worn-out.")

        # Krabs Caught You
        if not done:
            if mr_krabs_miles_traveled >= miles_traveled:
                print("Mr. Krabs has caught you and he has taken you and the car back! You have lost!")
                done = True

        # Krabs getting close
        if not done:
            if miles_traveled - mr_krabs_miles_traveled <= 15:
                print("Mr. Krabs is getting close!\n")

        # Winning the game
        if miles_traveled >= 200:
            print("You have reached Jellyfish Fields! Patrick meets you there and you share a Krabby Patty in victory! You have won the game!")
            done = True
main()

>>>>>>> 788e083e2b941b607edd7816ebd154ce13fabb39
