
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
    room = Room("You are in the living room. You can go into the bedroom to the north or walk into the south hallway to the east.", 3, 1, None, None)
    room_list.append(room)

    # Room 1
    room = Room("You are in the south hall.", None, 2, None, 0)
    room_list.append(room)

    # Room 2
    room = Room("You are in the kitchen.", 5, None, None, 1)
    room_list.append(room)

    # Room 3
    room = Room("You are in the bedroom.", None, 4, 0, None)
    room_list.append(room)

    # Room 4

    room = Room("You are in the north hall.", None, 5, None, 3)
    room_list.append(room)

    # Room 5
    room = Room("You are in the master bedroom.", 6, None, 2, 4)
    room_list.append(room)

    # Room 6
    room = Room("You are in the attic.", None, None, 5, 7)
    room_list.append(room)

    # Room 7
    room = Room("You are in the attic bedroom.", None, 6, None, None)
    room_list.append(room)

    current_room = 0



    print(room_list[current_room].description)



main()


