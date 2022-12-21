import random
import os

NUM_OF_WORDS = 8

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def isWord(x, y):
    if x == y:
        return True
    return False


def correctLetters(x, y):
    x_letters = [*x]
    y_letters = [*y]
    count = 0
    for i in range(len(x_letters)):
        if x_letters[i] == y_letters[i]:
            count += 1
    return count


def numOfGuesses(x):
    guesses = x - 1
    return guesses


def getWords():
    file_exists = os.path.isfile('/usr/share/dict/words')
    if (file_exists):
        with open('/usr/share/dict/words', 'r') as file:
            full_list_of_words = file.read().replace('\n', ' ').lower().split()
            list_of_words = []
            while len(list_of_words) < NUM_OF_WORDS:
                random_word = random.choice(full_list_of_words)
                if len(random_word) == 8:
                    list_of_words.append(random_word)
            return list_of_words
    else:
        with open('test_words.txt', 'r') as file:
            list_of_words = file.read().replace('\n', ' ').lower().split()
            return list_of_words

def getRandomWord(x):
    random_word = random.choice(x)
    return random_word


def getGuess():
    guess = input('What is your guess? ')
    return guess


def checkNumberOfLetters(x, y):
    if len(x) == len(y):
        return True
    return False



def playAgain():
    again = input('Would you like to play again? (Y/N) ').lower()
    if again == 'y' or again == 'yes':
        return True
    elif again == 'n' or again == 'yes':
        return False
    else: 
        print('Invalid response\nPlease input Y or N:')
    return False

def quitCheck(x):
    if x.lower() == 'q':
        return True
    return False


def playGame():
    cls()
    guesses = 8
    words = getWords()
    print('Word List:')
    for word in words:
        print(word)
    secrect_word = getRandomWord(words)
    print(f'Guess ({guesses} left)?')
    while guesses > 0:
        guess = getGuess()
        quit = quitCheck(guess)
        if (quit):
            os._exit(0)
        num_letters = checkNumberOfLetters(secrect_word, guess)
        if (num_letters):
            correct = isWord(secrect_word, guess)
            if (correct):
                print('You Win!\n')
                break
            else:
                guesses = numOfGuesses(guesses)
                print(f'Guess ({guesses} left)?')
                num_correct = correctLetters(secrect_word, guess)
                print(f'{num_correct}/{len(secrect_word)} correct')
            if guesses == 0:
                print('You lose\n')
                print(f'The word was: {secrect_word}')
        else:
            print(f'Invalid entry\nPlease enter a word with {len(secrect_word)} letters')
    again = playAgain()
    if (again):
        playGame()


playGame()