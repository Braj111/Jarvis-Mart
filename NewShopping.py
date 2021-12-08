from tkinter.constants import LEFT, RIGHT, TOP, X, Y
import MongoCommand
import tkinter as tk



class New_shopping_page(tk.Frame):
    
    
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
                                      text='Shopping',
                                      font=('orbitron',23),
                                      fg='white',
                                      bg='#3d3d5c')
        Enter_Detail_label.pack()

        invoice_frame = tk.Frame(self,
                                 bg='#ff0000')
        invoice_frame.pack(fill= Y, side= LEFT)

        detail_frame = tk.Frame(invoice_frame,
                                 bg='#ff0f00')
        detail_frame.pack(fill= X, padx=20)

        button_frame = tk.Frame(self,
                                 bg='#00ff00')
        button_frame.pack(fill= Y, side= RIGHT)

        Name_Label = tk.Label(detail_frame,
            text='Custmer\'s Name:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Name_Label.grid(row=0,column=0,pady=5)

        Name_box = tk.Entry(detail_frame,
                                                              
                                                              font=('orbitron',23),
                                                              width=22,borderwidth=2)
        Name_box.grid(row=0,column=1,pady=5)

        Age_Label = tk.Label(detail_frame,
            text='Custmer\'s Name:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Age_Label.grid(row=0,column=2,pady=5)

        Age_box = tk.Entry(detail_frame,
                                                              
                                                              font=('orbitron',23),
                                                              width=22,borderwidth=2)
        Age_box.grid(row=0,column=3,pady=5)