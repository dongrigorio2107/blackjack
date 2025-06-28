# interface_blackjack_demo.py
# Пример простого интерфейса, который использует логику из logic_blackjack.py
import tkinter as tk
from logic_blackjack import hand_value, deal_cards, dealer_take

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
hand = []
dealer_hand = []

root = tk.Tk()
root.title('Blackjack Demo')

player_var = tk.StringVar()
dealer_var = tk.StringVar()

# Функция для раздачи карт игроку и дилеру
def start_game():
    hand.clear()
    dealer_hand.clear()
    cards.clear()
    cards.extend([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4)
    deal_cards(cards, hand)
    deal_cards(cards, dealer_hand)
    update_labels()

def update_labels():
    player_var.set(f'Ваши карты: {hand} (сумма: {hand_value(hand)})')
    dealer_var.set(f'Карты дилера: {dealer_hand} (сумма: {hand_value(dealer_hand)})')

player_label = tk.Label(root, textvariable=player_var, font=("Arial", 14))
player_label.pack(pady=10)
dealer_label = tk.Label(root, textvariable=dealer_var, font=("Arial", 14))
dealer_label.pack(pady=10)

start_btn = tk.Button(root, text='Начать игру', command=start_game)
start_btn.pack(pady=10)

root.mainloop()
