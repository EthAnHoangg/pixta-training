# pixta-oop-training
To manage customers who come to rent a hotel room, one needs the following information: 

Number of days to rent, room type, personal information of the tenants.
For each individual, it is necessary to manage the following information: Full name, age, identity card number.

Requirement 1: Let's build a Person class to manage personal information of room tenants.
Requirement 2: Let's build a VIP class to manage VIP personal information of room tenants. Vip user have 10% discount on price

Requirement 3: Build Type Class to type and price of a room
Requirement 3: Build Room Class to manage information about rooms in the hotel including: Name, Type	


Requirement 4: Develop a Management Tool that support:
Adding and removing new room type according to Type
Adding and removing guest according to Identity card numbers
Calculate room rental for guests (identify guests by ID card number) based on the following formula: (number of rental days * price of each room type). VIP person receive 10% discount
Show available room, occupied room
Calculate revenue from specified start to end date. If a person hasn’t returned room yet, don’t count it into the total revenue

Proposed Management Tool Terminal Interface
1. Add room
2. Remove room
3. Add guest\
  |_ Person\
  |_ VIP
4. Remove guest
5. Show guest
6. Calculate rental
7. Show available room
8. Show occupied room
9. Exit
