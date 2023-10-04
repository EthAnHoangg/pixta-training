# For each individual, it is necessary to manage the following information:
# Full name, age, identity card number.
import copy

class Person:
    def __init__(self, id, name, age, rent_days, room_number):
        self.name = name
        self.age = age
        self.id = id
        self.rent_days = rent_days
        self.room_number = room_number
    def get_room_number(self):
        return self.room_number
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_id(self):
        return self.id
    
# VIP class to manage VP personal infromation of room tenants
class VIP(Person):
    def __init__(self, id, name, age, rent_days=None, room_number = None):
        super().__init__(id, name, age, rent_days, room_number)
        
class Type:
    def __init__(self, type, price):
        self.type_name = type
        self.price = price

class Room:
    def __init__(self, number, type):
        self.number = number
        self.type = type


# Adding and removing new room type according to Type
# Adding and removing guest according to Identity card numbers
# Calculate room rental for guests (identify guests by ID card number) based on the following formula: (number of rental days * price of each room type). VIP person receive 10% discount
# Show available room, occupied room
# Calculate revenue from specified start to end date. If a person hasn’t returned room yet, don’t count it into the total revenue
class Hotel:
    def __init__(self, name, room_list, guest_list=[], occupied_room=None, available_room=None):
        self.name = name
        self.room_list = room_list
        self.available_room = copy.copy(room_list)
        self.guest_list = guest_list
        self.occupied_room = []
        if guest_list != []:
            for guest in guest_list:
                guest_room_number = guest.get_room_number()
                for i in self.room_list:
                    if i.number == guest_room_number:
                        self.occupied_room.append(i)
                        self.available_room.remove(i)
    def get_rooms(self, number):
        return self.room_list[number]


if __name__ == "__main__":
    print("Hello world")