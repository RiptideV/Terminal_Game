
import os

def showInstructions():
    print('''
Terminal Text Game
==================
Commands:
    go [direction]
    get [item]
''')

run = True
menu = True
play = False
rules = False

HP = 100
ATK = 3



def save():
    list = [
        name,
        str(HP),
        str(ATK),
        currentRoom,
        inventory
    ]

    f = open("save.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()


while run:
    while menu:
        print("1: NEW GAME")
        print("1: LOAD GAME")
        print("1: RULES")
        print("1: QUIT GAME")

        if rules:
            print("placeholder")
            rules = False
            choice = ""
            input("> ")

        choice = input("> ")
        if choice == "1":
            name = input("What is your name? ")
            menu = False
            play = True

        if choice == "2":
            pass
        if choice == "3":
            rules = True
        if choice == "4":
            quit()

    while play:
        save() == autosave
        print(f"Welcome {name} to the Terminal Text Game!")

        dest = input("> ")
        if dest == "0":
            play = False
            menu = True
            save()



def status():
    print("---------------------------")
    print(f"Current Room: {currentRoom}")
    print(f"Inventory: {inventory}")

    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]:
        room_item = rooms[currentRoom]["item"]
        print(f"You see a {room_item}.")

    print("---------------------------")


inventory  = []

currentRoom = "Kitchen"

rooms = {
            "Garden"       : {
                            "north": "Dining Room",
                            "item" : "shears"
                             },
            "Dining Room"  : {
                            "south": "Garden",
                            "west" : "Hall",
                            "item" : "potion"
                             },
            "Hall"         : {
                            "south": "Kitchen",
                            "east" : "Dining Room",
                            "item" : "key"
                             },
            "Kitchen"       :{
                            "north": "Hall",
                            "item": "monster"
                             }
        }

showInstructions()

while True:

    status()

    move = input('> ')

    move = move.split(" ", 1)

    os.system('cls')

    if move[0] == 'get':
        if move[1] == rooms[currentRoom]["item"]:
            print(f"You got a {move[1]}!")
            inventory.append(move[1])
            rooms[currentRoom]["item"] = ""
            print(inventory)
        else:
            print(f"You don't see a {move[1]} here.")

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            print(f"You are now in the {currentRoom}.")
        else:
            print(f"You can't go {move[1]} from here.")

#Victory condtion: get the key, potion and escape through the garden
    if "key" in inventory and "potion" in inventory and currentRoom == "Garden":
        print("Congratulations! You've escaped the house.")
        break
#Loss Condition: getting eaten by the monster