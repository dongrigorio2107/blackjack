import random

CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
random_hand = random.sample(CARDS, 2)
random_card = random.sample(CARDS, 1)
hand = []

def start(answer):
    if answer == '1':
        deal_cards()
    elif answer == '2':
        print('Goodbye! ')

def deal_cards():
    hand.extend(random_hand)
    print(hand)

#TODO: УБРАТЬ sum(hand) И СОЗДАТЬ hand_value() (итерация через руку и суммирование значений)

def hit_or_stand(answer):
    if answer == '1':
        global hand
        hand.extend(random_card)
        if sum(hand) < 21:    
            print(hand)
            hit_or_stand(answer)
        elif sum(hand) > 21:
            print('You lost! ')
        else:
            print('Blackjack! ')
    elif answer == '1':
        print('... ')

start_answer = input('Start game? (1/2): ')
start(start_answer)

hit_answer = input('Hit or Stand? (1/2): ')
hit_or_stand(hit_answer)


