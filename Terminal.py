

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
buy = False
speak = False
boss = False


HP = 100
HPMAX = HP
ATK = 1
pot = 1
elx = 1
gold = 0
x = 0
y = 6


def make_tile(name, enemy=True, open_dirs=None, rot=0):
    if open_dirs is None:
        open_dirs = ["north", "east", "south", "west"]

    return {
        "tile": name,
        "e": enemy,
        "open": open_dirs[:],
        "rot": rot
    }


def copy_tile(tile):
    return {
        "tile": tile["tile"],
        "e": tile["e"],
        "open": tile["open"][:],
        "rot": tile["rot"]
    }


# Tile patterns
PL = make_tile("plains", True)
FO = make_tile("forest", True)
FI = make_tile("fields", False)
TO = make_tile("town", False)
HI = make_tile("hills", True)
MO = make_tile("mountain", True)
CA = make_tile("cave", True)
SH = make_tile("shop", False)
MA = make_tile("mayor", False)
EM = make_tile("empty", False, [])

# Bridge-style tiles
BR_NS = make_tile("bridge", True, ["north", "south"])
BR_EW = make_tile("bridge", True, ["east", "west"])
BR_NE = make_tile("bridge", True, ["north", "east"])
BR_ES = make_tile("bridge", True, ["east", "south"])
BR_SW = make_tile("bridge", True, ["south", "west"])
BR_WN = make_tile("bridge", True, ["west", "north"])
BR_ALL = make_tile("bridge", True, ["north", "east", "south", "west"])


map = [
    [copy_tile(PL), copy_tile(PL), copy_tile(EM), copy_tile(PL), copy_tile(FO), copy_tile(MO), copy_tile(CA)],  # y = 0
    [copy_tile(FO), copy_tile(FO), copy_tile(FO), copy_tile(FO), copy_tile(FO), copy_tile(HI), copy_tile(MO)],  # y = 1
    [copy_tile(FO), copy_tile(FI), copy_tile(BR_NS), copy_tile(PL), copy_tile(HI), copy_tile(FO), copy_tile(HI)], # y = 2
    [copy_tile(PL), copy_tile(SH), copy_tile(TO), copy_tile(MA), copy_tile(PL), copy_tile(HI), copy_tile(MO)],  # y = 3
    [copy_tile(PL), copy_tile(FI), copy_tile(FI), copy_tile(PL), copy_tile(HI), copy_tile(MO), copy_tile(MO)],  # y = 4
    [copy_tile(PL), copy_tile(FI), copy_tile(FI), copy_tile(PL), copy_tile(HI), copy_tile(MO), copy_tile(MO)],  # y = 5
    [copy_tile(PL), copy_tile(FI), copy_tile(FI), copy_tile(PL), copy_tile(HI), copy_tile(MO), copy_tile(MO)]   # y = 6
]

y_len = len(map) - 1
x_len = len(map[0]) - 1


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
        "atk": random.randint(5,8),
        "g": 5
    },
    "Goblin": {
        "hp": 15,
        "atk": random.randint(2,5),
        "g": 3
    },
    "Zombie": {
        "hp": 30,
        "atk": random.randint(3,6),
        "g": 7
    },
    "Ghost": {
        "hp": 25,
        "atk": random.randint(5,8),
        "g": 10
    },
    "Mummy": {
        "hp": 35,
        "atk": random.randint(9,12),
        "g": 15
    }
}


current_tile = map[y][x]
print(current_tile["tile"])
name_of_tile = current_tile["tile"]
enemy_tile = current_tile["e"]

dmgnum1 = 0
dmgnum2 = 0
dmgnum3 = 0
dmgnum4 = 0
dmgnum5 = 0
dmgnum6 = 0
dmgnum7 = 0
dmgnum8 = 0
dmgnum9 = 0
dmgnum10 = 0



