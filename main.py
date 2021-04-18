import random


def get_words(words, min_word_length=None):
    with open(words, encoding='utf-8') as file:
        wordlist = []
        for line in file:
            words = line.split()  # split words into a list

            if min_word_length is not None:  # if min length parameter is given, take only words that are long enough
                words = [word for word in words if len(word) >= min_word_length]

            wordlist += words
    return wordlist


def guess_letters():
    word_to_guess = random.choice(get_words('data/words.txt', min_word_length=6))
    wrong_guesses_made = 0
    max_incorrect_guesses = 20
    used_letters = []
    word_progress = (word_to_guess[0] + ' ' + "_ " * (len(word_to_guess) - 2) + word_to_guess[-1])
    print(
        f"Guess this word letter by letter! The game ends after you have made {max_incorrect_guesses} incorrect guesses.")
    print()
    print(word_progress)
    print()
    while wrong_guesses_made <= max_incorrect_guesses:
        guess = input("Insert one letter and press Enter: ")
        while True:
            if len(guess) != 1 or guess.isalpha() == False:
                guess = input('You entered something which is not ONE LETTER. Try again: ')
                continue
            else:
                break
        print()
        if guess in word_to_guess and guess not in used_letters:
            print("Correct!")
            used_letters.append(guess)
            i = 0
            word_progress_split = word_progress.split()
            while i < len(word_to_guess):
                if guess == word_to_guess[i]:
                    word_progress_split[i] = guess
                    i = i + 1
                else:
                    i = i + 1
            word_progress = ' '.join(word_progress_split)
            if '_' not in word_progress:
                print('..and you have guessed the word: ' + word_to_guess)
                break

        elif guess in word_to_guess and guess in used_letters:
            print("Correct, but you already guessed that letter. Try something else!")

        elif guess not in word_to_guess and guess in used_letters:
            print("Nope, and you already tried that!")

        elif guess not in word_to_guess and guess not in used_letters:
            print('Nope!')
            used_letters.append(guess)
            wrong_guesses_made = wrong_guesses_made + 1

        print(f'You have {max_incorrect_guesses - wrong_guesses_made} incorrect guesses left.')
        print("You have already tried these letters: " + str(used_letters))
        print()
        print(word_progress)
        print()
    else:
        print("Out of guesses!")
        print('The word: ' + word_to_guess)


if __name__ == '__main__':
    guess_letters()