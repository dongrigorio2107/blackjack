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

for i in range(3):
    root.grid_rowconfigure(i, minsize=100)
    root.grid_columnconfigure(i, minsize=100)
    for j in range(3):
        frame = tk.Frame(
            master=root,
            background='grey',
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, sticky='nsew')
        label = tk.Label(master=frame, 
        background='grey',
        text=f'Row {i+1},\nColumn {j+1}'
        )
        label.pack(expand=True, fill='both')

root.mainloop()