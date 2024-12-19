from tabulate import tabulate
class Character:
    
    def __init__(self, name, player, position, inventory, map_):
        self.name = name
        self.player = player
        self.position = position
        self.inventory = inventory
        self.map_ = map_
    
    def check_inventory(self):
        print("-----Item Own-----")
        for items in self.inventory:
            print(f"-- {items} --")

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

starting_map = Map_("starting map", [2,2])
player = Character("?", True, [2, 2], ["test 1", "test 2"], starting_map)


def move():
    player_choice("move")


def search():
    pass


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
        

def backward():
    player.position[1] += 1
    if player.map_.dect_border(player.position):
        player.position[1] -= 1
        print("You can't go there")
    else:
        print(player.position)


def right():
    player.position[0] -= 1
    if player.map_.dect_border(player.position):
        player.position[0] += 1
        print("You can't go there")
    else:
        print(player.position)


def left():
    player.position[0] += 1
    if player.map_.dect_border(player.position):
        player.position[0] -= 1
        print("You can't go there")
    else:
        print(player.position)


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
        player_selection = input("My decision is ")
        if player_selection in menu[type_]:
            menu[type_][player_selection]()
            print_player_position()
            if type_ != "game":
                continue 
            break
        elif player_selection == "" and type_ != "game":
            break
        else:
            print("That is not a option")
            continue


#print(tabulate(player.map_.map_,tablefmt = 'grid'))
while True:
    print_player_position()
    player_choice("game")

