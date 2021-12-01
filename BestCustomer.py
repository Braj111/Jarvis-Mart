from tkinter.constants import ANCHOR, CENTER, X
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

        customer_type = tk.IntVar()
        #radio button function 
        def fetchbystar(star):
            customer = MongoCommand.fetch_by_star(star)
            for row in bct.get_children():
                bct.delete(row)
            for i in customer:
                bct.insert(parent='',index = tk.END, values= tuple(i.values()))
            
        onestar = tk.Radiobutton(Star_frame,
                                      text='⭐',
                                      indicatoron=0,
                                      font=('orbitron',23),
                                      bg='#33334d',
                                      foreground="yellow",
                                      command= lambda: fetchbystar(1),
                                      relief='flat',
                                      value= 1,
                                      variable=customer_type)                          
        onestar.grid(row=0,column=1,padx=25)
        twostar = tk.Radiobutton(Star_frame,
                                       text='⭐⭐',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       bg='#33334d',
                                       foreground="yellow",
                                       command= lambda: fetchbystar(2),
                                       relief='flat',
                                       value= 2,
                                       variable=customer_type)                           
        twostar.grid(row=0,column=2,padx=10)

        threestar = tk.Radiobutton(Star_frame,
                                       text='⭐⭐⭐',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       command= lambda: fetchbystar(3),
                                       bg='#33334d',
                                       foreground="yellow",
                                       value= 3,
                                       variable=customer_type)                           
        threestar.grid(row=0,column=3,padx=10)

        fourstar = tk.Radiobutton(Star_frame,
                                       text='⭐⭐⭐⭐',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       command= lambda: fetchbystar(4),
                                       bg='#33334d',
                                       foreground="yellow",
                                       value= 4,
                                       variable=customer_type)                           
        fourstar.grid(row=0,column=4,padx=10)

        fivestar = tk.Radiobutton(Star_frame,
                                       text='⭐⭐⭐⭐⭐',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       command= lambda: fetchbystar(5),
                                       bg='#33334d',
                                       foreground="yellow",
                                       value= 5,
                                       variable=customer_type)                           
        fivestar.grid(row=0,column=5,padx=10)

        ################################################################
        #   Table frame
        ################################################################
        columns = ('_id','cust_name', 'cust_age', 'cust_phone','freq','total_shopping')

        bct = ttk.Treeview(table_frame, columns= columns, show='headings',height=8)
       
        bct.column('_id', anchor=CENTER)
        bct.column('cust_name', anchor=CENTER)
        bct.column('cust_age', anchor=CENTER)
        bct.column('cust_phone', anchor=CENTER)
        bct.column('freq', anchor=CENTER)
        bct.column('total_shopping',anchor=CENTER)

        bct.heading('_id', text='Customer ID', anchor=CENTER)
        bct.heading('cust_name', text='Name',anchor=CENTER)
        bct.heading('cust_age', text='Age',anchor=CENTER)
        bct.heading('cust_phone', text='Phone',anchor=CENTER)
        bct.heading('freq', text='No. of visits',anchor=CENTER)
        bct.heading('total_shopping', text='Total shopping',anchor=CENTER)
        bct.pack(fill= X)
        
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 15), rowheight=40) # Modify the font of the body
        #style.configure("Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        #style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders




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

