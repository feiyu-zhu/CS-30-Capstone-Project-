Version 1
  - Creat a map class contain varrible name and size, and use list to creat a 3x3 map
  - Creat caharacter class contain varrible name(name of character), player(is the character control by player), position(position on map), inventory(a list of item the character have), and map_(which map character at)
  - Basic function[move(use for let player choose where to move to), check inventory(print out item player own), and quit(quit the game)]
  - Use databases to create menu(a dictionary of dictionary call function based on player input

Version 2
  - import tabulate to creat map that show where player at on the map
  - creat class state and item
  - class state contain varrible(health and max_health)
  - class item contain varrible(name,description,type_, value, time, rarity)
  - add varrible (state) to player class
  - add new non player character mob_1
  - add Two item healing pill and crazy diamond
  - import random for search function
    - if the item find is a item not enemy(0 and 1 random)
    - From the item list base on rarity pick a item append to player inventory
  - when select choice if player input is empty return to the main menu

Version 3
  - creat move class and add varrible speed and attack in the state class
  - move class has varrible name, description, type, value, and piority
  - add move kick, punch, guard and the move use for testing God Requiem
  - if player use search function and the player is not at point [1,1] there is 50% of chance the player will get a item and 50% encounter with enemy.
  - after player encounter with enemy start fight function
  - player and ememy each make a move(cpu choose randomly)
  - compare the piroity between move and the speed state of player and emey to decide who go first
  - the fight only continue when both player and enenmy health is > than 0, if not into fight concluding
  - if player lost player will lost all the item and revive at potint [0,0]
  - add use item as a move so player able to use item during fight
  - add use item as a choice in main menu so player able to use item outdise of fight
  - recover player state by the value of the item, is over the max point player remove the extra part that is over.

Version 4
  - creat new character spearer name kenneth as boss of the starting map
  - use dictionery creat a npc Joseph at [0,0] heal he player when player use search functin at point [0,0]

Version 5
  - add story telling by use list
  - creat weapon class(name,description,type, move list)
  - now character move depend on weapon move list
