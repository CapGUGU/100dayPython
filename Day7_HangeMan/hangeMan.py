import requests
import random
from enum import Enum

# generate random word for user to guess
def wordGenerator():
    # pick a word from online webside
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    # now we randomly pick one word
    word = random.choice(WORDS).decode('utf-8')
    return word

class status(Enum):
    FALSE = 1
    TRUE = 2
    GUESSBEFORE = 3

hangeMan = [
    "  +---+\n" +
    "  |   |\n" +
    "      |\n" +
    "      |\n" +
    "      |\n" +
    "      |\n" +
    "=========",

    "  +---+\n" +
    "  |   |\n" +
    "  O   |\n" +
    "      |\n" +
    "      |\n" +
    "      |\n" +
    "=========",

    "  +---+\n" +
    "  |   |\n" +
    "  O   |\n" +
    "  |   |\n" +
    "      |\n" +
    "      |\n" +
    "=========",

    "  +---+\n" +
    "  |   |\n" +
    "  O   |\n" +
    " /|   |\n" +
    "      |\n" +
    "      |\n" +
    "=========",

    "  +---+\n" +
    "  |   |\n" +
    "  O   |\n" +
    " /|\  |\n" +
    "      |\n" +
    "      |\n" +
    "=========",

    "  +---+\n" +
    "  |   |\n" +
    "  O   |\n" +
    " /|\  |\n" +
    " /    |\n" +
    "      |\n" +
    "=========",

    "  +---+\n" +
    "  |   |\n" +
    "  O   |\n" +
    " /|\  |\n" +
    " / \  |\n" +
    "      |\n" +
    "=========",
]

lostTime = 0

word = list(wordGenerator())
guessWord = ['_'] * len(word)

while lostTime < len(hangeMan)-1 and word != guessWord:
    guess = input("\nGuess a letter: ")
    check = status.FALSE
    for i in range(0,len(word)):
        # if the guess letter in word
        if guess == word[i]:
            # if the guess letter not guess before
            if guess != guessWord[i]:
                guessWord[i] = guess
                check = status.TRUE
            elif check != status.GUESSBEFORE:
                check = status.GUESSBEFORE

    # print guessword
    for letter in guessWord:
        print(f'{letter}',end=' ')
    print('\n')
    # print result feedback
    if check == status.FALSE:
        lostTime += 1
        print(f'You guessed {guess},  that\' not in the word, You lose a life.')
    elif check == status.GUESSBEFORE:
        lostTime += 1
        print(f'You guessed {guess},  that\' in the word, But you guess before, You lose a life.')
    elif check == status.TRUE:
        print(f'You guessed {guess},  that\' in the word, Good.')
    # print the hange man
    print(hangeMan[lostTime])

# check if win or lose
print('\n')
if lostTime >= len(hangeMan)-1:
    print('You lose')
    wordStr = ''.join(word)
    print(f'The word is: {wordStr}')
else:
    print('You win')