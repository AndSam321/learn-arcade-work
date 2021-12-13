<<<<<<< HEAD
import random
import sys
import time


def typing(word):
    for letter in word:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(.001)
    print()


class Room:
    def __init__(self,
                 description,
                 northwest,
                 north, northeast,
                 east,
                 southeast,
                 south,
                 southwest,
                 west,
                 ):
=======
class Room:
    def __init__(self, description, northwest, north, northesat, east,
                 southeast, south, southwest, west):
>>>>>>> 5eba78bfea5e7a96d451312a2a3d9ca4a85bf3e0
        self.description = description
        self.northwest = northwest
        self.north = north
        self.northeast = northeast
        self.east = east
        self.southeast = southeast
        self.south = south
        self.southwest = southwest
        self.west = west


<<<<<<< HEAD
class Mobs:
    def __init__(self, room, description, health, damage, name):
        self.room = room
        self.description = description
        self.health = health
        self.name = name
        self.damage = damage


class Item:
    def __init__(self, room, description, name):
        self.room = room
        self.description = description
        self.name = name


class Player:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage


def main():
    # Intro
    typing(
        "Welcome to the Haunted Mansion text adventure game... "
        "\nYour job is simply to FIND A WAY OUT... \nBut, watch out for ghouls along the way... "
        "\nAre you ready to take up the challenge...")

    room_list = []
    # Entryway Room 0
    room = Room("It looks like I'm inside the main entryway of the mansion."
                "\nI see a hallway to my left and a staircase ahead of me."
                "\nShould I go to the hallway or to the stairs?", 1, None,
                6, None, None, None, None, None)
    room_list.append(room)

    # Hallway Room 1
    room = Room("Got it. I'm in this narrow hallway. I see 4 rooms. Looks like there is a boys bedroom and bathroom"
                "\nand a girl's bedroom and bathroom... where to first?,"
                "\nI could always go back.", 3, None, 4, 0, 5, None, 2, None)

    room_list.append(room)

    # Bedroom Room 2
    room = Room("Looks like I'm in a girl's bedroom. Looks pretty normal here...let's go back to the hallway.", None,
                None, 1, None, None, None, None, None)
    room_list.append(room)

    # Bedroom Room 3
    room = Room("Looks like I'm in a boy's bedroom. This room seems to be very messy...", None, None, None, None, 1,
                None, None, None)
    room_list.append(room)

    # Bedroom Room 4
    room = Room("Looks like I'm in a boys bathroom.", None, None, None, None, None, None, 1, None)
    room_list.append(room)

    # Bedroom Room 5
    room = Room("Looks like I'm in the girls bathroom.", 1, None, None, None, None, None, None, None)
    room_list.append(room)

    # Staircase Room 6
    room = Room("I'm at the stairs. North upstairs or south downstairs.", None, 7, None, None, None, 9, None, None)
    room_list.append(room)

    # Attic Room 7
    room = Room("*Cough* I'm in the attic. Huge attic,should I keep exploring or go back?", None, None, None, 8, None,
                6, None, None)
    room_list.append(room)

    # 2nd Room of attic 8
    room = Room("I can't seem to find anything here.", None, None, None, None, None, None, None, 7)
    room_list.append(room)

    # Basement Room 9
    room = Room("I'm downstairs, which seems to be a basement. Should I keep exploring?", None, 6, 10, None, 11, None,
                None, None)
    room_list.append(room)

    # Basement Room 10
    room = Room("I see a couple of boxes over here. Doesn't seem to be anything here though.", None, None, None, None,
                None, 11, 9, None)
    room_list.append(room)

    # Basement Room 11
    room = Room("I see something over here. Looks like its a hidden door. Let's keep going?", 9, 10, None, None, None,
                12, None, None)
    room_list.append(room)

    # Cellar Room 12
    room = Room("I'm in a cellar. It's a little tight down here, but I can keep climbing down.", None, 11, None, None,
                None, 13, None, None)
    room_list.append(room)

    # Final Room 13
    room = Room("This looks like a dungeon down here.", None, 12, None, None, None, 14, 15, None)
    room_list.append(room)

    # Final Room 14
    room = Room("I can feel the border of the left wall. There seems to be some old bookshelves.", 15, 13, None, None,
                None, None, None, None)
    room_list.append(room)

    # Final Room 15
    room = Room("I see a door. It seems to be locked. There's a keyhole here though.", None, None, None, None, None,
                None, None, 16)
    room_list.append(room)

    current_room = 0

    done = False
    while not done:
        print()
        typing(room_list[current_room].description)

        user_input = input("what do you want to do? ")
        command_words = user_input.split(" ")

        if command_words[0] == "go":
            if command_words[1] == "nw":
                next_room = room_list[current_room].northwest
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                else:
                    current_room = next_room

            elif command_words[1] == "n":
                next_room = room_list[current_room].north
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                else:
                    current_room = next_room

            elif command_words[1] == "ne":
                next_room = room_list[current_room].northeast
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                else:
                    current_room = next_room

            elif command_words[1] == "e":
                next_room = room_list[current_room].east
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                else:
                    current_room = next_room

            elif command_words[1] == "se":
                next_room = room_list[current_room].southeast
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                else:
                    current_room = next_room

            elif command_words[1] == "s":
                next_room = room_list[current_room].south
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                else:
                    current_room = next_room

            elif command_words[1] == "sw":
                next_room = room_list[current_room].southwest
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                else:
                    current_room = next_room

            elif command_words[1] == "w":
                next_room = room_list[current_room].west
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                else:
                    current_room = next_room

            elif command_words[1] == "back":
                next_room = room_list[current_room]
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                else:
                    current_room = next_room


=======
def main():
    """print("Welcome to the Haunted Mansion text adventure.")
    print("Your job is to simply find a way out and stay alive...")
    user_input = input("Are you ready to take up the challenge?\nY/N\n")
    if user_input.lower() == "y":
        print("It looks like I'm inside the main entryway of the mansion."
              "\nI see a hallway to my left and a staircase ahead of me."
              "\nShould I go northwest to the hall or northeast to the stairs."
              "What direction do you want to go?")"""

    room_list = []

    # Entryway Room 1
    room = Room("It looks like I'm inside the main entryway of the mansion."
                "\nI see a hallway to my left and a staircase ahead of me."
                "\nShould I go northwest to the hall or northeast to the stairs.", 2, None,
                7, None, None, None, None, None)
    room_list.append(room)

    # Hallway Room 2
    room = Room("Got it. I'm in this narrow hallway. I see 4 rooms. Each is northwest,"
                "northeast, southwest, and southeast. Yeah, there's a lot... which should I go in. I could always"
                "go back to the east.", 4, None, 6, 1, 5, None, 3, None)
    room_list.append(room)

    current_room = 0
    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("\nWhat direction do you want to go? ")

        if user_input.lower() == "nw" or user_input.lower() == "northwest":
            next_room = room_list[current_room].northwest
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        if user_input.lower() == "ne" or user_input.lower() == "northeast":
            next_room = room_list[current_room].northeast
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

            print(next_room)
>>>>>>> 5eba78bfea5e7a96d451312a2a3d9ca4a85bf3e0

main()
