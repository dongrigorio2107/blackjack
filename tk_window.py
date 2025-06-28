import tkinter as tk

root = tk.Tk()
root.title('Окно Tkinter')

window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f'{window_width}x{window_height}+{x}+{y}')

top_frame = tk.Frame(bg="#444479", relief=tk.GROOVE, borderwidth=2)
top_frame.place(relx=0, rely=0, relheight=0.1, relwidth=1)

bottom_frame = tk.Frame(bg='green', relief=tk.GROOVE, borderwidth=2)
bottom_frame.place(relx=0, rely=0.5, relheight=0.2, relwidth=1)

card_frame = tk.Frame(bg='grey')
card_frame.place(relx=0, rely=0.1, relheight=0.4, relwidth=1)

card_label = tk.Label(master=card_frame, bg='grey', text='Here will be cards')
card_label.place(rely=0.5, relx=0.5, anchor='center')

border_frame = tk.Frame(
    master=bottom_frame,
    width=215,
    height=60,
    borderwidth=3,
    background='#287F3E',
    relief=tk.GROOVE
)
border_frame.place(relx=0.5, rely=0.5, anchor='center')

inner_frame = tk.Frame(
    master=border_frame,
    width=200, 
    height=50,
    background="#287F3E"
    )
inner_frame.place(relx=0.5, rely=0.5, anchor='center')
inner_frame.grid_propagate(False)

for i in range(3):
    inner_frame.columnconfigure(i, weight=1),
    inner_frame.rowconfigure(0, weight=1)
    button = tk.Button(
    master=inner_frame,
    background='grey',
    activebackground='grey',
    text=f'Row 0\nColumn {i}'
    )
    button.grid(
    row=0,     
    column=i, 
    padx=1
    )

root.mainloop()