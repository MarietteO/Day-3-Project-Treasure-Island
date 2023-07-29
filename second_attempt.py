# List of questions to be asked during the game.
questions_list = ["Which way would you like to go? Type left or right: ",
                  "You reach a river. Do you want to swim or wait? Type swim or wait: ",
                  "While waiting, you spot three doors. Which door do you choose? Type red, blue, or yellow: "]

# List of possible answers for each question in 'questions_list'.
answers_list = [["right", "left"], ["swim", "wait"], ["red", "blue", "yellow"]]

# Dictionary containing various game outcomes based on the user's choices.
outcomes_dict = {
    0: "Oh no! You chose the wrong path and fell into a pit of quicksand. Game over!",
    1: "You are attacked by a fierce sea monster while swimming across the river. Game over!",
    2: "Oops! As you step through the door, you trigger a trap and get caught. Game over!",
    3: "The blue door leads to a room filled with treasure, but it's protected by a fire-breathing dragon."
       "You are toast. Game over!",
    4: "Congratulations! You've chosen the door of wisdom and found the treasure! You win!",
}


def ask(answer, answers):
    """Function to ask the user a question and get their answer."""
    while True:
        user_answer = input(answer)
        if user_answer in answers:
            return user_answer
        else:
            print("That is not a valid answer.")

# Start the game by asking the first question.
first_answer = questions_list[0]
first_options = answers_list[0]
step_one = ask(first_answer, first_options)
# Check the user's answer for the first question.
if step_one == "left":
    print(outcomes_dict[0])
elif step_one == "right":
    second_answer = questions_list[1]
    second_options = answers_list[1]
    step_two = ask(second_answer, second_options)
# Check the user's answer for the second question.
    if step_two == "swim":
        print(outcomes_dict[1])
    elif step_two == "wait":
        third_answer = questions_list[2]
        third_options = answers_list[2]
        step_three = ask(third_answer, third_options)
        # Check the user's answer for the third question.
        if step_three == "red":
            print(outcomes_dict[2])
        elif step_three == "blue":
            print(outcomes_dict[3])
        elif step_three == "yellow":
            print(outcomes_dict[4])
