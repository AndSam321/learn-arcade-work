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