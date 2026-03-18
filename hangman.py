import random

# Predefined word list (5 words only)
WORDS = ["apple", "brain", "chair", "dream", "earth"]

MAX_ATTEMPTS = 6


def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


def hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = MAX_ATTEMPTS

    print("🎮 Welcome to Hangman Game")
    print("Guess the word letter by letter\n")

    while attempts_left > 0:
        print("Word:", display_word(word, guessed_letters))
        print("Guessed Letters:", guessed_letters)
        print("Attempts Left:", attempts_left)

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Enter only ONE alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠ Already guessed.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts_left -= 1
            print("❌ Wrong guess!")

        if is_word_guessed(word, guessed_letters):
            print("\n🎉 Congratulations! You guessed the word:", word)
            return

        print()

    print("\n💀 Game Over! The word was:", word)


if __name__ == "__main__":
    hangman()