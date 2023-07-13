import random

def choose_word():
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']
    return random.choice(words)

def initialize_game():
    name = input("What is your name? ")
    print("Good Luck, ", name)
    print("Guess the characters")

def print_word(word, guesses):
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()

def get_guess():
    guess = input("Guess a character: ")
    if len(guess) != 1:
        print("Please enter only one character.")
        return None
    return guess

def play_hangman():
    word = choose_word()
    guesses = ''
    turns = 12

    while turns > 0:
        print_word(word, guesses)
        guess = get_guess()

        if guess is None:
            continue

        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", turns, 'more guesses')

            if turns == 0:
                print("You Lose")
                print("The word was:", word)
                break

        if all(char in guesses for char in word):
            print("You Win")
            break

initialize_game()
play_hangman()
