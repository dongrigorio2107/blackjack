import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
hand = []
dealer_hand = []

def remove_cards(lst):
    for card in lst:
        cards.remove(card)

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

def dealer_deal():
    random_dealer_hand = random.sample(cards, 2)
    dealer_hand.extend(random_dealer_hand)
    remove_cards(random_dealer_hand)

def dealer_take():
    random_card = random.choice(cards)
    dealer_hand.append(random_card)
    cards.remove(random_card)   

def dealer_play(depth=0):
    value = hand_value(dealer_hand)
    if depth == 0:
        print("Dealer's turn ")
    if value < 17:
        dealer_take()
        print(f'Dealer: {dealer_hand}')
        dealer_play(depth + 1)
        return
    elif 16 < value < 21:
        if depth == 0:
            print(f'Dealer: {dealer_hand} ')
        print('Dealer stands ')
        if hand_value(hand) > hand_value(dealer_hand):
            print('You win! ')
        elif hand_value(hand) < hand_value(dealer_hand):
            print('You lost! ')
    elif value > 21:
        print('Bust ')
        print('You win! ')
    elif value == 21:
        print('Dealer has a blackjack! ')
        print('You lost!')
    else:
        dealer_play(depth + 1)
        return
    try_again()
    return

def deal_cards():
    random_hand = random.sample(cards, 2)
    hand.extend(random_hand)
    remove_cards(random_hand)
    print(f'------------------------------------------------------\nYou: {hand}')
    dealer_deal()

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
    if get_valid_input('Try again? (1/2): ') == '1':
        hand.clear()
        dealer_hand.clear()
        deal_cards()
        new_answer = get_valid_input('Hit or Stand? (1/2): ')
        hit_or_stand(new_answer)
    else:
        print('------------------------------------------------------\nGoodbye!\n')
        return

def hit_or_stand(answer, first_turn=True):
    random_card = random.choice(cards)
    if answer == '1':
        hand.append(random_card)
        cards.remove(random_card)
        print(f'You: {hand} ')
        value = hand_value(hand)
        if value > 21:
            print(f'Dealer: {dealer_hand} ')
            print('Bust ')
            print('You lost! ')
            try_again()
            return
        elif value == 21:
            print(f'Dealer: {dealer_hand} ')
            print('Blackjack! ')
            print('You win! ')
            try_again()
            return
        else:
            print(f'Dealer: [{dealer_hand[0]},|*|]')
            new_answer = get_valid_input('Hit or Stand? (1/2): ')
            hit_or_stand(new_answer)
    elif answer == '2':
            dealer_play()
            return
    

deal_cards()
answer = get_valid_input('Hit or Stand? (1/2): ')
hit_or_stand(answer)