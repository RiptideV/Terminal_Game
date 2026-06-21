

import os

run = True
menu = True
play = False
rules = False

HP = 100
ATK = 3

def clear():
    os.system('cls')

def draw():
    print("xX--------------------Xx")
def save():
    list = [
        name,
        str(HP),
        str(ATK)
    ]

    f = open("save.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()


while run:
    while menu:
        clear()
        draw()
        print("1: NEW GAME")
        print("2: LOAD GAME")
        print("3: RULES")
        print("4: QUIT GAME")
        draw()

        if rules:
            print("placeholder")
            rules = False
            choice = ""
            print(">")
            
        else:
            choice = input("> ")
            
        if choice == "1":
            clear()
            draw()
            name = input("What is your name? ")
            menu = False
            play = True
            draw()

        elif choice == "2":
            f = open("save.txt", "r")
            load_list = f.readlines()
            name = load_list[0]
            HP = load_list[1][:-1]
            ATK = load_list[2][:-1]
            clear()
            draw()
            print(name, HP, ATK)
            print("Game Loaded!")
            draw()
            input("> ")
            menu = False
            play = True
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()  #autosave
        print(f"Welcome {name} to the Terminal Text Game!")
        clear()
        draw()
        print("0: SAVE AND QUIT")
        draw()

        dest = input("> ")
        if dest == "0":
            play = False
            menu = True
            save()
        