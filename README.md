Hangman Game Script
This Python script is an interactive Hangman game where players try to guess a hidden word by inputting letters. Players have a limited number of lives, and incorrect guesses reduce the number of lives remaining. The game tracks wins and losses across multiple rounds, and the player can choose to play again after each game.

Key Components
words List: This list (imported from another file) contains the words used in the game. The script selects a random word from this list as the hidden word for each game.

Global Win and Loss Counters: The variables win and lose track the total number of games won and lost across multiple rounds.

Functions:

get_valid_word(words): This function randomly selects a valid word from the words list. It keeps choosing until it finds a word without spaces or hyphens, ensuring the word is suitable for Hangman.

hangman(word): The main game function, which:

Initializes variables to track the letters in the word (wordlist), letters guessed correctly (displaylist), lives left (life), and letters already used (used).
Uses a while loop to allow the player to guess letters until they either guess the word or run out of lives.
Checks each guess to see if it’s in the word:
If correct, it updates displaylist and decrements letters_remaining.
If incorrect, it decrements the life counter.
Displays the current progress of the word and lives remaining after each guess.
Tracks used letters to prevent duplicate guesses.
Ends the game with a win or loss message and updates win or lose accordingly.
game(): The main game loop that prompts the player to start a new game, play again, or exit. It calls hangman(get_valid_word(words)) to start a game with a random word and provides feedback after each round.

Game Flow:

Each round, the player is asked if they want to play.
A random word is selected for each game, and the player attempts to guess it within the allowed number of lives.
At the end of each game, the player is asked if they would like to play again.
Example Usage
To start the game, simply run the script. The game will keep track of wins and losses and allow the player to replay or exit after each round.

This script provides an engaging way to practice letter guessing, with user input checks to ensure a smooth game experience.
