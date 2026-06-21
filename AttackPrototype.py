import msvcrt
import time
import os

fight = True

def clear():
    os.system('cls')

weapon = {
    "sword": {"damage": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    "axe": {"damage": [2, 3, 4, 5, 6, 9, 8, 9, 10]},
}

damage_list = weapon["axe"]["damage"]   # change to "sword" or "axe"
dmgindex = 0

move_delay = 0.12
last_move = 0

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

draw_screen(dmgindex)

while fight:
    now = time.time()

    if msvcrt.kbhit():
        char = msvcrt.getch()
        if char == b'\r':
            clear()
            print("Damage:", damage_list[dmgindex])
            break

    if now - last_move >= move_delay:
        dmgindex = (dmgindex + 1) % len(damage_list)
        draw_screen(dmgindex)
        last_move = now

    time.sleep(0.01)
