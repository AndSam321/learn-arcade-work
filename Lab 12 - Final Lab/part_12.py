class Room:
    def __init__(self, description, northeast, north, northwest, west,
                 southwest, south, southeast, east):
        self.description = description
        self.northeast = northeast
        self.north = north
        self.northwest = northwest,
        self.west = west
        self.southwest = southwest
        self.south = south
        self.southeast = southeast
        self.east = east

def main():
    print("Welcome to the Haunted Mansion text adventure.")
    print("Your job is to simply find a way out and stay alive...")
    user_input = input("Are you ready to take up the challenge?\nY/N\n")
    if user_input == "Y":
        print(room_list[current_room].description)
    elif user_input == "N":
        quit()

    room_list = []

    # Entryway
    room = Room("It looks like I'm inside the main entryway of the mansion."
                "\nI see a hallway to my left and a staircase ahead of me."
                "\nShould I go northwest to the hall or northeast to the stairs.", 2, None,
                7, None, None, None, None, None)
    room_list.append(room)




    done = False

main()