weapon = {
    "fist": {"damage": [dmgnum1 + 1, dmgnum2 + 1, dmgnum3 + 2, dmgnum4 + 2, dmgnum5 + 3, dmgnum6 + 3, dmgnum7 + 4, dmgnum8 + 4], "delay": 0.07},
    "sword": {"damage": [dmgnum1 + 1, dmgnum2 + 3, dmgnum3 + 3, dmgnum4 + 4, dmgnum5 + 5, dmgnum6 + 6, dmgnum7 + 6, dmgnum8 + 6, dmgnum9 + 6], "delay": 0.08},
    "axe": {"damage": [dmgnum1 + 1, dmgnum2 + 1, dmgnum3 + 1, dmgnum4 + 3, dmgnum5 + 6, dmgnum6 + 8, dmgnum7 + 8, dmgnum8 + 9, dmgnum9 + 10], "delay": 0.1},
    "dagger": {"damage": [dmgnum1 + 1, dmgnum2 + 1, dmgnum3 + 2, dmgnum4 + 8, dmgnum5 + 12], "delay": 0.05},
    "MASTERSWORD": {"damage": [dmgnum1 + 100, dmgnum2 + 100, dmgnum3 + 100, dmgnum4 + 100, dmgnum5 + 100], "delay": 0.1}
}

# Weapons

# Fists
fistdamage = weapon["fist"]["damage"]
fistdelay = weapon["fist"]["delay"]

# Sword
sworddamage = weapon["sword"]["damage"]
sworddelay = weapon["sword"]["delay"]

# Axe
axedamage = weapon["axe"]["damage"]
axedelay = weapon["axe"]["delay"]

# Dagger
daggerdamage = weapon["dagger"]["damage"]
daggerdelay = weapon["dagger"]["delay"]

# MASTERSWORD (DEV ONLY)
MASTERSWORDdamage = weapon["MASTERSWORD"]["damage"]
MASTERSWORDdelay = weapon["MASTERSWORD"]["delay"]



damage_list = MASTERSWORDdamage   # change to "sword" or "axe"
weapon_delay = MASTERSWORDdelay   # change to "sword" or "axe"
dmgindex = 0

move_delay = 0.12
last_move = 0








def clear():
    os.system('cls')

def draw():
    print("xX--------------------Xx")

def save():
    save_list = [
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

    for row in map:
        for tile in row:
            save_list.append(str(tile["rot"]))

    f = open("save.txt", "w")

    for item in save_list:
        f.write(item + "\n")

    f.close()

def heal(amount):
    global HP
    if HP + amount > HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(name + " healed " + str(amount) + " HP.")


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
    print("Press ENTER to attack.")
    print(dmgvalues)
    print(arrow_line)


def battle():

    global fight, play, run, HP, pot, elx, gold, dmgindex, last_move

    enemy = random.choice(e_list)
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["atk"]
    g = mobs[enemy]["g"]

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
            print("2: USE POTION (30 HP)")
        if elx > 0:
            print("3: USE ELIXIR (50 HP)")
        draw()

        choice = input("> ")

        if choice == "1":
            draw_screen(dmgindex)
            rolling = True
            move_delay = weapon_delay
            while rolling:
                now = time.time()

                if msvcrt.kbhit():
                    char = msvcrt.getch()
                    if char == b'\r':
                        clear()
                        print(name + " dealt " + str(damage_list[dmgindex]) + " + " + str(ATK) + " damage to " + enemy)
                        rolling = False
                        time.sleep(1)
                        hp -= damage_list[dmgindex] + ATK
                        if hp > 0:
                            HP -= atk
                            print(enemy + " dealt " + str(atk) + " damage to " + name)
                            input("> ")
                        

                if now - last_move >= move_delay:
                    dmgindex = (dmgindex + 1) % len(damage_list)
                    draw_screen(dmgindex)
                    last_move = now

                time.sleep(0.01)
        elif choice == "2":
                if pot > 0:
                    pot -= 1
                    heal(30)
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + name)
                else:
                    print("You have no potions left.")
                input("> ")
                    
        elif choice == "3":
                if elx > 0:
                    elx -= 1
                    heal(50)
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + name)
                else:
                    print("You have no elixirs left.")
                input("> ")

        if HP <= 0:
            clear()
            draw()
            print(enemy + " defeated " + name + ".")
            draw()
            fight = False
            play = False
            print("GAME OVER")
            quit()
        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            draw()
            fight = False
            gold += g
            print("You found " + str(gold) + " gold on the " + enemy + ".")
            if random.randint(0, 100) <= 10:  # 20% chance of potion drop
                pot += 1
                print("The " + enemy + " dropped a potion.")
            
            input("> ")
            clear()

