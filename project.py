import random
import sys


def main():
    random_vocab = select_vocab()

    underscores = format_underscores(random_vocab)
    print(underscores)

    attempts = 5 #initialize # of tries
    guessed_letters = [] #empty list for guessed characters

    while attempts > 0:
        guess = input("Enter a letter: ").strip().lower()
        check_input(guess)

        while guess in guessed_letters:
            print(f"Letter was previously used. Letters used so far: {guessed_letters}. Try again.")
            guess = input("Enter a letter: ").strip().lower()
            check_input(guess)

        guessed_letters.append(guess)
        print(f"letters used so far: {guessed_letters}")

        if guess not in list(random_vocab):
            attempts -= 1
            print(f"This letter is not in the word! You have {attempts} attempts left.")
        else:
            for position in range(len(random_vocab)):
                if guess == random_vocab[position]:
                    underscores = underscores[:position * 2] + random_vocab[position] + underscores[position * 2 + 1:]
            print(underscores)
            if "_" not in underscores:
                sys.exit("Congratulations! You got the word!")

    if attempts == 0:
        sys.exit(f"Uh oh. You've used all attempts, the word was {random_vocab}.")


def select_vocab():
    vocab = ["test", "obfuscate", "funny", "computers", "coding", "python", "matrix", "programming", "iphone", "macbook", "screen"]
    random_vocab = random.choice(vocab)
    return random_vocab


def format_underscores(random_vocab):
    length_word = len(random_vocab) #getting the length of the chosen word
    underscores = "_ " * length_word #number of underscores + space that matches the length of word
    return underscores


def check_input(guess):
        if guess.isalpha() == True & len(guess) == 1:
            pass
        else:
            raise TypeError("Please only enter single alphabets.")


if __name__ == "__main__":
    main()
