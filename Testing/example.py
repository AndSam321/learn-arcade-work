import random


class Room:

    # This is a class that represents the rooms of the game.

    def __init__(self, description, north, west, south, east):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

class Character:
    # This is a class that represents the items you find in the game which are
    # The enemies and the helpers.

    def __init__(self, room, description, health, damage, name):
        self.room = room
        self.description = description
        self.health = health
        self.name = name
        self.damage = damage

# This is the player class for the player
class Player:

    def __init__(self, health, damage):
        self.health = health
        self.damage = damage


# These are ll the rooms of the building
def main():
    print("Hello!")
    print("Welcome to the new way of living. the apocalypse is getting worse and the\n"
          "government have decided to burn the whole town because of the zombie overload\n"
          "most people have left but a few remain including you!")
    print("there is one chopper left in the whole town and its in the Mako hotel,"
          "\nit's up to you to find the chopper and escape with your life or possibly\n"
          "find some precious possessions of your own.")
    print()
    print("Make sure you pay close attention to everything and wish yourself some luck!")
    print("When you take some things and or leave some things they will impact you n the\n"
          "future, so be sure what you take and what you do!"
          "\n SOO, yeah. well don't stand out here get in side waiting to die,\n"
          "get inside, the door is to your north")
    print("type where you want to go and lets get going.")
    print("-------------------------------------------------------")
    # Variable


    room_list = []
    # This is outside
    room = Room("You are outside. There is chaos outside and people\n"
                "are running everywhere. "
                "\nBuildings are burning down. so find an escape!\n"
                "get inside quick", 1, None, 0, None)
    room_list.append(room)

    # this is room one (the lobby)
    room = Room("You are currently in the lobby. There are couches and TVs\n"
                "are still playing.There are drinks on the table and the room\n"
                "is very dark. You can drink some bose and chill of find\n"
                "a different room. It is all up to you, as always.", 4, 2, 0, None)
    room_list.append(room)

    # This is room two (the vip room)
    room = Room("You are in the VIP room, there is gold on the table, a gun,\n"
                "and a bag of cash.\nthe gun only has 2 bullets. you can take\n"
                "the pistol and continue to explore the house, whatever you want.", 5, None, None, 1)
    room_list.append(room)

    # This is room 3 (The Storage)
    room = Room("You are in the storage room. There are bags of food and a few dead bodies.\n "
                "The bags seem to be in good shape so you can take some if you like.", 6, None, None, 10)
    room_list.append(room)

    # This is room 4 (The Kitchen)
    # Take a sword, increase weight or reduce health
    room = Room("You are now in the kitchen. There is something cooking on the stove.\n"
                "There is bloody knives laying on the counter so pay attention there maybe.\n"
                "someone there who may kill you, there is also a sword behind the door\n"
                "you can take the sword(it may be helpful in the future).", None, 11, 1, 5)
    room_list.append(room)

    # This is room 5 (The cafe)
    room = Room("You are in the cafe. There is no one here so do whatever you like but\n"
                "there is blood everywhere. Coffee adds to your energy if you are tired.\n"
                "you can take a shot of coffee but be mindful.\n"
                "Donâ€™t Drink too much!", 8, 6, 2, 4)
    room_list.append(room)

    # This is room 6 (The dark room)
    room = Room("oops this room is very dark, i cant's see anything. Can you? right you cant\n"
                "You can't see anything but by going around you may find useful tools and resources.\n"
                "do you want to search the room? I would if i were you. and then you can leave after\n"
                "", None, None, 3, 10)
                # There is a health drink jar that has 2 drinks if they are all drunk
                # fast the character passes out and probably dies.

    # add navigation like north south and etcâ€¦ to navigate the dark room
    # like north south and more
    room_list.append(room)

    # This is room 7 (The Lounge)
    room = Room("You are in the lounge, you can sleep and rest to regain mental intelligence.\n"
                "It will allow you to be faster than everyone else when you wake up, however \n"
                "keep in mind that things happen when you are asleep. you may get killed.\n"
                "If you feel like the risk is worth it you can """"sleep"""".", None, 8, None, None)
    room_list.append(room)

    # This is room 8 (The pool room)
    room = Room("whew.. that was something at least you are still alive.You are in the indoors\n"
                "pool room. You can /swim/ to heal your wounds.If the water is clean you will be fine\n"
                "but if dirty you get an infection.it's the way it is", None, 7, 5, None)
    room_list.append(room)

    # This is room 9 ( the roof top)
    room = Room("You are on the roof access room. you are safe here so you can now climb north to.\n"
                "the roof access, otherwise you may be caught and killed.\n"
                "", None, 11, None, 8,)
    room_list.append(room)

    # This is room 10 (The west balcony)
    room = Room("You are on the German balcony now, HORRIBLE VIEW. Find you way out of the\n"
                "balcony because you can get shot by the people outside. Find you way back\n"
                "inside to safety.If you cannot you will die", None, 6, 3, None)
    room_list.append(room)

    # This is room 11 (The East balcony)
    room = Room("You are on the Italian balcony. Great progress. Find the rooftop to get rescued.\n"
                "You do not have a lot of time to mess about, and make sure you have resources you may need\n"
                "before you go outside the building. Good luck and god speed.", None, 8, 4, 9)
    room_list.append(room)

    # This is the Hidden room 12. room on roof
    # If they pick zero they die
    room = Room("You are in the secret room twelve. this room has a lot of things you can take with you to escape.\n"
                "you however can only go west out of the door. the access back in the building is gone\n"
                "it's not stable once you get out of the door.You can say in here and eat or stock up all the\n"
                "precious stuff inside or you can leave right now with nothing on you.", None, 13, None, None)
    room_list.append(room)

    # This is the room 13
    # It only goes to the end room 14 is the end
    room = Room("you are on the helipad, you have done a great job.\n"
                "now! you don't happen to have a gallon of gas on you /n"
                "for this chopper. anyway lets get out of here", 14, None, None, None)
    room_list.append(room)
    current_room = 0

