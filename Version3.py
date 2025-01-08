from tabulate import tabulate
import random
class Character:
    
    def __init__(self, name, player, position, inventory, map_, state, move_list):
        self.name = name
        self.player = player
        self.position = position
        self.inventory = inventory
        self.map_ = map_
        self.state = state
        self.move_list = move_list
    
    def check_inventory(self):
        print("-----Item Own-----")
        list_of_item = []
        for items in self.inventory:
            if items not in list_of_item:
                list_of_item.append(items)
                items.number += 1
            else:
                items.number += 1
        for items in list_of_item:
            print(f"-- {items.name.title()} × {items.number} --")
            items.number = 0
        
        print("----Move List----")
        for items in self.move_list:
            print(f"--{items.name.title()}--")

class State:
    def __init__(self, player, health, max_health, speed, damage):
        self.player = player
        self.health = health
        self.max_health = max_health
        self.speed = speed
        self.damage = damage
        
class Map_:
    
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.map_ = [[None for _ in range(self.size[1]+1)] for _ in range(self.size[0]+1)]
        
    def dect_border(self, coordinate):
        if coordinate[0] > self.size[0] or coordinate[1] > self.size[1]:
            return True
        elif coordinate[0] < 0 or coordinate[1] < 0:
            return True
        else:
            return False

class Items:
    
    def __init__(self, name, description, type_, value, time, rarity):
        self.name = name
        self.description = description
        self.type_ = type_
        self.value = value
        self.time = time
        self.rarity = rarity
        self.number = 0

class Moves:
    
    def __init__(self, name, description, type_, value, priority):
        self.name = name
        self.description = description
        self.type = type_
        self.value = value
        self.priority = priority

punch = Moves("punch", "Quickly punches enemy", "attack", 1, 2)
kick = Moves("kick", "Kick Strike", "attack", 2, 1)
guard = Moves("guard", "Use defense form, guard your self from the attack", "guard", 2, 3)
god_requiem = Moves("god requiem", "A cheat move for testing", "attack", 999, 4)
healing_pill = Items("healing pill", "A pill that heal you for a small amount", "health", 5,0,10 )
crazy_diamond = Items("crazy diamond", "A magical stone that restore all your state", "all", 999, 0, 1)
starting_map = Map_("starting map", [2,2])
player_state = State(True, 20, 20, 10, 5)
mob_state = State(False, 10, 10, 5, 1)
player = Character("Emyia", True, [2, 2], [healing_pill,healing_pill,crazy_diamond], starting_map, player_state, [punch, kick, guard, god_requiem])
servant = Character("Servant", False, [0,1], [], starting_map, mob_state, [punch, kick, guard])
list_ = [healing_pill, crazy_diamond]
def move():
    player_choice("move")


def search():
    item_list = []
    for item in list_:
        for i in range(item.rarity):
            item_list.append(item)
    varrible = random.randint(0,1)
    if varrible == 1:
        item = random.choice(item_list)
        player.inventory.append(item)
        print(f"You find a {item.name}")
        print(item.description)
    else:
        if player.position != [1,1]:
            print("You have encounter with an enemy")
            fight(servant)
        else:
            print("...")
            pass


def cpu(unit):
    return(random.choice(unit.move_list))


def player_choose_move():
    while True:
        for name in player.move_list:
            print(name.name.title())
            print(f"--- {name.description}")
        player_choose = input().lower()
        count = 0
        for choose in player.move_list:
            count = count + 1
            if choose.name == player_choose:
                return(choose)
            elif count == len(player.move_list):
                print("That is not a available choice")


