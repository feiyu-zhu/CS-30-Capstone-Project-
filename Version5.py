###############################################################################
# Titles: CS-30-Capstone-Project(The Holy Grail War)
# class:CS 30
# Date: Jan 18 2025
# Coders Name:Johnson
# Version:5.0
###############################################################################
'''
A round base fighting game
'''
###############################################################################
# Import-----------------------------------------------------------------------
from tabulate import tabulate
import random
# Class------------------------------------------------------------------------
class Character: #class character
    
    def __init__(self, name, player, position, inventory, map_, state, \
                 weapon, move_list, boss):
        self.name = name # name of the character
        self.player = player # is the character control by player
        self.position = position # position of the character
        self.inventory = inventory # character inventory
        self.map_ = map_ # map the character
        self.state = state # the state of character
        self.weapon = weapon # weapon of the character
        self.move_list = move_list # move list of the character
        self.boss = boss # is the character boss
        self.story_line = [0,0] # current story line

    def check_inventory(self): # function check player's inventory (item own)
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

class State: # state class
    def __init__(self, player, health, max_health, speed, damage):
        self.player = player # is this the state of player
        self.health = health # health state of character
        self.max_health = max_health # max health state of character
        self.speed = speed # speed state of character
        self.damage = damage # damage state of character
        
class Map_: # map class
    
    def __init__(self, name, size, mob, boss, item_list):
        self.name = name
        self.size = size
        self.map_ = [[None for _ in range(self.size[1]+1)] for _
                     in range(self.size[0]+1)] # code genrate list of list
        self.mob = mob
        self.boss = boss
        self.item_list = item_list
    # function dect if position out of map or not  
    def dect_border(self, coordinate): 
        if coordinate[0] > self.size[0] or coordinate[1] > self.size[1]:
            return True
        elif coordinate[0] < 0 or coordinate[1] < 0:
            return True
        else:
            return False

class Items: # item class
    
    def __init__(self, name, description, type_, value, time, rarity):
        self.name = name
        self.description = description
        self.type = type_
        self.value = value # the value that item provide
        self.time = time # not use varrible
        self.rarity = rarity # the rarity of the item
        self.number = 0 # number item owned

class Moves:
    
    def __init__(self, name, description, type_, value, priority):
        self.name = name
        self.description = description
        self.type = type_
        self.value = value # damage of the move
        self.priority = priority # priority of the move

class Weapons:
    
    def __init__(self, name, description, type_, move_list):
        self.name = name
        self.description = description
        self.type = type_
        self.move_list = move_list #the move list of the weapon

# Global Varriables------------------------------------------------------------
# define move use class
slash = Moves("slash", "slash the enemy with sword", "attack", 5, 2)
heavy_chop = Moves("heavy chop", "use full power chop the enemy",
                   "attack", 10, 1)
ex_calibur = Moves("EX-Calibur!!!", "unleash the power of Excalibur",
                   "attack", 30, 3)
stab = Moves("stab", "stab the enemy with spear", "attack", 6, 2)
sweep = Moves("sweep", "sweep the spear horizontally", "attack", 15, 1)
item_use = Moves("item use", "use a item", "special", 0, 0)
punch = Moves("punch", "Quickly punches enemy", "attack", 1, 2)
kick = Moves("kick", "Kick Strike", "attack", 2, 1)
guard = Moves("guard", "Use defense form, guard your self from the attack",
              "guard", 2, 3)
god_requiem = Moves("god requiem", "A cheat move for testing",
                    "attack", 999, 4)
#define item use class
healing_pill = Items("healing pill",
                     "A pill that heal you for a small amount",
                     "health", 5,0,10 )
crazy_diamond = Items("crazy diamond",
                      "A magical stone that restore all your state",
                      "all", 999, 0, 1)
#define state use class
player_state = State(True, 20, 20, 10, 5)
mob_state = State(False, 10, 10, 5, 1)
spearer_state = State(False, 30, 30, 10, 10)
#define weapon use class
no_weapons = Weapons("Barehanded", "You hand", "hand",
                     [punch, kick, guard])
excalibur = Weapons("Ex-calibur", "The legendary sword of King Arthur",
                    "sword", [slash, heavy_chop])
gae_bulg = Weapons("Gáe Bulg", "The spear of Cu Chulainn in Irish mythology",
                   "spear", [stab, sweep])
# define character use class
servant = Character("Servant", False, [0,1], [], None, mob_state,
                    [no_weapons], [punch, kick, guard],False)
kenneth = Character("Kenneth", False, [1,1], [], None,
                    spearer_state, [no_weapons], [punch, kick, guard], True)
# define class use map
starting_map = Map_("starting map", [2,2],
                    servant, kenneth, [healing_pill, crazy_diamond])
# define player use class
player = Character("Emyia", True, [1, 1], [healing_pill], starting_map,
                   player_state, [no_weapons, excalibur],
                   [god_requiem, item_use], False)
