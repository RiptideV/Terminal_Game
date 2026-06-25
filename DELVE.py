

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
BASESAVELINES = 11  

inventory = {
    "weapons": ["fist"],
    "consumables": {
        "potion": pot,
        "elixir": elx
    }
}

weapons_text = ",".join(inventory["weapons"])

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

EM = make_tile("empty", False, [])
CRSW = make_tile("Chest Room: Sword", False, ["north", "east", "south", "west"])
CRDG = make_tile("Chest Room: Dagger", False, ["north", "east", "south", "west"])
CRAX = make_tile("Chest Room: Axe", False, ["north", "east", "south", "west"])
CREM = make_tile("Chest Room: Empty", False, ["north", "east", "south", "west"])
ST = make_tile("Starting Room", False, ["north", "east", "south", "west"])
END = make_tile("Dragon's Lair", False, ["north", "east", "south", "west"])

# Bridge-style tiles
BR_NS = make_tile("Hallway", True, ["north", "south"])
BR_EW = make_tile("Hallway", True, ["east", "west"])
BR_NE = make_tile("Corner", True, ["north", "east"])
BR_ES = make_tile("Corner", True, ["east", "south"])
BR_SW = make_tile("Corner", True, ["south", "west"])
BR_WN = make_tile("Corner", True, ["west", "north"])
BR_WNS = make_tile("Corner", True, ["west", "north", "south"])
BR_ALL = make_tile("Crossroads", True, ["north", "east", "south", "west"])
BR_NES = make_tile("T-Junction", True, ["north", "east", "south"])




map = [
    [copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(END)],   # y = 0
    [copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(BR_NS)], # y = 1
    [copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(CRAX)], # y = 2
    [copy_tile(EM),    copy_tile(EM),    copy_tile(CRSW),    copy_tile(BR_ES), copy_tile(BR_EW), copy_tile(BR_EW), copy_tile(BR_WN)], # y = 3
    [copy_tile(EM),    copy_tile(EM),    copy_tile(BR_NES), copy_tile(BR_WNS), copy_tile(EM),    copy_tile(EM),    copy_tile(EM)],    # y = 4
    [copy_tile(EM),    copy_tile(BR_ES), copy_tile(BR_WN), copy_tile(CRDG),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM)],    # y = 5
    [copy_tile(ST),    copy_tile(BR_WN), copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM),    copy_tile(EM)]     # y = 6
]

