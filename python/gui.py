import tkinter as tk
import main



root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

quit_button = tk.Button(frame, 
    text="QUIT", 
    fg="red",
    command=quit)
quit_button.pack(side=tk.LEFT)

add_button = tk.Button(frame,
    text="Add Customer",
    command=main.add_cust)
add_button.pack(side=tk.LEFT)

fetch_by_id_button = tk.Button(frame,
    text="Find Customer by Customer Id",
    command=main.fetch_by_id)
fetch_by_id_button.pack(side=tk.LEFT)

fetch_by_id_button = tk.Button(frame,
    text="Find Customer by Phone no.",
    command=main.fetch_by_phone)
fetch_by_id_button.pack(side=tk.LEFT)

fetch_by_id_button = tk.Button(frame,
    text="Remove Customer",
    command=main.remove_cust)
fetch_by_id_button.pack(side=tk.LEFT)
frame.mainloop()
    