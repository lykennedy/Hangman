import random
import pandas
try:
    pd = pandas
    words = list(pd.read_csv('Hangman_wordbank.csv'))
    word = []
    for i in words:
        word.append(i.replace(' ', ''))
    blank = []
    chances = 0
    selected_word = word[random.randint(0, len(word)-1)]
    correct_word = list(selected_word)
    for i in range(len(selected_word)):
        blank.append('_')
    print(blank)
    check = False
    while not check:
        if blank == correct_word:
            print("You got the word correct. Congratulations.")
            print(blank)
            break
        else:
            if chances == 3:
                break
            print(blank)
            print('You have ' + str(3 - chances) + ' chances left')
            guess = input('What is your guess?')
            if len(guess) > 1:
                if guess == selected_word:
                    print("You got it right. Congratulations.")
                    print(correct_word)
                    break
                else:
                    print("Sorry, you got it wrong.")
                    chances += 1
            else:
                if guess in correct_word:
                    for counter, i in enumerate(correct_word):
                        if i == guess:
                            blank[counter] = correct_word[counter]
                else:
                    chances += 1
    print("The word was " + selected_word)
except KeyboardInterrupt:
    print('Exiting program')