y_len = len(map) - 1
x_len = len(map[0]) - 1




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
    },
    "Dragon": {
        "hp": 100,
        "atk": random.randint(10,15),
        "g": 100
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



weapon_data = {
    "fist": {"damage": [dmgnum1 + 1, dmgnum2 + 1, dmgnum3 + 2, dmgnum4 + 2, dmgnum5 + 3, dmgnum6 + 3, dmgnum7 + 4, dmgnum8 + 4], "delay": 0.07},
    "sword": {"damage": [dmgnum1 + 1, dmgnum2 + 3, dmgnum3 + 3, dmgnum4 + 4, dmgnum5 + 5, dmgnum6 + 6, dmgnum7 + 6, dmgnum8 + 6, dmgnum9 + 6], "delay": 0.08},
    "axe": {"damage": [dmgnum1 + 1, dmgnum2 + 1, dmgnum3 + 1, dmgnum4 + 3, dmgnum5 + 6, dmgnum6 + 8, dmgnum7 + 8, dmgnum8 + 9, dmgnum9 + 10], "delay": 0.1},
    "dagger": {"damage": [dmgnum1 + 1, dmgnum2 + 1, dmgnum3 + 2, dmgnum4 + 8, dmgnum5 + 12], "delay": 0.05},
    "MASTERSWORD": {"damage": [dmgnum1 + 100, dmgnum2 + 100, dmgnum3 + 100, dmgnum4 + 100, dmgnum5 + 100], "delay": 0.1}
}


equipped_weapon = "fist"  # Default weapon
# Weapons





current_weapon = weapon_data[equipped_weapon]

damage_list = current_weapon["damage"]
weapon_delay = current_weapon["delay"]
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
        str(key),
        equipped_weapon,
        ",".join(inventory["weapons"])
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

    global fight, play, run, HP, pot, elx, gold, dmgindex, last_move, boss, current_weapon, damage_list, weapon_delay, boss

    current_weapon = weapon_data[equipped_weapon]
    damage_list = current_weapon["damage"]
    weapon_delay = current_weapon["delay"]
    dmgindex = 0
    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
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
            if random.randint(0, 100) <= 30:  # 30% chance of potion drop
                pot += 1
                print("The " + enemy + " dropped a potion.")
            if random.randint(0, 100) <= 10:  # 10% chance of elixir drop
                elx += 1
                print("The " + enemy + " dropped an elixir.")
            if enemy == "Dragon":
                draw()
                print("""
                After all this time you have finally defeated the dragon.
                You have avenged your village and spared many others the same fate as yours.
                Now you can finally rest, knowing that the dragon will never harm anyone again.
                """)
                print("""
                       .-.
                       |/|
                       |/|
                       |/|
                       |/|
                    ___|_|___
                    )  ___  (
                   /__/ | \__\
                      ) | (
                      ) | (
                      ) | (
                      ) | (
                      | | |
                      | | |
                      | | |
                      | | |
                      | | |
                      | | |
                ______| | |______

                """)
                draw()
                print("Thanks for playing my first game!: RiptideV (Pufferfish)")
                draw()
                boss = False
                play = False
                run = False
            
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

def weapon_equip(weapon_name):
    global equipped_weapon, current_weapon, damage_list, weapon_delay, dmgindex

    if weapon_name in inventory["weapons"]:
        equipped_weapon = weapon_name
        current_weapon = weapon_data[weapon_name]
        damage_list = current_weapon["damage"]
        weapon_delay = current_weapon["delay"]
        dmgindex = 0
        print(f"{name} equipped {weapon_name}.")
    else:
        print(f"You do not have a {weapon_name}.")


def boss_fight():
    global boss, fight

    while boss:
        clear()
        draw()
        print("""
        Here lies the dragon. After all this time and all this pain you have finally found it.
        It's massive form towers over you, its scales glinting in the dim light of the cavern.
        The dragon lets out a deafening roar, shaking the very walls of the labyrinth.
        This is it. The final battle. 
        """)
        draw()
        fight = True
        battle()



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
        print("3: READ THIS BEFORE PLAYING")
        print("4: QUIT GAME")
        draw()

        if rules:
            print("Have pen and paper ready. Your journey will be easier if you draw a map of the labyrinth as you explore it.")
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
            clear()
            draw()
            print("""
            4 years ago, your village was attacked by a fearsome dragon. You were the only survivor.
            After years of training and tracking down dead ends you have finally located the dragon's lair.
            The dragon resides deep inside the ruins of the Twisting Labyrinth, a maze of tunnles and catacombs that have been there for centuries.
            Preparing yourself, you enter the Twisting Labyrinth, ready to finally get your revenge.
            """)
            draw()
            print("""
            As you step into the labyrinth, you see a pedestal holding an amulet, it has twisting marks engraved all over it.
            You take it and put it around your neck, and you feel a sleep come over you.
            You wake up in a empty cobblestone room, with a single door.
            You have no weapons, and only 1 potion and 1 elixir.
            Navigate the labrinth. Find the dragon. Kill it. 
            """)
            draw()
            menu = False
            play = True
            

        elif choice == "2":
            try:
                f = open("save.txt", "r")
                load_list = f.readlines()
                f.close()

                needed_lines = BASESAVELINES + (len(map) * len(map[0]))

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
                    equipped_weapon = load_list[9].strip()
                    weapons_text = load_list[10].strip()
                    inventory["weapons"] = [w for w in weapons_text.split(",") if w]

                    rot_index = BASESAVELINES
                    current_weapon = weapon_data[equipped_weapon]
                    damage_list = current_weapon["damage"]
                    weapon_delay = current_weapon["delay"]
                    dmgindex = 0
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
            print("EQUIPPED WEAPON: " + equipped_weapon)
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
                print("5: USE POTION (30 HP)")
            if elx > 0:
                print("6: USE ELIXIR (50 HP)")
            print("7: USE AMULET (ROTATE TILE)")
            if map[y][x]["tile"] == "shop" or map[y][x]["tile"] == "mayor" or map[y][x]["tile"] == "END":
                print("?: ENTER")
            if map[y][x]["tile"] == "Chest Room: Sword" or map[y][x]["tile"] == "Chest Room: Dagger" or map[y][x]["tile"] == "Chest Room: Axe":
                print("!: OPEN CHEST")
            print("8: INVENTORY")
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

            elif dest == "8":
                clear()
                print("INVENTORY:")
                print("WEAPONS: " + ", ".join(inventory["weapons"]))
                print("EQUIPPED WEAPON: " + equipped_weapon)
                print("CONSUMABLES:")
                print("POTIONS: " + str(pot))
                print("ELIXIRS: " + str(elx))
                print("1 - EQUIP WEAPON")
                possibleequip = input("> ")
                if possibleequip == "1":
                    print("Which weapon would you like to equip?")
                    for i, weapon in enumerate(inventory["weapons"]):
                        print(f"{i+1} - {weapon}")
                    weapon_choice = input("> ")
                    if weapon_choice.isdigit() and 1 <= int(weapon_choice) <= len(inventory["weapons"]):
                        equipped_weapon = inventory["weapons"][int(weapon_choice) - 1]
                        weapon_equip(equipped_weapon)
                        print(f"You have equipped the {equipped_weapon}.")
                    else:
                        print("Invalid choice.")
            elif dest == "?":
                if map[y][x]["tile"] == "Dragon's Lair":
                    boss = True
                    fight = True
                    battle()
            elif dest == "!":
                if map[y][x]["tile"] == "Chest Room: Sword":
                    print("You found a sword in the chest!")
                    inventory["weapons"].append("sword")
                    map[y][x] = copy_tile(CREM)
                elif map[y][x]["tile"] == "Chest Room: Dagger":
                    print("You found a dagger in the chest!")
                    inventory["weapons"].append("dagger")
                    map[y][x] = copy_tile(CREM)
                elif map[y][x]["tile"] == "Chest Room: Axe":
                    print("You found an axe in the chest!")
                    inventory["weapons"].append("axe")
                    map[y][x] = copy_tile(CREM)
                else:
                    print("There is no chest here.")
                input("> ")

            else:
                standing = True