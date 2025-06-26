import random
from time import sleep

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
hand = []
dealer_hand = []

def remove_cards(lst):
    for card in lst:
        cards.remove(card)

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

def dealer_deal():
    random_dealer_hand = random.sample(cards, 2)
    dealer_hand.extend(random_dealer_hand)
    remove_cards(random_dealer_hand)
    print(f'Dealer: [{dealer_hand[0]},|*|] ')

def dealer_take():
    random_dealer_card = random.choice(cards)
    dealer_hand.append(random_dealer_card)
    remove_cards(random_dealer_card)   

def dealer_play():
    value = hand_value(dealer_hand)
    if value < 17:
        random_card = random.choice(cards)
        dealer_hand.append(random_card)
        cards.remove(random_card)
        sleep(2)
        print(f'Dealer: {dealer_hand}')
        sleep(1)
        dealer_play()
        return
    elif 16 < value < 21:
        print(f'Dealer: {dealer_hand}')
        sleep(1)
        print('Dealer stands ')
        if hand_value(hand) > hand_value(dealer_hand):
            sleep(1.5)
            print('You win! ')
        elif hand_value(hand) < hand_value(dealer_hand):
            sleep(1.5)
            print('You lost! ')
    elif value > 21:
        print('Bust ')
        sleep(1.5)
        print('You win! ')
    elif value == 21:
        print('Dealer has a blackjack! ')
        sleep(1.5)
        print('You lost!')
    else:
        sleep(1)
        dealer_play()
        return
    try_again()
    return

def deal_cards():
    random_hand = random.sample(cards, 2)
    hand.extend(random_hand)
    remove_cards(random_hand)
    print(f'------------------------------------------------------\nYou: {hand}')
    sleep(1)
    dealer_deal()
    sleep(1)

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
        sleep(1)
        print('------------------------------------------------------\nGoodbye!\n')
        return

def hit_or_stand(answer, first_turn=True):
    random_card = random.choice(cards)
    if answer == '1':
        sleep(0.1)
        hand.append(random_card)
        cards.remove(random_card)
        sleep(1)
        print(f'You: {hand} ')
        sleep(1)
        value = hand_value(hand)
        if value > 21:
            print(f'Dealer: {dealer_hand} ')
            print('Bust ')
            sleep(1)
            print('You lost! ')
            sleep(1.5)
            try_again()
            return
        elif value == 21:
            print(f'Dealer: {dealer_hand} ')
            print('Blackjack! ')
            print('You win! ')
            sleep(1.5)
            try_again()
            return
        else:
            print(f'Dealer: [{dealer_hand[0]},|*|]')
            new_answer = get_valid_input('Hit or Stand? (1/2): ')
            hit_or_stand(new_answer)
    elif answer == '2':
            sleep(1)
            print("Dealer's turn")
            dealer_play()
            return
    

deal_cards()
answer = get_valid_input('Hit or Stand? (1/2): ')
hit_or_stand(answer)