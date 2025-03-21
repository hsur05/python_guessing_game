# Python Word Guessing Game

A simple command-line word guessing game built with Python. Players have 5 attempts to guess a randomly selected word by suggesting letters one at a time.

## How to Play

1. The game randomly selects a word from its vocabulary
2. You get 5 attempts to guess the word
3. Enter one letter at a time
4. If your guess is correct, all instances of that letter are revealed
5. If your guess is incorrect, you lose an attempt
6. You win by correctly guessing all letters in the word
7. You lose if you run out of attempts

## Features

- Random word selection from a predefined vocabulary
- Input validation for letter guesses
- Tracking of previously guessed letters
- Visual representation of word progress using underscores
- Game ends when the player wins or runs out of attempts

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the `project_final.py` file
2. No additional dependencies are required

## Usage

Run the game using Python:

```bash
python project_final.py
```

## Game Mechanics

- Words are randomly selected from a predefined list
- Each letter is represented by an underscore "_"
- Correctly guessed letters replace their corresponding underscores
- The game tracks letters you've already guessed
- You cannot guess the same letter twice

## Word List

The game includes the following words:
- test
- obfuscate
- funny
- computers
- coding
- python
- matrix
- programming
- iphone
- macbook
- screen

## Example Gameplay

```
_ _ _ _ _ _
Enter an alphabet: a
letters used so far: ['a']
This letter is not in the word! You have 4 attempts left.
Enter an alphabet: p
letters used so far: ['a', 'p']
p _ _ _ _ _
Enter an alphabet: y
letters used so far: ['a', 'p', 'y']
p y _ _ _ _
...
Congratulations! You got the word!
```

## Customization

To add more words to the game, edit the `vocab` list in the `select_vocab()` function.

## License

This project is available for open use.

## Author

[Your Name] - Initial work

## Acknowledgments

- Inspired by the classic Hangman game
