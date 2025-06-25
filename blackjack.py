import random

CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
random_hand = random.sample(CARDS, 2)
hand = []

def deal_cards():
    hand.extend(random_hand)
    print(hand)

def hand_value(hand):
    sum = 0
    for card in hand:
        if isinstance(card, str) and card != 'A':
            sum += 10
        elif card != 'A': 
            sum += card
        if card == 'A':
            if sum + 11 <= 21:
                sum += 11
            else:
                sum += 1
    return sum

def hit_or_stand(answer):
    random_card = random.sample(CARDS, 1)
    if answer == '1':
        hand.extend(random_card)
        print(hand)
        value = hand_value(hand)
        if value > 21:
            print('You lost! ')
            return
        elif value == 21:
            print('Blackjack! ')
        else:
            new_answer = hit_answer = input('Hit or Stand? (1/2): ')
            hit_or_stand(new_answer)
    elif answer == '2':
            print('Over! ')

deal_cards()

hit_answer = input('Hit or Stand? (1/2): ')
hit_or_stand(hit_answer)

#Hello