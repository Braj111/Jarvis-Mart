from tkinter.constants import BOTH, CENTER, E, LEFT, N, RIGHT, TOP, X, Y
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

        bct = ttk.Treeview(body_frame1, columns= columns, show='headings',height=8)
       
        bct.column('item', anchor=CENTER)
        bct.column('price', anchor=CENTER)


        bct.heading('item', text='Product Name', anchor=CENTER)
        bct.heading('price', text='Price',anchor=CENTER)

    
        bct.pack(fill= Y, side = LEFT, padx=20, pady= 20)
        def setprod():
            products = MongoCommand.fetch_products()
            for product in products:
                    bct.insert(parent='',index = tk.END, values= tuple(product.values()))
        setprod()

        body_frame25 = tk.Frame(body_frame2, bg='#116530')
        body_frame25.pack(side= TOP,fill=X, expand=True, pady=10)
        #body_frame25.grid_anchor(anchor=CENTER)
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
            tkinter.messagebox.showinfo('inserted!', 'Product: '+name+', Price: '+str(price)+' inserted')


        add_button = tk.Button(body_frame25,
                                command=addprod,
                                fg='#FFCC1D',
                                bg = '#3C4A3E',
                                text='Add Product',font=('orbitron',20),
                                relief='raised',
                                borderwidth=1,
                                width=12)
                                                     
        add_button.grid()

        def Menu():
            controller.show_frame('MenuPage')
        
        menu_button = tk.Button(body_frame2,
                                command=Menu,
                                fg='#FFCC1D',
                                bg = '#3C4A3E',
                                text='Menu',font=('orbitron',20),
                                relief='raised',
                                borderwidth=1,
                                width=5)
                                                     
        menu_button.pack()