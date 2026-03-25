# 📘 Assignment: Games in Python

## 🎯 Objective

Students will build a classic Hangman word-guessing game using Python, practicing string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️	Set Up the Game State

#### Description
Initialize the game by randomly selecting a secret word and setting up the variables needed to track the player's progress and remaining attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list using the `random` module
- Initialize a set or list to track guessed letters
- Set a maximum number of incorrect guesses (e.g., 6)
- Track the number of incorrect guesses made so far


### 🛠️	Implement the Game Loop

#### Description
Create the main game loop that accepts player input, validates guesses, updates game state, and ends when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Display the current word progress using underscores (e.g., `_ _ t h o n`)
- Prompt the player to guess a letter and handle invalid input
- Update progress when a correct letter is guessed
- Increment incorrect guess count for wrong guesses
- End the loop when the word is fully guessed or attempts are exhausted
- Display a win or lose message with the secret word revealed
