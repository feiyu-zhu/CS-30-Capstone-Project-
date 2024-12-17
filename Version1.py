class Character:
    def __init__(self,name, player, position, inventory):
        self.name = name
        self.player = player
        self.position = position
        self.inventory = inventory
    
    def check_inventory(self):
        for items in self.inventory:
            print(f"-- {items} --")

            
player = Character("?", True, [0, 0], ["item1", "item2"])


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
    pass


def backward():
    pass


def right():
    pass


def left():
    pass


menu = {"game": {"move": move, "search": search, "check": check, "quit": quit_},
        "move": {"forward": forward, "backward": backward, "right": right, "left": left}}

def player_choice(type_):
    while True:
        for choice in menu[type_].keys():
            print(f"- {choice}")
        player_selection = input("My decision is ")
        if player_selection in menu[type_]:
            menu[type_][player_selection]()
        else:
            print("That is not a option")
            continue

player_choice("game")
            
        
        