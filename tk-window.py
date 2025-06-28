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
    width=215,
    height=60,
    borderwidth=3,
    background='#287F3E',
    relief=tk.GROOVE
)
extra_frame.place(relx=0.5, rely=0.5, anchor='center')

root_frame = tk.Frame(
    width=200, 
    height=50,
    background="#287F3E"
    )
root_frame.place(relx=0.5, rely=0.5, anchor='center')
root_frame.grid_propagate(False)

for i in range(3):
    root_frame.columnconfigure(i, weight=1),
    root_frame.rowconfigure(0, weight=1)
    button = tk.Button(
    master=root_frame,
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