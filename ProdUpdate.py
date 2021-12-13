from tkinter.constants import BOTH, CENTER, E, END, LEFT, N, RIGHT, TOP, X, Y
from tkinter.font import BOLD
import MongoCommand
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class prod_update(tk.Frame):
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#0B4619')
        self.controller = controller
        heading_label = tk.Label(self,
                                 text='Customer-Management-System',
                                 font=('orbitron',45,BOLD),
                                 foreground='#FFCC1D',
                                 background='#0B4619')
        heading_label.pack(pady=25)

        searchcustomer_label = tk.Label(self,
                                   text='Manage Products',
                                   font=('orbitron',21,BOLD),
                                   fg='#B7C304',
                                   bg='#0B4619')
        searchcustomer_label.pack()

        body_frame1 = tk.Frame(self, bg='#116530')
        body_frame1.pack(side= LEFT,fill=Y, expand=True)

        body_frame2 = tk.Frame(self, bg='#116530')
        body_frame2.pack(side= RIGHT,fill=BOTH, expand=True)

        ################################################################
        #   Table frame
        ################################################################
        self.style = ttk.Style(body_frame1)
        self.style.theme_use("xpnative")
        self.style.map("Treeview")
        self.style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 15), rowheight=80)
        self.style.configure("Treeview.Heading", font=('Calibri', 15,'bold'), background='black', foreground='dark blue') 
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        columns = ('item','price')
        
        def clear():
            prodname_box.delete(0,END)
            price_box.delete(0,END)
            priceres_box.delete(0,END)
            prodnameres_box.delete(0,END)

        def selecteditem(event):
            clear()
            selecteditem = bct.focus()
            prod = bct.item(selecteditem)['values']
            prodnameres_box.insert(0,prod[0])
            priceres_box.insert(0,prod[1])

        bct = ttk.Treeview(body_frame1, columns= columns, show='headings',height=8)
       
        bct.column('item', anchor=CENTER)
        bct.column('price', anchor=CENTER)


        bct.heading('item', text='Product Name', anchor=CENTER)
        bct.heading('price', text='Price',anchor=CENTER)
        bct.bind('<<TreeviewSelect>>', selecteditem)
    
        bct.pack(fill= Y, side = LEFT, padx=50, pady= 20)
        def setprod():
            products = MongoCommand.fetch_products()
            for product in products:
                    bct.insert(parent='',index = tk.END, values= tuple(product.values()))
        setprod()

        body_frame25 = tk.Frame(body_frame2, bg='#116530')
        body_frame25.pack(side= TOP,fill=X, expand=True, pady=10)
        body_frame25.grid_anchor(anchor=CENTER)
        prodname_Label = tk.Label(body_frame25,
                            text='Product Name:',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        prodname_Label.grid(row=0, column=0, sticky=E+N)

        prodname_box = tk.Entry(body_frame25,
                                                              
                            font=('orbitron',23),
                            width=20,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        prodname_box.grid(row=0,column=1, sticky=N)

        price_Label = tk.Label(body_frame25,
                            text='Product Price:',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        price_Label.grid(row=1, column=0, sticky=E+N)

        price_box = tk.Entry(body_frame25,
                                                              
                            font=('orbitron',23),
                            width=20,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        price_box.grid(row=1,column=1, sticky=N)
        def addprod():
            name = prodname_box.get()
            price = int(price_box.get())
            MongoCommand.insert_product(name, price)
            for row in bct.get_children():
                bct.delete(row)
            setprod()
            tkinter.messagebox.showinfo('Successfull!', 'Product: '+name+', Price: '+str(price)+' added')


        add_button = tk.Button(body_frame25,
                                command=addprod,
                                fg='#FFCC1D',
                                bg = '#3C4A3E',
                                text='Add Product',font=('orbitron',20),
                                relief='raised',
                                borderwidth=1,
                                width=12)
                                                     
        add_button.grid(row=2, column=1, pady=5)

        showing_selected_Label = tk.Label(body_frame25,
                            text='Selected Product:',
                            font=('orbitron',24, BOLD),
                            fg='#B7C304',
                            bg='#116530')
        showing_selected_Label.grid(row=4, column=0, sticky=E+N, pady=8)

        prodnameres_Label = tk.Label(body_frame25,
                            text='Product Name:',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        prodnameres_Label.grid(row=5, column=0, sticky=E+N)

        prodnameres_box = tk.Entry(body_frame25,
                                                              
                            font=('orbitron',23),
                            width=20,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        prodnameres_box.grid(row=5,column=1, sticky=N)

        priceres_Label = tk.Label(body_frame25,
                            text='Product Price:',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        priceres_Label.grid(row=6, column=0, sticky=E+N)

        priceres_box = tk.Entry(body_frame25,
                                                              
                            font=('orbitron',23),
                            width=20,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        priceres_box.grid(row=6,column=1, sticky=N)

        def update():
            pass
            for row in bct.get_children():
                bct.delete(row)
            setprod()
            #tkinter.messagebox.showinfo('Successfull!', 'Product: '+name+', Price: '+str(price)+' added')


        update_button = tk.Button(body_frame25,
                                command=update,
                                fg='#FFCC1D',
                                bg = '#3C4A3E',
                                text='Update Price',font=('orbitron',20),
                                relief='raised',
                                borderwidth=1,
                                width=15)
                                                     
        update_button.grid(row=7, column=1, pady=5)

        def delprod():
            pass
        del_button = tk.Button(body_frame25,
                                text='Delete Product',
                                font=('orbitron',20, BOLD),
                                command= delprod,
                                bg = '#3C4A3E',
                                relief='raised',
                                fg='red',
                                borderwidth = 1,
                                width=16)
        del_button.grid(row=8, column=1,pady=5)
        def Menu():
            controller.show_frame('MenuPage')
        
        menu_button = tk.Button(body_frame25,
                                command=Menu,
                                fg='#FFCC1D',
                                bg = '#3C4A3E',
                                text='Menu',font=('orbitron',20),
                                relief='raised',
                                borderwidth=1,
                                width=5)
                                                     
        menu_button.grid(row=9, column=1, pady=5)