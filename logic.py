# logic.py
# Пример файла с логикой (например, blackjack.py)

def hand_value(hand):
    """Возвращает сумму очков в руке."""
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
