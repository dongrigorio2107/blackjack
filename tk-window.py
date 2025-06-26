import tkinter as tk

root = tk.Tk()
root.title('Окно Tkinter')

window_width = 400
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f'{window_width}x{window_height}+{x}+{y}')

label = tk.Label(root, text='Привет')
label.pack()

def on_click():
    label.config(text='Еба, ты жмякнул кнопку!')

button = tk.Button(root, text='Нажми', command=on_click)
button.pack()

root.mainloop()