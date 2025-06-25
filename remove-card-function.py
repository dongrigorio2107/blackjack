from time import sleep
from random import choice

cards = [2, 3, 4] * 2

def remove_card(lst, first_cycle=True):
    first_cycle = True
    random_card = choice(lst)
    if first_cycle == True:
        print(f'----------------------------------------------- \n {set(lst)}')
    else:
        print('\nset(lst)')
    print(f'{len(lst)} cards left')
    sleep(1)
    answer = input('Press Enter to remove random card: ')
    if answer == '':
        lst.remove(random_card)
        sleep(1)
        print(f'\nRemoved {random_card}')
        print(f'{lst.count(random_card)} instance(s) left\n')
        sleep(1)
        if len(lst) > 0:
            remove_card(lst, first_cycle=False)
        else:
            print('Over\n')

remove_card(cards)