def rotate_openings(openings, rot):
    dirs = ["north", "east", "south", "west"]
    new_openings = []

    for direction in openings:
        index = dirs.index(direction)
        new_index = (index + rot) % 4
        new_openings.append(dirs[new_index])

    return new_openings


def can_enter(tile, direction):
    if tile["tile"] == "empty":
        return False

    allowed = rotate_openings(tile["open"], tile.get("rot", 0))
    return direction in allowed


def can_leave(tile, direction):
    if tile["tile"] == "empty":
        return False

    allowed = rotate_openings(tile["open"], tile.get("rot", 0))
    return direction in allowed


def rotate_tile(x, y):
    tile = map[y][x]
    tile["rot"] = (tile["rot"] + 1) % 4









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
                f.close()

                needed_lines = 9 + (len(map) * len(map[0]))

                if len(load_list) == needed_lines:
                    name = load_list[0].strip()
                    HP = int(load_list[1].strip())
                    ATK = int(load_list[2].strip())
                    pot = int(load_list[3].strip())
                    elx = int(load_list[4].strip())
                    gold = int(load_list[5].strip())
                    x = int(load_list[6].strip())
                    y = int(load_list[7].strip())
                    key = load_list[8].strip() == "True"

                    rot_index = 9
                    for row in map:
                        for tile in row:
                            tile["rot"] = int(load_list[rot_index].strip())
                            rot_index += 1

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
            if map[y][x]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()

        if play:
            draw()
            print("LOCATION: " + map[y][x]["tile"])
            draw()
            print("HP: " + str(HP) + "/" + str(HPMAX))
            print("ATK: " + str(ATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elx))
            print("GOLD: " + str(gold))
            display_y = y_len - y
            print("GRID COORDS:", x, y)
            print("COORDS:", x, display_y)
            draw()
            print("0: SAVE AND QUIT")
            if y > 0 and can_leave(map[y][x], "north") and can_enter(map[y-1][x], "south"):
                print("1 - NORTH")
            if x < x_len and can_leave(map[y][x], "east") and can_enter(map[y][x+1], "west"):
                print("2 - EAST")
            if y < y_len and can_leave(map[y][x], "south") and can_enter(map[y+1][x], "north"):
                print("3 - SOUTH")
            if x > 0 and can_leave(map[y][x], "west") and can_enter(map[y][x-1], "east"):
                print("4 - WEST")
            if pot > 0:
                print("5 - USE POTION (30 HP)")
            if elx > 0:
                print("6 - USE ELIXIR (50 HP)")
            print("7 - ROTATE TILE")
            if map[y][x]["tile"] == "shop" or map[y][x]["tile"] == "mayor" or map[y][x]["tile"] == "cave":
                print("? - ENTER")
            dest = input("> ")
            if dest == "0":
                play = False
                menu = True
                save()

            elif dest == "1":
                if y > 0 and can_leave(map[y][x], "north") and can_enter(map[y-1][x], "south"):
                    y -= 1
                    standing = False

            elif dest == "2":
                if x < x_len and can_leave(map[y][x], "east") and can_enter(map[y][x+1], "west"):
                    x += 1
                    standing = False

            elif dest == "3":
                if y < y_len and can_leave(map[y][x], "south") and can_enter(map[y+1][x], "north"):
                    y += 1
                    standing = False

            elif dest == "4":
                if x > 0 and can_leave(map[y][x], "west") and can_enter(map[y][x-1], "east"):
                    x -= 1
                    standing = False

            elif dest == "5":
                if pot > 0:
                    pot -= 1
                    heal(30)
                else:
                    print("You have no potions left.")
                    input("> ")
                standing = True

            elif dest == "6":
                if elx > 0:
                    elx -= 1
                    heal(50)
                else:
                    print("You have no elixirs left.")
                    input("> ")
                standing = True

            elif dest == "7":
                rotate_tile(x, y)
                standing = True

            else:
                standing = True