from hotel import *

# Create room types
single = Type("Single", 50)
double = Type("Double", 100)
president = Type("President", 200)



# Create a hotel
room1 = Room(101, single)
room2 = Room(102, single)
room3 = Room(103, double)
room4 = Room(104, double)
room5 = Room(105, double)
room6 = Room(106, double)
room7 = Room(107, double)
room8 = Room(108, double)
room9 = Room(109, double)
room10 = Room(110, double)
room11 = Room(111, president)
room12 = Room(112, president)
room_list = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10, room11, room12]


# create guests
guest1 = Person(1, "John Jeremiah", 36, 3, 101) # id, name, age, rent_days, room_number
guest2 = Person(2, "Alex Wang", 25, 2, 102)
guest3 = Person(3, "Marry Jane", 30, 1, 103)
guest4 = Person(4, "Tommy Lee", 40, 2, 112)
guest_list = [guest1, guest2, guest3, guest4]

hotel = Hotel("Hilton", room_list, guest_list)

class Management_Tool:
    def __init__(self, hotel):
        self.hotel = hotel

    # add room and remove rooms
    def add_room(self, room):
      
        self.hotel.room_list.append(room)
        self.hotel.available_room.append(room)
    def remove_room(self, room):
        self.show_available_room()
        self.hotel.room_list.remove(room)
        self.hotel.available_room.remove(room)

    # add guest and remove guest
    def add_guest(self, guest):    
        for i in self.hotel.available_room:
            if i.number == guest.room_number:
                self.hotel.occupied_room.append(i)
                self.hotel.available_room.remove(i)
                self.hotel.guest_list.append(guest)
                return
        print("Room is not available")
    def remove_guest(self, guest):
        self.show_guest()
        self.hotel.guest_list.remove(guest)
    def show_guest(self):
        for i in self.hotel.guest_list:
            print(f"ID: {i.id}, Name: {i.name}, Age: {i.age}, Rent days: {i.rent_days}, Room number: {i.room_number}")
        print("===============================================")

    # calculate rental
    def calculate_rental(self, guest_id):
        print(f"=================== Rental price =====================")
        print(f"Guest ID: {guest_id}")
        for i in self.hotel.guest_list:
            if i.id == guest_id:
                for j in self.hotel.room_list:
                    if j.number == i.room_number:
                        if isinstance(i, VIP):
                            return i.rent_days * j.type.price * 0.9
                        return i.rent_days * j.type.price
                
    def show_available_room(self):
        for i in self.hotel.available_room:
            print(i.number, i.type.type_name)
        print("===============================================")
    def show_occupied_room(self):
        for i in self.hotel.occupied_room:
            print(i.number)

    def display_menu(self):
        print("1. Add room")
        print("2. Remove room")
        print("3. Add guest")
        print("4. Remove guest")
        print("5. Show guest")
        print("6. Calculate rental")
        print("7. Show available room")
        print("8. Show occupied room")
        print("9. Exit")
        choice = int(input())
        
        #create switch case for choice
        if choice == 1:
            room_number = int(input("Enter room number: "))
            room_type = input("Enter room type: ")
            room = Room(room_number, room_type)
            self.add_room(room)
            self.show_available_room()

        elif choice == 2:
            self.show_available_room()
            room_number = int(input("Enter room number: "))
            for i in self.hotel.available_room:
                if i.number == room_number:
                    self.remove_room(i)
                    self.show_available_room()

        elif choice == 3:
            print("1. VIP")
            print("2. Normal")
            choice = int(input())
            if choice == 1:
                guest_id = int(input("Enter guest id: "))
                guest_name = input("Enter guest name: ")
                guest_age = int(input("Enter guest age: "))
                guest = VIP(guest_id, guest_name, guest_age)
                self.add_guest(guest)
            elif choice == 2:
                guest_id = int(input("Enter guest id: "))
                guest_name = input("Enter guest name: ")
                guest_age = int(input("Enter guest age: "))
                guest_rent_days = int(input("Enter rent days: "))
                guest_room_number = int(input("Enter room number: "))
                guest = Person(guest_id, guest_name, guest_age, guest_rent_days, guest_room_number)
                self.add_guest(guest)
                
        elif choice == 4:
            guest_id = int(input("Enter guest id: "))
            for i in self.hotel.guest_list:
                if i.id == guest_id:
                    self.remove_guest(i)
        elif choice == 5:
            print("================ Guest list ================")
            self.show_guest()
        elif choice == 6:
            guest_id = int(input("Enter guest id: "))
            print(self.calculate_rental(guest_id))
        elif choice == 7:
            print("================ Available room ================")
            self.show_available_room()
        elif choice == 8:
            print("================ Occupied room ================")
            self.show_occupied_room()
        elif choice == 9:
            exit()


if __name__ == "__main__":
    while True:
        management_tool = Management_Tool(hotel)
        management_tool.display_menu()