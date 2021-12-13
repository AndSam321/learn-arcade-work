class Room:
    def __init__(self, 
                id,
                description, 
                northwest, 
                north, 
                northeast, 
                east,
                southeast, 
                south, 
                southwest, 
                west ):
        self.id          = id
        self.description = description
        self.northwest   = northwest
        self.north       = north
        self.northeast   = northeast
        self.east        = east
        self.southeast   = southeast
        self.south       = south
        self.southwest   = southwest
        self.west        = west
 
class Mobs:
    def __init__(self, room, description, health, damage, name):
        self.room = room
        self.name = name
        self.description = description
        self.health = health
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
        self.inventory = []
