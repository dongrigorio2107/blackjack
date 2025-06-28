# interface_example.py
# Пример простого интерфейса, который использует функцию из logic.py

import tkinter as tk
from logic import hand_value

root = tk.Tk()
root.title('Demo')

# Пример руки
hand = [10, 'A']

# StringVar для отображения суммы
value_var = tk.StringVar()

# Функция для обновления текста
def update_value():
    value = hand_value(hand)
    value_var.set(f'Сумма очков: {value}')

label = tk.Label(root, textvariable=value_var, font=("Arial", 16))
label.pack(padx=20, pady=20)

button = tk.Button(root, text='Посчитать сумму', command=update_value)
button.pack(pady=10)

root.mainloop()
