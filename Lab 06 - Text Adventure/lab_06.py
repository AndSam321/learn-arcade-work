class Room:

    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():

    # Room 0
    room_list = []
    room = Room("You are in the living room. You can go into the bedroom to the north "
                "\nor walk into the south hallway to the east.", 3, 1, None, None)
    room_list.append(room)

    # Room 1
    room = Room("You are in the south hall. You can go back to the living room "
                "\nor continue east to the kitchen.", None, 2, None, 0)
    room_list.append(room)

    # Room 2
    room = Room("You are in the kitchen. You can move north into the master bedroom "
                "\nor go back west to the hall.", 5, None, None, 1)
    room_list.append(room)

    # Room 3
    room = Room("You are in the bedroom. You can go west into the north wall "
                "\nor south into the living room.", None, 4, 0, None)
    room_list.append(room)

    # Room 4

    room = Room("You are in the north hall. You can move west into the bedroom "
                "\nor east into the master bedroom.", None, 5, None, 3)
    room_list.append(room)

    # Room 5
    room = Room("You are in the master bedroom. Pretty spacious... "
                "\nThere seems to be a ladder that leads to the attic in the north. "
                "\nYou can always go west to go back into the north hall or south into the kitchen.", 6, None, 2, 4)
    room_list.append(room)

    # Room 6
    room = Room("You are in the attic. It's a little dark in here. "
                "\nSeems to be a room up here to the west. "
                "\nYou can always go back down to the master bedroom to the south.", None, None, 5, 7)
    room_list.append(room)

    # Room 7
    room = Room("You are in the attic bedroom. Little quiet...too quiet. "
                "\nYou can go back east into the attic.", None, 6, None, None)
    room_list.append(room)

    current_room = 0

    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("\nWhat direction do you want to go? ")

        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
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

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
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

        elif user_input.lower() == "q" or user_input.lower() == "quit":
            print("Thanks for playing!")
            done = True


main()