import time
import json
import random
from classes import Room, Item, Player, Mobs


# Typing function rather print out each statement
def typing(word):
    for letter in word:
        print(letter, end="", flush=True)
        time.sleep(.01)
    print()


# Get function to find the actual item
def get(_item, _item_list, _room, _inventory):
    if _item == _room.item.name:
        for item in _item_list:
            if item.name == _item:
                print(f"found {_item}")
                _inventory.append(_item)
                return
        print(f"Couldn't find {_item}")
    else:

        print(f"{_item} is not in this room!")


# Loading JSON file here
def load_room_data(_room_list: list):
    with open("rooms.json", "r") as data_file:
        room_data = json.load(data_file)

    for room in room_data:
        temp_room = Room(
            room["id"],
            room["description"],
            room["northwest"],
            room["north"],
            room["northeast"],
            room["east"],
            room["southeast"],
            room["south"],
            room["southwest"],
            room["west"]
        )
        _room_list.append(temp_room)


def main():
    # List of all the variables
    room_list = []
    item_list = []
    mob_list = []
    final_door_locked = True

    # Loading the room list data
    load_room_data(room_list)

    # Setting player location
    current_room = 0
    previous_room = 0

    # Player Stats
    player = Player(100, 15)

    # Monsters

    monster1 = Mobs(0, "\nThere appears to be a monster standing in the middle of the room!\n", 40, 15, "zombie")
    monster2 = Mobs(3, "\nThere appears to be a monster standing in the middle of the room!\n", 40, 15, "zombie")
    mob_list.append(monster1)
    mob_list.append(monster2)
    monster_in_room = False

    # Items
    arrows = 3
    sword = Item(0, "You found a shiny sword!", "Sword")
    bow = Item(3, f"A wooden bow with {arrows} arrows", "Bow")
    key = Item(5, "You found a key to a door. It doesn't look like it fits the front door..."
                  "will have to find another way out.", "Key")
    item_list.append(sword)
    item_list.append(bow)
    item_list.append(key)

    # Typing out intro
    typing("Welcome to the Haunted Mansion text adventure game... "
           "\nYour job is simply to FIND A WAY OUT... "
           "\nBut, watch out for ghouls along the way... "
           "\nAre you ready to take up the challenge?"
           "\nTips: Use commands like 'get', 'go' , or 'use' to interact. "
           "\nUse can always use 'inventory' to check what you have.")

    input("\nPress enter to continue...")

    done = False
    while not done:
        typing(room_list[current_room].description)

        # Monster check to see if it matches the player's current room
        for monster in mob_list:
            if monster.room == current_room:
                current_monster = monster
                print(monster.description)
                monster_in_room = True
                break

        typing("What do you want to do?")
        command_words = input("Enter your command: ").split(" ")

        # First command word go
        if command_words[0] == "go":
            if current_room == 16:
                typing(room_list[current_room].description)
                break
            if current_room == 15 and command_words[1] == "out":
                if not final_door_locked:
                    current_room = 16
            if command_words[1] == "nw":
                next_room = room_list[current_room].northwest
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                    input("\npress enter to continue...")
                else:
                    previous_room = current_room
                    current_room = next_room

            elif command_words[1] == "n":
                next_room = room_list[current_room].north
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                    input("\npress enter to continue...")
                else:
                    previous_room = current_room
                    current_room = next_room

            elif command_words[1] == "ne":
                next_room = room_list[current_room].northeast
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                    input("\npress enter to continue...")
                else:
                    previous_room = current_room
                    current_room = next_room

            elif command_words[1] == "e":
                next_room = room_list[current_room].east
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                    input("\npress enter to continue...")
                else:
                    previous_room = current_room
                    current_room = next_room

            elif command_words[1] == "se":
                next_room = room_list[current_room].southeast
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                    input("\npress enter to continue...")
                else:
                    previous_room = current_room
                    current_room = next_room

            elif command_words[1] == "s":
                next_room = room_list[current_room].south
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                    input("\nPress enter to continue...")
                else:
                    previous_room = current_room
                    current_room = next_room

            elif command_words[1] == "sw":
                next_room = room_list[current_room].southwest
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                    input("\nPress enter to continue...")
                else:
                    previous_room = current_room
                    current_room = next_room

            elif command_words[1] == "w":
                next_room = room_list[current_room].west
                if next_room is None:
                    print()
                    print("\nYou can't go that way.")
                    input("\nPress enter to continue...")
                else:
                    previous_room = current_room
                    current_room = next_room

            elif command_words[1] == "back":
                current_room = previous_room

        # Command word for getting an item
        elif command_words[0] == "get":
            _item = command_words[1]
            for item in item_list:
                if item.room == current_room:
                    if item.name == _item:
                        item.room = -1
                        player.inventory.append(item)
                        typing(item.description)
                        input("\nPress enter to continue...")
                        break
                    else:
                        continue
                else:
                    continue
            print(f"{_item} is not in this room")

        elif command_words[0] == "inventory":
            for _item in player.inventory:
                typing(_item.name)

            input("\nPress enter to continue...")
        # Command word for using an item
        elif command_words[0] == "use":
            if command_words[1] == "sword":
                for item in player.inventory:
                    if item.name == "sword":
                        if monster_in_room:
                            monster.health -= player.damage * 2
                            if monster.health <= 0:
                                monster_in_room = False
                                typing("The monster is dead")
                                break
                            player.health -= monster.damage
                            typing(
                                f"You swing at the monster and deal {player.damage * 2} damage. "
                                f"\nThe monster has {monster.health}hp")
                            typing(
                                f"But the monster swings back at you, dealing {monster.damage} damage! "
                                f"\nYou now have {player.health}hp")
                            break
                        else:
                            typing("You swung at nothing!")
                    typing("You don't have a sword")
            elif command_words[1] == "bow":
                for item in player.inventory:
                    if item.name == "bow":
                        if monster_in_room:
                            monster.health -= player.damage * 3
                            arrows -= 1
                            monster_in_room = False
                            typing(
                                f"You shoot an arrow at the monster and deal 45 damage!"
                                f"\nThe monster has dies. You now have {arrows} arrows")
                            break
                        else:
                            typing("You shoot at nothing!")
                    typing("You don't have a bow")

            input("\nPress enter to continue...")

        elif command_words[0] == "open" and command_words[1] == "door":
            for _item in player.inventory:
                if _item.name == "key":
                    typing("You opened the door!")
                    final_door_locked = False
                    input("\nPress enter to continue...")
                    break
            typing("You don't have a key!")

        else:
            typing("That command is not valid!")
            input("...")

    typing("Congratulations, Game Over!")
    input("\nPress enter to quit...")


main()
