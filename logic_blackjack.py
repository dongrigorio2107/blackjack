# logic_blackjack.py
# Только логика, без print и input
import random

def hand_value(hand):
    value = 0
    for card in hand:
        if card == 'A':
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        elif isinstance(card, str):
            value += 10
        else:
            value += card
    return value

def deal_cards(cards, hand):
    random_hand = random.sample(cards, 2)
    hand.extend(random_hand)
    for card in random_hand:
        cards.remove(card)
    return random_hand

def dealer_take(cards, dealer_hand):
    random_card = random.choice(cards)
    dealer_hand.append(random_card)
    cards.remove(random_card)
    return random_card
