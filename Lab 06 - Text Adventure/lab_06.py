class Room:

    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    current_room = 0
    # Room 0
    room_list = []
    my_room = Room("You are in the living room. You can go into the bedroom to the north or walk into the south hallway to the east.", 3, 1, None, None)
    room_list.append(my_room)
    # Room 1
    room_list = []
    my_room = Room("You are in the south hall.", None, 2, None, 0)
    room_list.append(my_room)
    # Room 2
    room_list = []
    my_room = Room("You are in the kitchen.", 5, None, None, 1)
    room_list.append(my_room)
    # Room 3
    room_list = []
