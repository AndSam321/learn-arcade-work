import sys
import time
import random


def typing(word):
    for letter in word:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(.001)
    print()


class Room:
    Id = 0

    def __init__(self,
                 description,

                 northwest,
                 north,
                 northeast,
                 east,
                 southeast,
                 south,
                 southwest,
                 west,
                 item,
                 mob):
        self.id = Room.Id
        self.description = description
        self.northwest = northwest
        self.north = north
        self.northeast = northeast
        self.east = east
        self.southeast = southeast
        self.south = south
        self.southwest = southwest
        self.west = west
        self.item = item
        self.mob = mob


class Mobs:
    available_mobs = ["zombie", None, None, None, None, None]

    def __init__(self, room, description, health, damage, name):
        self.room = room
        self.description = description
        self.health = health
        self.name = name
        self.damage = damage


class Item:
    available_items = ["sword"]

    def __init__(self, description, name):
        self.description = description
        self.name = name


class Player:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage


def get(_item, _item_list, _room, _inventory):
    if _item == _room.item.name:
        for item in _item_list:
            if item.name == _item:
                print(f"found {_item}")
                _inventory.append(_item)
                return
        print(f"couldnt find {_item}")
    else:
        print(f"{_item} is not in this room")


def use(_item):
    if _item == "sword":
        print("you swing at the monster")
    elif _item == "key":
        print("you used the key and opened a door")
    else:
        print("you cant use that")


room_list = []


def setup():
    # Entryway Room 0
    entryway = Room("It looks like I'm inside the main entryway of the mansion."
                    "\nI see a hallway to my left and a staircase ahead of me."
                    "\nShould I go northwest to the hall or northeast to the stairs.", 1, None,
                    6, None, None, None, None, None)

    sword = Item("You found a sword", "sword")
    entryway.item = sword

    room_list.append(entryway)

    # Hallway Room 1
    hallway = Room("Got it. I'm in this narrow hallway. I see 4 rooms. Each is northwest,"
                   "northeast, southwest, and southeast. Yeah, there's a lot... which should I go in. I could always"
                   "go back to the east.", 3, None, 4, 0, 5, None, 2, None)

    room_list.append(hallway)

    # Bedroom Room 2
    girl_bedroom = Room("Looks like I'm in a girl's bedroom.", None, None, 1, None, None, None, None, None)
    room_list.append(girl_bedroom)

    # Bedroom Room 3
    boy_bedroom = Room("Looks like I'm in a boy's bedroom.", None, None, None, None, 1, None, None, None)

    key = Item("a rusty looking key ", "key")
    boy_bedroom.item = key
    room_list.append(boy_bedroom)

    # Bedroom Room 4
    boy_bathroom = Room("Looks like I'm in a boys bathroom.", None, None, None, None, None, None, 1, None)
    room_list.append(boy_bathroom)

    # Bedroom Room 5
    girl_bathroom = Room("Looks like I'm in the girls bathroom.", 1, None, None, None, None, None, None, None)
    room_list.append(girl_bathroom)

    # Staircase Room 6
    stairs = Room("I'm at the stairs. North upstairs or south downstairs.", None, 7, None, None, None, 9, None, None)
    room_list.append(stairs)

    # Attic Room 7
    attic = Room("*Cough* I'm in the attic. Huge attic,should I keep exploring or go back?", None, None, None, 8, None,
                 6,
                 None, None)
    room_list.append(attic)

    # 2nd Room of attic 8
    extension_of_attic = Room("I can't seem to find anything here.", None, None, None, None, None, None, None, 7)
    room_list.append(extension_of_attic)

    # Basement Room 9
    basement = Room("I'm downstairs, which seems to be a basement. Should I keep exploring?", None, 6, 10, None, 11,
                    None,
                    None, None)
    room_list.append(basement)

    # Basement Room 10
    basement_room_10 = Room("I see a couple of boxes over here. Doesn't seem to be anything here though.", None, None,
                            None, None,
                            None, 11, 9, None)
    room_list.append(basement_room_10)

    # Basement Room 11
    basement_room_11 = Room("I see something over here. Looks like its a hidden door. Let's keep going?", 9, 10, None,
                            None, None, 12,
                            None, None)
    room_list.append(basement_room_11)

    # Cellar Room 12
    cellar_room_12 = Room("I'm in a cellar. It's a little tight down here, but I can keep climbing down.", None, 11,
                          None, None,
                          None, 13, None, None)
    room_list.append(cellar_room_12)

    # Final Room 13
    final_room_13 = Room("This looks like a dungeon down here.", None, 12, None, None, None, 14, 15, None)

    # Final Room 14
    final_room_14 = Room("I can feel the border of the left wall. There seems to be some old bookshelves.", 15, 13,
                         None, None,
                         None, None, None, None)
    room_list.append(final_room_14)

    # Final Room 15
    final_room_15 = Room("I see a door. It seems to be locked. There's a keyhole here though.", None, None, None, None,
                         None, None,
                         None, 16)
    room_list.append(final_room_15)

    # END
    end_room = Room("End,", None, None, None, None, None, None, None, None)
    room_list.append(end_room)



def main():
    setup()

    typing(
        "Welcome to the Haunted Mansion text adventure game... \nYour job is simply to FIND A WAY OUT... \nBut, watch out for ghouls along the way... \nAre you ready to take up the challenge?")

    current_room = 0
    done = False
    while not done:
        print()

        typing(room_list[current_room].description)

        typing("what do you want to do?")
        command = input(">>> ").lower().split(" ")

        if command[0] == "go":
            if command[1] == "nw":
                next_room = room_list[current_room].northwest
                if next_room is None:
                    print("\nYou can't go that way.")
                else:
                    current_room = next_room


main()

done = False
    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("\nWhich direction do you want to go? ")
        if user_input.lower() == "nw" or user_input.lower() == "northwest":
            next_room = room_list[current_room].northwest
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_input.lower() == "ne" or user_input.lower() == "northeast":
            next_room = room_list[current_room].northeast
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "se" or user_input.lower() == "southeast":
            next_room = room_list[current_room].southeast
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "sw" or user_input.lower() == "southwest":
            next_room = room_list[current_room].southwest
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room