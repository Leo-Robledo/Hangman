import pygame
import random
from hangman_list1 import text_w

def gallows(penal):
    if penal == 0:
        gal = '-------| \n'\
              '       | \n'\
              '       | \n'\
              '       | \n'\
              '       | \n'\
              '       | \n'\
              '      / \  \n'\
              '     /   \  \n'\
              '    =======  \n'
    if penal == 1:
        gal = '-------| \n' \
              '  |    | \n' \
              '       | \n' \
              '       | \n' \
              '       | \n' \
              '       | \n' \
              '      / \  \n' \
              '     /   \  \n' \
              '    =======  \n'
    if penal ==2:
        gal = '-------| \n' \
              '  |    | \n' \
              '  O    | \n' \
              '       | \n' \
              '       | \n' \
              '       | \n' \
              '      / \  \n' \
              '     /   \  \n' \
              '    =======  \n'
    if penal == 3:
        gal = '-------| \n' \
              '  |    | \n' \
              '  0    | \n' \
              '  |    | \n' \
              '  |    | \n' \
              '  |    | \n' \
              '      / \  \n' \
              '     /   \  \n' \
              '    =======  \n'
    if penal == 4:
        gal = '-------| \n' \
              '  |    | \n' \
              '  0    | \n' \
              '  |    | \n' \
              '  |    | \n' \
              '  |    | \n' \
              ' /    / \  \n' \
              '     /   \  \n' \
              '    =======  \n'
    if penal == 5:
        gal = '-------| \n' \
              '  |    | \n' \
              '  0    | \n' \
              '  |    | \n' \
              '  |    | \n' \
              '  |    | \n' \
              ' / \  / \  \n' \
              '     /   \  \n' \
              '    =======  \n'
    if penal == 6:
        gal = '-------| \n' \
              '  |    | \n' \
              '  0    | \n' \
              ' /|    | \n' \
              '  |    | \n' \
              '  |    | \n' \
              ' / \  / \  \n' \
              '     /   \  \n' \
              '    =======  \n'
    if penal == 7:
        gal = '-------| \n' \
              '  |    | \n' \
              '  0    | \n' \
              ' /|\   | \n' \
              '  |    | \n' \
              '  |    | \n' \
              ' / \  / \  \n' \
              '     /   \  \n' \
              '    =======  \n'
    if penal == 8:
        gal = '-------| \n' \
              '  |    | \n' \
              '  0    | \n' \
              ' /|\   | \n' \
              '  |    | \n' \
              '  |    | \n' \
              './ \  / \  \n' \
              '     /   \  \n' \
              '    =======  \n'
    if penal == 9:
        gal = '-------| \n' \
              '  |    | \n' \
              '  0    | \n' \
              ' /|\   | \n' \
              '  |    | \n' \
              '  |    | \n' \
              './ \. / \  \n' \
              '     /   \  \n' \
              '    =======  \n'
    if penal == 10:
        gal = '-------| \n' \
              '  |    | \n' \
              '  0    | \n' \
              './|\.  | \n' \
              '  |    | \n' \
              '  |    | \n' \
              './ \. / \  \n' \
              '     /   \  \n' \
              '    =======  \n'
    if penal == 11:
        gal = '-------| \n' \
              '  |    | \n' \
              ' ~0    | \n' \
              './|\.  | \n' \
              '  |    | \n' \
              '  |    | \n' \
              './ \. / \  \n' \
              '     /   \  \n' \
              '    =======  \n'
    if penal == 12:
        gal = '-------| \n' \
              '  |    | \n' \
              ' ~0~   | \n' \
              './|\.  | \n' \
              '  |    | \n' \
              '  |    | \n' \
              './ \. / \  \n' \
              '     /   \  \n' \
              '    =======  \n'


    return gal


again = 'y'
while again == 'y':
    index = random.randint(0, len(text_w))

    word = text_w[index]
    secret_word = list(word)
    # print(secret_word)
    new_word = ['*' for i in range(len(secret_word))]
    print(new_word)

    penalty = 0
    letters_used = []

    while '*' in new_word and penalty < 12:
        guess = input('Enter a letter \n')
        if guess not in secret_word or guess in letters_used:
            penalty += 1
        else:
            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    new_word[i] = secret_word[i]
        letters_used.append(guess)
        print(letters_used)
        print('penalty', penalty)
        print(gallows(penalty))
        print(new_word)
    print('the end.')
    # print(secret_word)
    again = input('Enter y if you want to play another game, else enter n \n')
if '*' == secret_word:
    print(secret_word)
print('Thank you for playing the game.')
exit()