# creat a npc use dictonary
joseph = {"name": "joseph", "encounter": False,
          "first_meet":("You have encounter with a 6" + 
"foot tall man with a regent hairtyle"), 
          "ask": "Need help for healing your state?",
          "introduce": "Hello! My name is Joseph",
          "heal": ("Joseph put hands on your shoulder, suddenly," + 
"all your wound get healed"),
          "wonder": ("It does not feels like sorcery," + 
"more like something that is close to magic"),
          "finish": "GREAT!! You can always find me when needed"
          }
# story line use for print
story_line = [[["How long is it since the last time I dreamed about" + 
"this; The scene of hell"],
               ["A young boy; Walking on the ruins of the city"],
               ["The smeel of blood, the scream that calls for help"],
               ["Is it because he is already numb to the things surround?..."],
               ["or he just try to ignore; Since he doesn't even have" + 
"enough power to save himself"],
               ["Then, following the fall of that last will of living," +
"the heart of the boy die with it"],
               ["After how long... The boy is rescued"],
               ["A man lifted up that lifeless body..."],
               ["The first thing that come into the boy's" + 
"eyes is the man's face"],
               ["that unforgettable happiness on the man's face," +
"he is so happy,it is like he is the one who got rescued"],
               ["Emiya; the boy was the only survivor from the" + 
"disaster caused by gas leak 10 years ago"],
               ["The Holy Grail War; the war that caused that disaster"],
               ["The war between seven people who got" + 
"chosen by the holy grail"],
               ["Seven Grand Order the one who got chosen will fight" + 
"for the grail that grants any wish"],
               ["The Grand Order will provide the power and" + 
"weapon of the Heroic Spirit"],
               ["Heroic Spirit; the spirit of heroes who achieved great deed" +
"in lifeand become objects of worship after their deaths"],
               ["Emiya has now been chosen as the GrandOrder," + 
"to stop that kind of disaster from happening again he decide" + 
"to fight for the grail"], 
               ["The game is not finished the boss is at the center of the map," + 
"use search to find item and enemy"]],
              [["..."],["..."]]
              ]


# functions-------------------------------------------------------------------
def story_telling(): # function print out story 
    if player.story_line == [0,0]:
        while player.story_line[1] < len(story_line[0]):
            print(*story_line[player.story_line[0]][player.story_line[1]])
            input("HIT Enter to continue")
            player.story_line[1] += 1
        else:
            player.story_line[0] += 1
            player.story_line[1] = 0


# function call move
def move():
    player_choice("move")


# function for search 50% get item else enemy
# if at potint 0,0 encounter with boss
def search():
    if player.position == [0,0]:
        if joseph["encounter"]:
            print(joseph["ask"])
            player_choice = input("Y/N").lower()
            if player_choice == "y":
                print(joseph["heal"])
                player.state.health = player.state.max_health
                print("Hit ENTER to continue")
                input(f"{player.name}: {joseph['wonder']}")
                print(joseph["finish"])
            else:
                print(joseph["finish"])
        else:
            print(joseph["first_meet"])
            input("Hit ENTER to continue")
            print(joseph["introduce"])
            input("Hit ENTER to continue")
            print(joseph["ask"])
            player_choice = input("Y/N").lower()
            if player_choice == "y":
                print(joseph["heal"])
                player.state.health = player.state.max_health
                print("Hit ENTER to continue")
                input(f"{player.name}: {joseph['wonder']}")
                print(joseph["finish"])
                joseph["encounter"] = True
            else:
                print(joseph["finish"])
                joseph["encounter"] = True
    else:
        if player.position == [1,1]:
            print(f"Encounter with boss {player.map_.boss.name}")
            player_choice = input("Continue Y/N").lower()
            if player_choice == "y":
                fight(player.map_.boss)
            else:
                print("You walk away")
        else:
            item_list = []
            for item in player.map_.item_list:
                for i in range(item.rarity):
                    item_list.append(item)
            varrible = random.randint(0,1)
            if varrible == 1:
                item = random.choice(item_list)
                player.inventory.append(item)
                print(f"You find a {item.name}")
                print(item.description)
            else:
                print(f"You have encounter with {player.map_.mob.name}")
                fight(player.map_.mob)


#random choose a move
def cpu(unit):
    return(random.choice(unit.move_list))


# let player choose move
def player_choose_move():
    while True:
        player.check_inventory()
        print("")
        for name in player.move_list:
            print(name.name.title())
            print(f"--- {name.description}")
        player_choose = input().lower()
        count = 0
        if player_choose == "item use" and len(player.inventory) != 0:
            choose_item(player)
        elif player_choose == "item use" and len(player.inventory) == 0:
            print("There are no item in your inventory")
            continue
        for choose in player.move_list:
            count = count + 1
            if choose.name == player_choose:
                return(choose)
            elif count == len(player.move_list):
                print("That is not a available choice")


# fight function
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


