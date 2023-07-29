# Dictionary containing questions with possible answers.
steps = {
    "Which way would you like to go? Type left or right: ": ["left", "right"],
    "You reach a river. Do you want to swim or wait? Type swim or wait: ": ["swim", "wait"],
    "While waiting, you spot three doors. Which door do you choose? Type red, blue, or yellow: ":
    ["red", "blue", "yellow"],
}

# Dictionary containing various outcomes based on the user's choices.
outcomes_dict = {
    0: "Oh no! You chose the wrong path and fell into a pit of quicksand. Game over!",
    1: "You are attacked by a fierce sea monster while swimming across the river. Game over!",
    2: "Oops! As you step through the door, you trigger a trap and get caught. Game over!",
    3: "The blue door leads to a room filled with treasure, but it's protected by a fire-breathing dragon."
       "You are toast. Game over!",
    4: "Congratulations! You've chosen the door of wisdom and found the treasure! You win!",
}


def ask(answer, answers):
    """Function to ask the user a question and get their answer. Also loops back to current question if invalid
    answer received."""
    while True:
        user_answer = input(answer)
        if user_answer in answers:
            return user_answer
        else:
            print("That is not a valid answer.")


def game():
    """Function to play the adventure game based on user choices."""
    outcomes_num = 0
    for question in steps:
        possible_answers = steps[question]
        user_response = ask(question, possible_answers)
        if user_response == possible_answers[0]:
            print(outcomes_dict[outcomes_num])
            outcomes_num += 1
            break
        elif question == "While waiting, you spot three doors. Which door do you choose? Type red, blue, or yellow: ":
            if user_response == "blue":
                print(outcomes_dict[3])
                break
            elif user_response == "yellow":
                print(outcomes_dict[4])
                break


game()
