

import os
import random
import msvcrt
import time
import os


run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True

HP = 100
HPMAX = HP
ATK = 3
pot = 1
elx = 1
gold = 0
x = 0
y = 0
        #x = 0      #x = 1      #x = 2      #x = 3      #x = 4      #x = 5     #x = 6
map = [["plains",  "plains",   "empty",   "plains",  "forest", "mountain",       "cave"],  # y = 0
       ["forest",  "forest",   "forest",   "forest",  "forest",    "hills",   "mountain"],  # y = 1
       ["forest",  "fields",   "bridge",   "plains",   "hills",   "forest",      "hills"],  # y = 2
       ["plains",    "shop",     "town",    "major",  "plains",    "hills",   "mountain"],  # y = 3
       ["plains",  "fields",   "fields",   "plains",   "hills", "mountain",   "mountain"]]  # y = 4

y_len = len(map)-1
x_len = len(map[0])-1

biome = {
    "plains": {
        "t": "plains",
        "e": True},
    "forest": {
        "t": "forest",
        "e": True},
    "fields": {
        "t": "fields",
        "e": False},
    "town": {
        "t": "town",
        "e": False},
    "hills": {
        "t": "hills",
        "e": True},
    "mountain": {
        "t": "mountain",
        "e": True},
    "cave": {
        "t": "cave",
        "e": True},
    "shop": {
        "t": "shop",
        "e": False},
    "bridge": {
        "t": "bridge",
        "e": True},
    "major": {
        "t": "major",
        "e": False},
    "void": {
        "t": "empty",
        "e": False},
}

e_list = ["Skeleton", "Goblin", "Zombie", "Ghost", "Mummy"]

mobs = {
    "Skeleton": {
        "hp": 20,
        "atk": 5,
        "gold": 5
    },
    "Goblin": {
        "hp": 15,
        "atk": 3,
        "gold": 3
    },
    "Zombie": {
        "hp": 30,
        "atk": 4,
        "gold": 7
    },
    "Ghost": {
        "hp": 25,
        "atk": 6,
        "gold": 10
    },
    "Mummy": {
        "hp": 35,
        "atk": 7,
        "gold": 15
    }
}


current_tile = map[y][x]
print(current_tile)
name_of_tile = biome[current_tile]["t"]
enemy_tile = biome[current_tile]["e"]

weapon = {
    "sword": {"damage": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    "axe": {"damage": [2, 3, 4, 5, 6, 9, 8, 9, 10]},
}

damage_list = weapon["axe"]["damage"]   # change to "sword" or "axe"
dmgindex = 0

move_delay = 0.12
last_move = 0








def clear():
    os.system('cls')

def draw():
    print("xX--------------------Xx")

def save():
    list = [
        name.strip(),
        str(HP),
        str(ATK),
        str(pot),
        str(elx),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    f = open("save.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

def build_screen(index):
    damage_strings = [str(x) for x in damage_list]
    dmgvalues = "Damage: " + " ".join(damage_strings)

    prefix = "Damage: "
    before_selected = " ".join(damage_strings[:index])

    if index == 0:
        arrow_pos = len(prefix)
    else:
        arrow_pos = len(prefix) + len(before_selected) + 1

    arrow_line = " " * arrow_pos + "^"
    return dmgvalues, arrow_line

def draw_screen(index):
    clear()
    dmgvalues, arrow_line = build_screen(index)
    print(dmgvalues)
    print(arrow_line)


def battle():

    global fight, play, run, HP, pot, elx, gold, dmgindex, last_move

    enemy = random.choice(e_list)
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["atk"]
    gold = mobs[enemy]["gold"]

    while fight:
        clear()
        draw()
        print("You are fighting a " + enemy + "!")
        draw()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(name + "'s HP: " + str(HP) + "/" + str(HPMAX))
        draw()
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elx))
        draw()
        print("1: ATTACK")
        if pot > 0:
            print("2: USE POTION")
        if elx > 0:
            print("3: USE ELIXIR")
        draw()

        choice = input("> ")

        if choice == "1":
            draw_screen(dmgindex)
            rolling = True
            while rolling:
                now = time.time()

                if msvcrt.kbhit():
                    char = msvcrt.getch()
                    if char == b'\r':
                        clear()
                        print("Damage:", damage_list[dmgindex])
                        rolling = False

                if now - last_move >= move_delay:
                    dmgindex = (dmgindex + 1) % len(damage_list)
                    draw_screen(dmgindex)
                    last_move = now

                time.sleep(0.01)





while run:
    while menu:
        clear()
        print(""" 
 _____  ______ _ __      ________ 
|  __ \|  ____| |\ \    / /  ____|
| |  | | |__  | | \ \  / /| |__   
| |  | |  __| | |  \ \/ / |  __|  
| |__| | |____| |___\  /  | |____ 
|_____/|______|______\/   |______|""")
        print("V.0.1")
        print("By: RiptideV")
        print(" ")
        draw()
        print("1: NEW GAME")
        print("2: LOAD GAME")
        print("3: RULES")
        print("4: QUIT GAME")
        draw()

        if rules:
            print("These are the rules of the game: ")
            rules = False
            choice = ""
            input(">")

            
        else:
            choice = input("> ")
            
        if choice == "1":
            clear()
            draw()
            name = input("What is your name? ")
            draw()
            menu = False
            play = True
            

        elif choice == "2":
            try:
                f = open("save.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0].strip()
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elx = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    draw()
                    print(name, HP, ATK)
                    print("Game Loaded!")
                    draw()
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Save file is corrupted!")
                    input("> ")
            except OSError:
                print("No save file found!")
                input("> ")

        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()  #autosave
        clear()

        if not standing:
            if biome[map[y][x]]["e"]:
                if random.randint(0, 100) <= 30:  # 30% chance of encounter
                    fight = True
                    battle()


        draw()
        print("LOCATION: " + biome [map[y][x]]["t"])
        draw()
        print("HP: " + str(HP) + "/" + str(HPMAX))
        print("ATK: " + str(ATK))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elx))
        print("GOLD: " + str(gold))
        print("COORDS:", x, y)
        draw()
        print("0: SAVE AND QUIT")
        if y > 0 and map[y-1][x] != "empty":
                print("1 - NORTH")
        if x < x_len and map[y][x+1] != "empty":
            print("2 - EAST")
        if y < y_len and map[y-1][x] != "empty":
            print("3 - SOUTH")
        if x > 0 and map[y][x-1] != "empty":
            print("4 - WEST")
        draw()

        dest = input("> ")
        if dest == "0":
            play = False
            menu = True
            save()
        elif dest == "1":
            if y > 0 and map[y-1][x] != "empty":
                y -= 1
                standing = False

        elif dest == "2":
            if x < x_len and map[y][x+1] != "empty":
                x += 1
                standing = False

        elif dest == "3":
            if y < y_len and map[y+1][x] != "empty":
                y += 1
                standing = False

        elif dest == "4":
            if x > 0 and map[y][x-1] != "empty":
                x -= 1
                standing = False
            
