import random
from time import sleep

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
hand = []

def deal_cards():
    random_hand = random.sample(cards, 2)
    hand.extend(random_hand)
    print(f'------------------------------------------------------\n{hand}')

def hand_value(hand):
    sum = 0
    for card in hand:
        if card == 'A':
            if sum + 11 <= 21:
                sum += 11
            else:
                sum += 1
        elif isinstance(card, str):
            sum += 10
        else: 
            sum += card
    return sum

def get_valid_input(question):
    while True:
        try:
            answer = input(question)
            if answer not in ['1', '2']:
                raise ValueError('Error: Enter 1 or 2! ')
            return answer
        except Exception as e:
            print(e)

def try_again():
    if get_valid_input('Try again? (1/2): ') == 1:
        hand.clear()
        deal_cards()
        new_answer = get_valid_input()
        hit_or_stand(new_answer)
    else:
        sleep(1)
        print('------------------------------------------------------\nGoodbye!\n')
        return

def hit_or_stand(answer):
    random_card = random.choice(cards)
    if answer == '1':
        sleep(0.1)
        hand.append(random_card)
        cards.remove(random_card)
        sleep(1)
        print(hand)
        value = hand_value(hand)
        if value > 21:
            sleep(1)
            print('You lost! ')
            sleep(1.5)
            try_again()
        elif value == 21:
            print('Blackjack! ')
            try_again()
        else:
            new_answer = get_valid_input('Hit or Stand? (1/2): ')
            hit_or_stand(new_answer)
    elif answer == '2':
            try_again()
    

deal_cards()
answer = get_valid_input('Hit or Stand? (1/2): ')
hit_or_stand(answer)