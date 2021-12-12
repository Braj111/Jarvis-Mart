from tkinter.constants import BOTH, CENTER, X
from tkinter.font import BOLD
import MongoCommand
import tkinter as tk
from tkinter import ttk

class invoice_history(tk.Frame):
    
    
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
                                   text='Invoice History',
                                   font=('orbitron',21,BOLD),
                                   fg='#B7C304',
                                   bg='#0B4619')
        searchcustomer_label.pack()

        body_frame = tk.Frame(self, bg='#116530')
        body_frame.pack(fill=BOTH, expand=True)

        ################################################################
        #   Table frame
        ################################################################
        self.style = ttk.Style(self)
        self.style.theme_use("xpnative")
        self.style.map("Treeview")
        self.style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 15), rowheight=80)
        self.style.configure("Treeview.Heading", font=('Calibri', 15,'bold'), background='black', foreground='dark blue') 
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        columns = ('invono','invod', 'cid', 'billamount','discount','items')

        bct = ttk.Treeview(body_frame, columns= columns, show='headings',height=8)
       
        bct.column('invono', anchor=CENTER)
        bct.column('invod', anchor=CENTER)
        bct.column('cid', anchor=CENTER)
        bct.column('billamount', anchor=CENTER)
        bct.column('discount', anchor=CENTER)
        bct.column('items',anchor=CENTER)

        bct.heading('invono', text='Invoice No.', anchor=CENTER)
        bct.heading('invod', text='Customer Id',anchor=CENTER)
        bct.heading('cid', text='Bill Amount',anchor=CENTER)
        bct.heading('billamount', text='Discount',anchor=CENTER)
        bct.heading('discount', text='Items',anchor=CENTER)
        bct.heading('items', text='Invoice Date',anchor=CENTER)
    
        bct.pack(fill= BOTH, expand=True)

        invoices = MongoCommand.fetch_invoice()
        for invoice in invoices:
                bct.insert(parent='',index = tk.END, values= tuple(invoice.values()))




        def Menu():
            controller.show_frame('MenuPage')
        menu_button = tk.Button(body_frame,
                                command=Menu,
                                fg='#FFCC1D',
                                bg = '#3C4A3E',
                                text='Menu',font=('orbitron',20),
                                relief='raised',
                                borderwidth=1,
                                width=5)
                                                     
        menu_button.pack()