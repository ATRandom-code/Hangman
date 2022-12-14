import random

# The list of words to choose from.
words = ["apple", "banana", "orange", "grape", "strawberry"]

# Generate a random word from the list.
secret_word = random.choice(words)

# Set the number of tries the player has.
tries = 5

# Start the game.
while tries > 0:
    # Get the player's guess.
    guess = input("Enter your guess: ")

    # If the guess is correct, the player wins.
    if guess == secret_word:
        print("You win!")
        break

    # If the guess is incorrect, subtract one from the number of tries.
    else:
        tries -= 1
        print("Incorrect. You have %d tries left." % tries)

# If the player runs out of tries, the player loses.
if tries == 0:
    print("You lose!")