# fight calculate the dmage
def fight_calcu(first, first_move, second, second_move):
    if first_move.type == "guard":
        print(f"{first.name.upper()} used {first_move.name.title()}")
        if second_move.value >= first_move.value:
            damage = second_move.value
            first.state.health -= damage
            print(f"{second.name.upper()}'s attack is too strong")
            print(f"{first.name.upper()} take {damage} damage")
            if second.state.health <= 0:
                print(f"{first.name.upper()} current health is 0")
            else:
                print(f"{first.name.upper()}" + 
                f" current health is {first.state.health}")
        else:
            print(f"{first.name.upper()} guard {second_move.name.title()}")
    elif first_move.type == "attack":
        damage = round(first_move.value * (first.state.damage/10 + 1))
        second.state.health -= damage
        print(f"{first.name.upper()} used {first_move.name.title()}")
        print(f"{second.name.upper()} take {damage} damage")
        if second.state.health <= 0:
            print(f"{second.name.upper()} current health is 0")
        else:
            print(f"{second.name.upper()}" + 
            f"current health is {second.state.health}")
            if second_move.type == "guard":
                print(f"{second.name.upper()} is too slow on guard")
            elif second_move.type == "attack":
                damage = round(second_move.value *
                               (second.state.damage/10 + 1))
                first.state.health -= damage
                print(f"{second.name.upper()} used {second_move.name.title()}")
                print(f"{first.name.upper()} take {damage} damage")
                if first.state.health <= 0:
                    print(f"{first.name.upper()} current health is 0")
                else:
                    print(f"{first.name.upper()}" + 
                    f"current health is {first.state.health}")


# check the inventory
def check():
    player.check_inventory() 


# quit the game
def quit_():
    print("See You Next Game")
    quit()


# move forward
def forward():
    player.position[1] -= 1
    if player.map_.dect_border(player.position):
        player.position[1] += 1
        print("You can't go there")
    else:
        print(player.position)
        print_player_position()


# move backward
def backward():
    player.position[1] += 1
    if player.map_.dect_border(player.position):
        player.position[1] -= 1
        print("You can't go there")
    else:
        print(player.position)
        print_player_position()


# move right
def right():
    player.position[0] += 1
    if player.map_.dect_border(player.position):
        player.position[0] -= 1
        print("You can't go there")
    else:
        print(player.position)
        print_player_position()


# move left
def left():
    player.position[0] -= 1
    if player.map_.dect_border(player.position):
        player.position[0] += 1
        print("You can't go there")
    else:
        print(player.position)
        print_player_position()


# let character or player choose item
def choose_item(character):
    while True:
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
            if len(character.inventory) != 0:
                player_choice = input("I want to use: ").lower()
                if player_choice == "":
                    break
                count = 0
                choose = None
                for items in character.inventory:
                    count += 1
                    if player_choice == items.name:
                        choose = items
                if choose != None:
                    use_item(character, choose)
                    break
                else:
                    print("There are no item in your inventory")
                    break    
        else:
            try:
                cpu_choice = random.choice(character.inventory)
            except:
                break
            else:
                use_item(character, cpu_choice)
                break


# use the item base on varrible of item
def use_item(character,item):
    if item.type == "health":
        character.state.health += item.value
        print(f"{character.name.title()} use {item.name.upper()} recover {item.value} health point")
        if character.state.health > character.state.max_health:
            character.state.health = character.state.max_health
            print(f"Current health: {character.state.health}")
        else:
            print(f"Current health: {character.state.health}")
    elif item.type == "all":
        character.state.health += item.value
        print(f"{character.name.title()} use {item.name.upper()} recover {item.value} health point")
        if character.state.health > character.state.max_health:
            character.state.health = character.state.max_health
            print(f"Current health: {character.state.health}")
        else:
            print(f"Current health: {character.state.health}")
    character.inventory.remove(item)   


# menu dictonary
menu = {"game": {"move": move, "search": search, "check": check, "item": choose_item,
                 "quit": quit_},
        "move": {"forward": forward, "backward": backward, "right": right, "left": left}}


# add character move list from weapon move list
def append_move_from_weapon(character):
    for weapon in character.weapon:
        for move in weapon.move_list:
            if move not in character.move_list:
                character.move_list.append(move)


# use tabulate print where player is at on map
def print_player_position():
    copy_map = player.map_.map_
    copy_map[player.position[1]][player.position[0]] = "H"
    print(tabulate(player.map_.map_,tablefmt = 'grid'))
    copy_map[player.position[1]][player.position[0]] = None


# let player choose from choice
def player_choice(type_):
    while True:
        append_move_from_weapon(player)
        append_move_from_weapon(kenneth)
        append_move_from_weapon(servant)
        for choice in menu[type_].keys():
            print(f"- {choice}")
        if type_ == "move":
            print("Hit enter to return")
        player_selection = input("My decision is ").lower()
        if player_selection in menu[type_]:
            if player_selection == "item":
                if len(player.inventory) > 0:
                    print("Hit enter to return")
                    menu[type_][player_selection](player)
                else:
                    print("There are no item in your inventory")
            else:
                menu[type_][player_selection]()
            if type_ != "game":
                continue
            break
        elif player_selection == "" and type_ != "game":
            break
        else:
            print("That is not a option")
            continue

# main------------------------------------------------------------------------
story_telling()
while True:
    player_choice("game")
