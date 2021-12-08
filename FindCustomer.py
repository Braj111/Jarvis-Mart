import MongoCommand
import tkinter as tk


class find_customer(tk.Frame):
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        heading_label = tk.Label(self,
            text='Customer-Management-System',
            font=('orbitron',45,'bold'),
            foreground='#ffffff',
            background='#3d3d5c')
        heading_label.pack(pady=25)

        Enter_Detail_label = tk.Label(self,
            text='Find Customer Page',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Enter_Detail_label.pack()

        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)
        Name_Label = tk.Label(button_frame,
            text='Custmer\'s ID:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Name_Label.grid(row=0,column=0,pady=5)
        Name_box = tk.Entry(button_frame,
                                                              
                                                              font=('orbitron',23),
                                                              width=22,borderwidth=2)
        Name_box.grid(row=0,column=1,pady=5,padx=5)
        def find():
            controller.show_frame('MenuPage')
        Insert_button = tk.Button(button_frame,
                                                     text='Find',font=('orbitron',20),
                                                     command=find,
                                                     relief='raised',fg='red',
                                                     borderwidth = 1,
                                                     width=10,
                                                     )
        Insert_button.grid(row=0,column=2,pady=5)