from tkinter.constants import CENTER, LEFT, RIGHT, TOP, X, Y
import MongoCommand
import tkinter as tk
from tkinter import ttk



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

        ##################################################################################
        # Frames
        ##################################################################################

        invoice_frame = tk.Frame(self,
                                 bg='#ff0000')
        invoice_frame.pack(fill= Y, side= LEFT)

        detail_frame = tk.Frame(invoice_frame,
                                 bg='#ff0f00')
        detail_frame.pack(fill= X, padx=20)

        detail_frame1 = tk.Frame(detail_frame, bg='#ff0f00')
        detail_frame1.pack(fill = X)

        detail_frame2 = tk.Frame(detail_frame, bg='#ff0f00')
        detail_frame2.pack(fill = X)



        invoice_label = tk.Label(invoice_frame,
                                      text='Invoice',
                                      font=('orbitron',23),
                                      fg='white',
                                      bg='#3d3d5c')
        invoice_label.pack(fill=X, pady= 5)
        
        invoice_heading = tk.Frame(invoice_frame, bg='#ff0f00')
        invoice_heading.pack(fill = X)       

        button_frame = tk.Frame(self,
                                 bg='#00ff00')
        button_frame.pack(fill= Y, side= RIGHT)

        Name_Label = tk.Label(detail_frame1,
            text='Custmer\'s Name:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Name_Label.grid(row=0,column=0,pady=5,padx= 5)

        Name_box = tk.Entry(detail_frame1,
                                                              
                                                              font=('orbitron',23),
                                                              width=15,borderwidth=2,
                                                              justify='center')
        Name_box.grid(row=0,column=1,pady=5)

        Phone_label = tk.Label(detail_frame1,
            text='Phone:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Phone_label.grid(row=0,column=2,pady=5, padx= 10)


        Phone_box = tk.Entry(detail_frame1,
                                                              
                                                              font=('orbitron',23),
                                                              width=12,borderwidth=2,
                                                              justify= 'center')
        Phone_box.grid(row=0,column=3,pady=5,padx=10)

        Age_Label = tk.Label(detail_frame2,
            text='Age:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Age_Label.grid(row=1,column=0,pady=5, padx= 5)


        Age_box = tk.Entry(detail_frame2,
                                                              
                                                              font=('orbitron',23),
                                                              width=5,borderwidth=2,
                                                              justify= 'center')
        Age_box.grid(row=1,column=1,pady=5,padx=10)


        item_Label = tk.Label(invoice_heading,
            text='Items',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        item_Label.grid(row=0,column=0,sticky="ew")

        price_Label = tk.Label(invoice_heading,
            text='Price',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        price_Label.grid(row=0,column=1,sticky="ew")

        qty_Label = tk.Label(invoice_heading,
            text='Quantity',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        qty_Label.grid(row=0,column=2,sticky="ew")

        total_Label = tk.Label(invoice_heading,
            text='Total',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        total_Label.grid(row=0,column=3,sticky="ew")

        languages = ('Python', 'JavaScript', 'Java',
                        'Swift', 'GoLang', 'C#', 'C++', 'Scala')
        
        option_var = tk.StringVar(self)
        # items = tk.StringVar()
        # items.set(OptionList[0]) #defult

        def option_changed(self, *args):
            #self.output_label['text'] = f'You selected: {self.option_var.get()}'
            print('click')
        for row in range(8):
            for column in range(4):
                if column == 0:
                    self.e = ttk.OptionMenu(
                                                invoice_heading,
                                                option_var,
                                                languages[0],
                                                *languages,
                                                command=option_changed)
                    #command=option_changed)
                    #self.e.config(font=('orbitron',15),width=10)
                    self.e.grid(row=row+1,column=column, sticky= 'w')
                else:  
                    self.e = tk.Entry(invoice_heading, width=18, justify= 'center', font=('orbitron',18))
                    self.e.grid(row=row+1,column=column)

        total_foot_Label = tk.Label(invoice_heading,
            text='Total',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        total_foot_Label.grid(row=10,column=2,sticky="ew")

        discount_foot_Label = tk.Label(invoice_heading,
            text='Discount',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        discount_foot_Label.grid(row=11,column=2,sticky="ew")

        GT_foot_Label = tk.Label(invoice_heading,
            text='Grand Total',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        GT_foot_Label.grid(row=12,column=2,sticky="ew")