def fight(unit):
    while True:
        if unit.state.health <= 0:
            print("Player Win")
            unit.state.health = unit.state.max_health
            break
        elif player.state.health <= 0:
            player.inventory = []
            player.position = [0,0]
            player.state.health = player.state.max_health
            print("Player Lost")
            break
        if player.state.health > 0 and unit.state.health > 0:
            player_move = player_choose_move()
            cpu_move = cpu(unit)
            if player_move.priority > cpu_move.priority:
                fight_calcu(player, player_move, unit, cpu_move)
            elif cpu_move.priority > player_move.priority:
                fight_calcu(unit, cpu_move, player, player_move)
            else:
                if player.state.speed >= unit.state.speed:
                    fight_calcu(player, player_move, unit, cpu_move)
                else:
                    fight_calcu(unit, cpu_move, player, player_move)
        else:
            continue


def fight_calcu(first, first_move, second, second_move):
    if first_move.type == "guard":
        print(f"{first.name.upper()} used {first_move.name.title()}")
        if second_move.value >= first_move.value:
            damage = second_move.value
            first.state.health -= damage
            print(f"{first.name.upper()} take {damage} damage")
            if second.state.health <= 0:
                print(f"{first.name.upper()} current health is 0")
            else:
                print(f"{first.name.upper()} current health is {first.state.health}")
        else:
            print(f"{first.name.upper()} guard the attact")
    elif first_move.type == "attack":
        damage = round(first_move.value * (first.state.damage/100 + 1))
        second.state.health -= damage
        print(f"{first.name.upper()} used {first_move.name.title()}")
        print(f"{second.name.upper()} take {damage} damage")
        if second.state.health <= 0:
            print(f"{second.name.upper()} current health is 0")
        else:
            print(f"{second.name.upper()} current health is {second.state.health}")
            if second_move.type == "guard":
                print(f"{second.name.upper()} is too slow on guard")
            elif second_move.type == "attack":
                damage = round(second_move.value * (second.state.damage/100 + 1))
                first.state.health -= damage
                print(f"{second.name.upper()} used {second_move.name.title()}")
                print(f"{first.name.upper()} take {damage} damage")
                if first.state.health <= 0:
                    print(f"{first.name.upper()} current health is 0")
                else:
                    print(f"{first.name.upper()} current health is {first.state.health}")
def check():
    player.check_inventory() 


def quit_():
    print("See You Next Game")
    quit()


def forward():
    player.position[1] -= 1
    if player.map_.dect_border(player.position):
        player.position[1] += 1
        print("You can't go there")
    else:
        print(player.position)
        print_player_position()


def backward():
    player.position[1] += 1
    if player.map_.dect_border(player.position):
        player.position[1] -= 1
        print("You can't go there")
    else:
        print(player.position)
        print_player_position()


def right():
    player.position[0] -= 1
    if player.map_.dect_border(player.position):
        player.position[0] += 1
        print("You can't go there")
    else:
        print(player.position)
        print_player_position()


def left():
    player.position[0] += 1
    if player.map_.dect_border(player.position):
        player.position[0] -= 1
        print("You can't go there")
    else:
        print(player.position)
        print_player_position()


def use_item(character):
    if character.player:
        list_of_item = []
        for items in character.inventory:
            if items not in list_of_item:
                list_of_item.append(items)
                items.number += 1
            else:
                items.number += 1
        for items in list_of_item:
            print(f"{items.name.title()} × {items.number}")
            items.number = 0
        while True:
            player_choice = input("I want to use: ")
            
    else:
        pass

    
menu = {"game": {"move": move, "search": search, "check": check, "quit": quit_},
        "move": {"forward": forward, "backward": backward, "right": right, "left": left}}


def print_player_position():
    copy_map = player.map_.map_
    copy_map[player.position[1]][player.position[0]] = "H"
    print(tabulate(player.map_.map_,tablefmt = 'grid'))
    copy_map[player.position[1]][player.position[0]] = None


def player_choice(type_):
    while True:
        for choice in menu[type_].keys():
            print(f"- {choice}")
        player_selection = input("My decision is ").lower()
        if player_selection in menu[type_]:
            menu[type_][player_selection]()
            if type_ != "game":
                continue
            break
        elif player_selection == "" and type_ != "game":
            break
        else:
            print("That is not a option")
            continue
use_item(player)
print("Hit enter to return")
while True:
    player_choice("game")
