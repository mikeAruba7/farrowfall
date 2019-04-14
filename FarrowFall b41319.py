import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

# last edited 4.14.19 by Shane


# Functions
# ---------------------------------------
# These functions deal with text speed. Text will appear with 0.03 
# or 0.05 seconds between each character. Needs for loop (see example)

def quick_dialogue():
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)

def slow_dialogue():
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

#Example:
# question1 = '"What is your name?"\n'
# for character in question1:
#        slow_dialogue()

# ========================================

### Tips I haven't turned into functions yet ###

# If x is a string, the following will print the first
# letter capitalized and the remaining letters lower-case,
# provided the string is 21 characters or less.
# Good for proper nouns inputted by player.
# x[0].upper() + x[1:20].lower() 




# Player Setup
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.gold = 0
        self.status_effect = []
        self.location = 'start'
        self.game_over = False

myPlayer = player()

# Title Screen
def title_screen_selections():
    option = input('> ')
    if option.lower() == ('play'):
        start_game()
    elif option.lower() == ('help'):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print('Please enter a valid command.')
        option = input('> ')
        if option.lower() == ('play'):
            start_game()
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()

def title_screen():
    os.system('clear')
    print('#############################')
    print('#    F*A*R*R*O*W*F*A*L*L    #')
    print('#############################')
    print('          - Play -           ')
    print('          - Help -           ')
    print('          - Quit -           ')
    title_screen_selections()

def help_menu():
    print('     - Use up, down, left, right to move -     ')
    print('   - To progress, type commands seen in () -   ')
    print('- However, many secret commands exist as well -')
    title_screen_selections()

title_screen() # This calls the title_screen function

#Map
# ---------------------------
# A |  1  |  2  |  3  |  4  |
# B |  1  |  2  |  3  |  4  |
# C |  1  |  2  |  3  |  4  |
# D |  1  |  2  |  3  |  4  |
# ---------------------------

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
Up = 'up', 'north'
Down = 'down', 'south'
Left = 'left', 'west'
Right = 'right', 'east'

solved_places = {'a1' : False, 'a2' : False, 'a3' : False, 'a4' : False,
                'b1' : False, 'b2' : False, 'b3' : False, 'b4' : False,
                'c1' : False, 'c2' : False, 'c3' : False, 'c4' : False,
                'd1' : False, 'd2' : False, 'd3' : False, 'd4' : False,
                }
zonemap = {
    'a1' : {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: '',
        Down: 'b1',
        Left: '',
        Right: 'a2',
    },
    'a2' : {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: '',
        Down: 'b2',
        Left: 'a1',
        Right: 'a3',
    },
    'a3' : {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: '',
        Down: 'b3',
        Left: 'a2',
        Right: 'a4',
    },
    'a4' : {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: '',
        Down: 'b4',
        Left: 'a3',
        Right: '',
    },
    'b1' : {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        Up: 'a1',
        Down: 'c1',
        Left: '',
        Right: 'b2',
    },
    'b2' : {
        ZONENAME: 'Home'
        DESCRIPTION = 'This is your home.'
        EXAMINATION = 'Nothing appears out of place.'
        SOLVED = False
        Up = 'a2'
        Down = 'c2'
        Left = 'b1'
        Right = 'b3'
    },
    'b3' : {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        Up = 'up', 'north'
        Down = 'down', 'south'
        Left = 'left', 'west'
        Right = 'right', 'east'
    },
    'b4' : {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        Up = 'up', 'north'
        Down = 'down', 'south'
        Left = 'left', 'west'
        Right = 'right', 'east'
    },
    'c1' : {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        Up = 'up', 'north'
        Down = 'down', 'south'
        Left = 'left', 'west'
        Right = 'right', 'east'
    },
    'c2' : {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        Up = 'up', 'north'
        Down = 'down', 'south'
        Left = 'left', 'west'
        Right = 'right', 'east'
    },
    'c3' : {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        Up = 'up', 'north'
        Down = 'down', 'south'
        Left = 'left', 'west'
        Right = 'right', 'east'
    },
    'c4' : {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        Up = 'up', 'north'
        Down = 'down', 'south'
        Left = 'left', 'west'
        Right = 'right', 'east'
    },
    'd1' : {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        Up = 'up', 'north'
        Down = 'down', 'south'
        Left = 'left', 'west'
        Right = 'right', 'east'
    },
    'd2' : {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        Up = 'up', 'north'
        Down = 'down', 'south'
        Left = 'left', 'west'
        Right = 'right', 'east'
    },
    'd3' : {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        Up = 'up', 'north'
        Down = 'down', 'south'
        Left = 'left', 'west'
        Right = 'right', 'east'
    },
    'd4' : {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        Up = 'up', 'north'
        Down = 'down', 'south'
        Left = 'left', 'west'
        Right = 'right', 'east'
    },
    'd5' : {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        Up = 'up', 'north'
        Down = 'down',
    }
}
    
