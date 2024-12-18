class Character:
    
    def __init__(self, name, player, position, inventory, map_):
        self.name = name
        self.player = player
        self.position = position
        self.inventory = inventory
        self.map_ = map_
    
    def check_inventory(self):
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
player = Character("?", True, [0, 0], ["test 1", "test 2"], starting_map)


def move():
    player_choice("move")


def search():
    player.check_inventory()


def check():
    pass


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

def player_choice(type_):
    while True:
        for choice in menu[type_].keys():
            print(f"- {choice}")
        player_selection = input("My decision is ")
        if player_selection in menu[type_]:
            menu[type_][player_selection]()
            break
        else:
            print("That is not a option")
            continue

while True:
    player_choice("game")
