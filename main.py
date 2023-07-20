game_on = True

def direction():
    direction_choice = input("Which way would you like to go? Type left or right: ").lower()
    if direction_choice == "right":
        game_over("Oh no! You chose the wrong path and fell into a pit of quicksand.")
        return False
    elif direction_choice == "left":
        return True
    else:
        not_valid_answer()
        direction()

def action():
    action_choice = input("You reach a river. Do you want to swim or wait? Type swim or wait: ").lower()
    if action_choice == "swim":
        game_over("You are attacked by a fierce sea monster while swimming across the river.")
        return False
    elif action_choice == "wait":
        return True
    else:
        not_valid_answer()
        action()

def choose_door():
    door_choice = input("While waiting, you spot three doors. Which door do you choose? Type red, blue,"
                        " or yellow: ").lower()
    if door_choice == "red":
        game_over("Oops! As you step through the door, you trigger a trap and get caught.")
        return False
    elif door_choice == "blue":
        game_over("The blue door leads to a room filled with treasure, but it's protected by a fire-breathing dragon."
                  " You are toast!")
        return False
    elif door_choice == "yellow":
        print("Congratulations! You've chosen the door of wisdom and found the treasure! You win!")
        return True
    else:
        not_valid_answer()
        choose_door()

def not_valid_answer():
    print("Argh! You're making me dizzy! Please choose a valid answer.")

def game_over(reason):
    print(f"{reason} Game over!")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

print("Welcome to Treasure Island ...")
print("Your mission is to find the treasure ...")

while game_on:
    if direction():
        if action():
            if choose_door():
                break
            break
        break
    else:
        break
