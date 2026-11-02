import random


attempts = 7


def display_rules():
    print("Welcome to the Number guessing game!")
    print("I have selected a number between 1 and 100")
    print("You have 7 attempts to guess it.")


def select_number(number, attempt=1):
    if attempt > attempts:
        print("Game Over!")
        print("The correct number was:", number)
        return

    guess = input(f"Attempt {attempt}/7 - Enter your guess:")

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number")
        return select_number(number, attempt)

    if guess < 1 or guess > 100:
        print("Please select a number between 1 and 100")
        return select_number(number, attempt)

    # check_guess = lambda x, y: "Correct" if x == y else (
    #     "Too low" if x < y else "Too high"
    # )

# Has the same function as commented code above
def check_guess(x, y):
    if x == y:
        return "Correct"
    elif x < y:
        return "Too low"
    else:
        return "Too high"


    result = check_guess(guess, number)

    if result == "Correct":
        print("Congratulations! You guessed the number!")
        print("You guessed it in", attempt, "attempt(s).")
        return

    if result == "Too low":
        print("Too low! Try a higher number")
    else:
        print("Too high! Try a higher number")

    select_number(number, attempt + 1)

display_rules()
random_number = random.randint(1, 100)
select_number(random_number)
