
import tkinter as tk

root = tk.Tk()
root.title('MyBlackjack')

window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f'{window_width}x{window_height}+{x}+{y}')

top_frame = tk.Frame(bg="#393E46", relief=tk.RAISED, borderwidth=1)
top_frame.place(relx=0, rely=0, relheight=0.1, relwidth=1)

title = tk.Label(text='MyBlackjack', master=top_frame, bg='#393E46', fg='white', font=('Roboto', 12, 'bold'))
title.place(relx=0.5, rely=0.5, anchor='center')

button_frame = tk.Frame(bg="#411D1D", relief=tk.SOLID, borderwidth=3)
button_frame.place(relx=0, rely=0.8, relheight=0.2, relwidth=1)

card_frame = tk.Frame(bg='#648A35')
card_frame.place(relx=0, rely=0.1, relheight=0.7, relwidth=1)

card_label = tk.Label(master=card_frame, bg='#648A35', text='Here will be cards')
card_label.place(rely=0.5, relx=0.5, anchor='center')

border_frame = tk.Frame(
    master=button_frame,
    width=305,
    height=55,
    borderwidth=2,
    background='#411D1D',
    relief=tk.SOLID
)
border_frame.place(relx=0.5, rely=0.5, anchor='center')

inner_frame = tk.Frame(
    master=border_frame,
    width=300, 
    height=50,
    background="grey"
    )
inner_frame.place(relx=0.5, rely=0.5, anchor='center')
inner_frame.grid_propagate(False)

for i in range(3):
    inner_frame.columnconfigure(i, weight=1),
    inner_frame.rowconfigure(0, weight=1)

    button = tk.Button(
    master=inner_frame,
    width=10,
    bg="#393E46",
    fg='#EEEEEE',
    activebackground="grey",
    text=f'Text'
    )
    button.grid(
    row=0,     
    column=i, 
    padx=1,
    sticky='nsew'
    )

root.mainloop()