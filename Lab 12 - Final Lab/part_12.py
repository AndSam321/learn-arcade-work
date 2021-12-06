class Room:
    def __init__(self, description, northwest, north, northesat, east,
                 southeast, south, southwest, west):
        self.description = description
        self.northwest = northwest
        self.north = north
        self.northeast = northeast
        self.east = east
        self.southeast = southeast
        self.south = south
        self.southwest = southwest
        self.west = west


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

main()
