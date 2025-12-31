import random

words = ["apple", "mango", "pineapple", "watermelon", "grapes"]

secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)

attempts = 6

print("Welcome to Hangman Game!")
print(" ".join(guessed_word))

while attempts > 0:
    guess = input("Guess a letter: ")

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong Guess!")
    attempts -= 1

    print(" ".join(guessed_word))
    print("Attempts left:", attempts)

    if "_" not in guessed_word:
        break

if "_" not in guessed_word:
    print("You Win! The word was:", secret_word)
else:
    print("Game Over! The word was:", secret_word)