# Room 6
    choice_list = []
    # If you sleep it's a risk
    choice = Character(6, "Well this is an empty one... Well, move on", None, None, "empty room")
    choice_list.append(choice)

    # Room 7
    # if they sleep all their stuff disappear and health reduced
    choice = Character(7, "Well this is a nice bedroom. You can rest on the\n"
                          "\ncomfy bed......."
                          "\nit will boost your energy. if you sleep you're in danger.", 40, 20, "rest", )
    choice_list.append(choice)

    # Room 8
    # This is a roof access
    choice = Character(8, "We got ourselves a swimming pool, you can swim to heal yourself\n"
                          "be mindful that it's a risk,", 100, 20, "swim")
    choice_list.append(choice)

    # Room 9
    choice = Character(9, "Yes, we got a staircase which will access the top if i'm right\n"
                          "we are almost there. Good work. I would access roof if i were you\n"
                          , None, None, "access roof")
    choice_list.append(choice)

    # Room 10
    choice = Character(10, "Just a balcony nothing special. Move on", None, None, "balcony")
    choice_list.append(choice)

    # Room 11
    choice = Character(11, "Just a balcony nothing special. Move on", None, None, "balcony")
    choice_list.append(choice)

    # Room Number 12
    # This is the gold
    choice = Character(12, "Gold, you can take some more gold", 20, 100, "more gold")
    choice_list.append(choice)

    # This is the gas
    choice = Character(12, "The gas can maybe. you can take the gas can", 100, None, "gas can")
    choice_list.append(choice)

    # You can take a bag of money
    choice = Character(12, "We have some money you can take cash", 20, 100, "cash")
    choice_list.append(choice)

    # Room Number 13
    choice = Character(13, "Yes yes yes, we got a chopper. Let's fly away\n"
                         , 100, None, "fly away")
    choice_list.append(choice)

    player = Player(70, 15)


    # User input stuff
    done = False
    room_change = True
    while not done:
        if room_change:

            # User choice
            # Talks about the room
            print(room_list[current_room].description)
            # Going into the room triggers the enemy
            for choice in choice_list:
                if choice.room == current_room:
                    print(choice.description)
            room_change = False
        user_choice = input("\nWant do you want to do?  ")
        # User options
        # If user quits
        if user_choice.lower() == "quit":
            print("Scream loser bye!!!! I hope you DIE")
            done = True

        # If user wants to go north
        elif user_choice.lower() == "north":
            next_room = room_list[current_room].north
            room_change = True
            if next_room is None:
                print()
                print("\nYou can't go there. find another way to the next room")
            else:
                current_room = next_room

        # If user wants to go east
        elif user_choice.lower() == "east":
            next_room = room_list[current_room].east
            room_change = True
            if next_room is None:
                print()
                print("\n It looks like you cannot go in that direction. Go another way")
            else:
                current_room = next_room

        # If user wants to go south
        elif user_choice.lower() == "south":
            next_room = room_list[current_room].south
            room_change = True
            if next_room is None:
                print()
                print("\nIt looks like you cannot go in that direction. Find another way")
            else:
                current_room = next_room

        # If user wants to go west
        elif user_choice.lower() == "west":
            next_room = room_list[current_room].west
            room_change = True
            if next_room is None:
                print()
                print("\nNope you cannot migrate to the cali coast. Sorry not sorry.\n"
                      "any who, let's move on.")
            else:
                current_room = next_room

        # The user can choose to attack
        elif user_choice.lower() == "drink":
            print()
            print("\nAlright! let's drink! I am sure you are not underage at all?"
                  "\ndon't drink too much though because you will be drunk. There is"
                  "\nnothing worse than trying to escape drunk!")
            print()
            print("Anyway, what do you want? beer or beer? haha")

        # The user then has to pick what to do
        if user_choice.lower() == "beer":
            for choice in choice_list:
                if choice.room == current_room:
                    player.damage = random.randrange(1, 30)
                    choice.health -= player.damage
                    print()
                    print("Oh yeah! oh yeah that's some good beer!")
                    print("That beer took", choice.health, " from us\n"
                                                                        "WHOOPS")
                    if choice.damage == 30:
                        print()
                        print("Well I told you not to drink")
                        player.health = 70
                    else:
                        print("You're going to be weak now, at least for a while")
                        player.health = player.health - choice.damage


        # This is if the user choses gold
        if user_choice.lower() == "gold" or user_choice.lower() == "take gold":
            for choice in choice_list:
                if choice.room == current_room:
                    player.damage = random.randrange(1, 20)
                    print()
                    print("Gold it is. But it may be a problem later in the future")
                    print("The gold took", choice.health, "health from us\n")
                    if choice.damage == 20:
                        print()
                        player.health = player.health
                    else:
                        print("let's be careful")




        elif user_choice.lower() == "gun" or user_choice.lower == "take gun":
            for choice in choice_list:
                if choice.room == current_room:
                    choice.health = choice.health - player.damage
                    print()
                    print("Improvised special move: The Comet Home Run!")
                    print("Nice! That did", player.damage, "damage!")
                    print("That darn zombie is at", choice.health, " left!")
                    if choice.health <= 0:
                        print()
                        print("Yahoo! Yah did it! He dead! Again!")
                        player.hp = 65
                    else:
                        print("Kaboom! Let's keep it up!")
                        print("Ayaya! The zombie is attacking! He's using bite!")
                        player.health = player.health - choice.damage
                        print("Boof! That did", choice.damage, "damage!")

        elif user_choice.lower() == "check health":
            print()
            if player.health <= 10:
                print("You're low on health! Be super careful! death is real you know")
                print("Health:", player.health)

            elif player.health <= 50:
                print("Well, we are still alive! It's just a small wound!")
                print("Health:", player.health)

            else:
                print("Don't check the health. You are barely drunk!")
                print("Health:", player.health)


# Main function
main()