# The function takes in the secret word and the letters
# that the player has guessed so far as inputs
# and returns the current state of the game as a string
def hangman(secret_word: str, letters_guessed: List[str]):
  # Create a string that will be used to store the current state of the game
  current_state = ""
  
  # Loop over each character in the secret word
  for char in secret_word:
    # If the character is in the list of letters guessed,
    # add it to the current state string
    if char in letters_guessed:
      current_state += char
    # Otherwise, add an underscore to the string to
    # represent a letter that has not been guessed yet
    else:
      current_state += "_"
  
  # Return the current state of the game
  return current_state

# Run the function with a secret word and a list of letters guessed
# as inputs to see the current state of the game
print(hangman("python", ["p", "t", "h"]))
