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

top_frame = tk.Frame(bg="#444479", relief=tk.RAISED)
top_frame.place(relx=0, rely=0, relheight=0.1, relwidth=1)

extra_frame = tk.Frame(
    width=200,
    height=134,
    borderwidth=2,
    background='#282324',
    relief=tk.GROOVE
)
extra_frame.place(relx=0.5, rely=0.5, anchor='center')

root_frame = tk.Frame(
    width=300, 
    height=300,
    background="#282324"
    )
root_frame.place(relx=0.5, rely=0.5, anchor='center')

for i in range(3):
    root.grid_rowconfigure(i, minsize=100)
    root.grid_columnconfigure(i, minsize=100)
    for j in range(3):
        frame = tk.Frame(
            master=root_frame,
            background='grey',
            relief=tk.RAISED,
            borderwidth=1,
        )
        outer_padx = 2 if j == 0 or j == 2 else 1
        outer_pady = 2 if i == 0 or i == 2 else 1

        frame.grid(row=i,
        column=j, 
        sticky='nsew', 
        padx=outer_padx,
        pady=outer_pady
        )
        label = tk.Label(master=frame, 
        background='grey',
        text=f'Row {i},\nColumn {j}'
        )
        label.pack(expand=True, fill='both')

root.mainloop()