from tabulate import tabulate
import random
class Character:
    
    def __init__(self, name, player, position, inventory, map_, state):
        self.name = name
        self.player = player
        self.position = position
        self.inventory = inventory
        self.map_ = map_
        self.state = state
    
    def check_inventory(self):
        print("-----Item Own-----")
        for items in self.inventory:
            print(f"-- {items.name.title()} --")

class State:
    def __init__(self, player, health, max_health):
        self.player = player
        self.health = health
        self.health = max_health
        
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

healing_pill = Items("healing pill", "A pill that make you health +5", "health", 5,0,10 )
crazy_diamond = Items("crazy diamond", "A magical stone that restore all your state", "all", 999, 0, 1)
starting_map = Map_("starting map", [2,2])
player_state = State(True, 20, 20)
mob_state = State(False, 10, 10)
player = Character("?", True, [2, 2], [], starting_map, player_state)
mob_1 = Character("Servant", False, [0,1], [], starting_map, mob_state)
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
        print("You have encounter with a enemy")
    


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


#print(tabulate(player.map_.map_,tablefmt = 'grid'))
print_player_position()
while True:
    player_choice("game")