# Game interactivity
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('#' + myPlayer.location.upper() + '#')
    print('#' + zonemap[myPlayer.location][DESCRIPTION] +'#')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print('\n' + "=================================")
    print('"What would you like to do?"')
    action = input('> ')
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'examine',
                        'roll perception', 'tavern', 'npc','stats',
                        'fight', 'character' 'inventory', 'interact', 
                        'look', 'quit']
    while action.lower() not in acceptable_actions
        print('Unknown action, try again.\n')
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']
        player_move(action.lower)
    elif action.lower() in ['examine', 'look', 'interact', 'inspect',
                            'roll perception']
        player.examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest == in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest == in ['down', 'south']
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest == in ['left', 'west']
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest == in ['right', 'east']
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED] == True:
        print("There is nothing left to examine.")
    else:
        print("Placeholder.")

def movement_handler(destination):
    print('\n' + "You have moved to the " + destination + '.')
    myPlayer.destination = destination
    print_location()

# Game functionality
def start_game():
    return

def main_game_loop():
    while myPlayer.game_over == False:
    prompt()
    # This prompts the player until they win. Essential to keep active.


def setup_game()
    os.system('clear')

    Confirm = False
    while Confirm = False
    question1 = '"What is your name?"\n'
    for character in question1:
        slow_dialogue()
    player_name = input('> ')
    myPlayer.name = player_name

    question2 = '"What kind of adventurer are you?"\n'
    question2added = 'Barbarian, Bard, Cleric, Druid\n'
                + 'Fighter, Monk, Paladin, Ranger\n'
                + 'Rogue, Sorcerer, Warlock, Wizard\n'
    for character in question2:
        slow_dialogue()
    for character in question2added:
        quick_dialogue()
    player_job = input('> ')
    valid_jobs = ['barbarian', 'bard', 'cleric', 'druid', 'fighter',
                'monk', 'paladin', 'ranger', 'rogue', 'sorcerer',
                'warlock', 'wizard']
    if player_job.lower() in valid_jobs:
      myPlayer.job = player_job
    while player_job.lower not in valid_jobs:
            player_job = input('> ')
            if player_job.lower() in valid_jobs:
                myPlayer.job = player_job
                print('"Greetings, ' + player_job[0].upper() 
                + player_job[1:20].lower() + '."\n')

# Job-based stat assignment, no racials yet. Ripped directly from DND:
    if myPlayer.job.lower() is in ['barbarian']
        self.hp = 12
        self.gold = 5
    elif myPlayer.job.lower() is in ['fighter', 'paladin', 'ranger']
        self.hp = 10
        self.gold = 15
    elif myPlayer.job.lower() is in ['bard', 'cleric', 'druid',
                                    'monk', 'rogue', 'warlock']
        self.hp = 8
        self.gold = 10
    elif myPlayer.job.lower() is in ['sorcerer']
        self.hp = 6
        self.gold = 20

# Introduction
    question3 = '"Welcome, ' + player_name + ' ' 
    + player_job[0].upper() + player_job[1:20].lower() + '.'

    os.system('clear')
    print('####################################')
    print('#   "And now your story begins."   #')
    print('####################################')
    main_game_loop()


title_screen()

