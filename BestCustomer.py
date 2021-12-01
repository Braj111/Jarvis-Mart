from tkinter.constants import CENTER, X
import MongoCommand
import tkinter as tk
from  tkinter import ttk


class best_customer_page(tk.Frame):
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        #################################################################
        # Frames and Label
        #################################################################
        heading_label = tk.Label(self,
                                 text='Customer-Management-System',
                                 font=('orbitron',45,'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        Enter_Detail_label = tk.Label(self,
                                      text='Best Customer',
                                      font=('orbitron',23),
                                      fg='white',
                                      bg='#3d3d5c')
        Enter_Detail_label.pack()

        Star_frame = tk.Frame(self,bg='#33334d')
        Star_frame.pack(fill= X)
        
        table_frame = tk.Frame(self,bg='#33334d')
        table_frame.pack(fill= X)
        
        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        ################################################################
        #   Star selecting frame
        ################################################################
        star_select = tk.Label(Star_frame,
                              text='Custmer\'s Above:',
                              font=('orbitron',23),
                              fg='white',
                              bg='#3d3d5c')
        star_select.grid(row=0,column=0,pady=5)

        customer_type = tk.IntVar(Star_frame, 1)
        def onestar():
            customer = MongoCommand.fetch_by_star(2)
            for i in customer:
                bct.insert(parent='',index = tk.END, values= tuple(i.values()))
        onestar = tk.Radiobutton(Star_frame,
                                      text='⭐',
                                      indicatoron=0,
                                      font=('orbitron',23),
                                      bg='#33334d',
                                      command=onestar,
                                      relief='flat',
                                      value= 1,
                                      variable=customer_type)                          
        onestar.grid(row=0,column=1,padx=25)
        twostar = tk.Radiobutton(Star_frame,
                                       text='⭐⭐',
                                       font=('orbitron',23),
                                       bg='#33334d',
                                       value= 2,
                                       variable=customer_type)                           
        twostar.grid(row=0,column=2,padx=10)

        threestar = tk.Radiobutton(Star_frame,
                                       text='⭐⭐⭐',
                                       font=('orbitron',23),
                                       bg='#33334d',
                                       value= 3,
                                       variable=customer_type)                           
        threestar.grid(row=0,column=3,padx=10)

        fourstar = tk.Radiobutton(Star_frame,
                                       text='⭐⭐⭐⭐',
                                       font=('orbitron',23),
                                       bg='#33334d',
                                       value= 4,
                                       variable=customer_type)                           
        fourstar.grid(row=0,column=4,padx=10)

        fivestar = tk.Radiobutton(Star_frame,
                                       text='⭐⭐⭐⭐⭐',
                                       font=('orbitron',23),
                                       bg='#33334d',
                                       value= 5,
                                       variable=customer_type)                           
        fivestar.grid(row=0,column=5,padx=10)

        ################################################################
        #   Table frame
        ################################################################
        columns = ('_id','cust_name', 'cust_age', 'cust_phone','total_shopping','freq')
        bct = ttk.Treeview(table_frame, columns= columns, show='headings',height=8)


        bct.heading('_id', text='Customer ID', anchor=CENTER)
        bct.heading('cust_name', text='Name',anchor=CENTER)
        bct.heading('cust_age', text='Age',anchor=CENTER)
        bct.heading('cust_phone', text='Phone',anchor=CENTER)
        bct.heading('total_shopping', text='Total shopping',anchor=CENTER)
        bct.heading('freq', text='Shopping Frequency',anchor=CENTER)
        bct.pack()
        
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")


        Insert_button = tk.Button(button_frame,
                                 text='Insert',font=('orbitron',20),
                                 
                                 relief='raised',fg='red',
                                 borderwidth = 1,
                                 width=20,
                                 )
        Insert_button.grid(row=5,column=1,pady=5)

        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = tk.Button(button_frame,
                                command=menu,fg='green',
                                text='Menu',font=('orbitron',20),
                                relief='raised',
                                borderwidth=1,
                                width=20,
                                )
        menu_button.grid(row=6,column=1,pady=5)

