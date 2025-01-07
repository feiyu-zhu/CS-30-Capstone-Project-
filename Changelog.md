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
