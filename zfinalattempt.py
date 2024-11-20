# Dictionary containing questions with possible answers.
steps = {
    "Which way would you like to go? Type left or right: ": ["left", "right"],
    "You reach a river. Do you want to swim or wait? Type swim or wait: ": ["swim", "wait"],
    "While waiting, you spot three doors. Which door do you choose? Type red, blue, or yellow: ":
        ["red", "blue", "yellow"],
}

# Dictionary containing various outcomes based on the user's choices.
outcomes = {
    "left": "Oh no! You chose the wrong path and fell into a pit of quicksand. Game over!",
    "swim": "You are attacked by a fierce sea monster while swimming across the river. Game over!",
    "red": "Oops! As you step through the door, you trigger a trap and get caught. Game over!",
    "blue": "The blue door leads to a room filled with treasure, but it's protected by a fire-breathing dragon. "
            "You are toast. Game over!",
    "yellow": "Congratulations! You've chosen the door of wisdom and found the treasure! You win!",
}

def ask(ques, answers):
    """Function to ask the user a question and get their answer. Also loops back to current question if invalid
    answer received."""
    while True: #ensures that the program keeps asking the user the same question until a valid answer is provided
        user_answer = input(ques)
        if user_answer in answers:
            return user_answer
        else:
            print("That is not a valid answer.")

def game():
    """Function to play the adventure game based on user choices."""
    for question in steps:
        possible_answers = steps[question] #retrieves the values for each key in the "steps" dictionary. For each key, saves them in a variable called "possible answers"
        user_response = ask(question, possible_answers) #inputs each value key pair into the function called ask
        if user_response in outcomes:
            print(outcomes[user_response])
            break

game()
