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
    for j in range(3):
        frame = tk.Frame(
            master=root,
            relief=tk.RAISED,
            borderwidth=1,
            width=10,
            height=10
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f'Row {i+1}, Column {j+1}')
        label.pack()

root.mainloop()