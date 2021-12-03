from tkinter.constants import ANCHOR, BOTTOM, CENTER, END,FLAT, LEFT, RIGHT, TOP, X, Y

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

        best_customer_label = tk.Label(self,
                                      text='Best Customer',
                                      font=('orbitron',23),
                                      fg='white',
                                      bg='#3d3d5c')
        best_customer_label.pack(fill=X)

        Star_frame = tk.Frame(self,bg='#33334d')
        Star_frame.pack(fill= X)
        star1 = "Nil"
        selectedstar_label = tk.Label(self,
                                      text='Showing '+star1+' star customers',
                                      font=('orbitron',20),
                                      fg='white',
                                      bg='#3d3d5c')
        selectedstar_label.pack(fill=X)
        
        table_frame = tk.Frame(self,bg='#33334d')
        table_frame.pack(fill= X)
        
        star_selector = tk.Frame(Star_frame,bg='#33334d')
        star_selector.pack(side=LEFT)

        update_frame = tk.Frame(Star_frame,bg='#33334d')
        update_frame.pack(side=RIGHT)

        automsg_label = tk.Label(self,
                                      text='Send whatsapp message to the selected customers',
                                      font=('orbitron',20),
                                      fg='white',
                                      bg='#3d3d5c')
        automsg_label.pack(fill=X)

        msgbox_frame = tk.Frame(self, bg='#33334d')
        msgbox_frame.pack(fill= X)

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill= X)
        

        ################################################################
        #   Star selecting frame
        ################################################################
        star_select = tk.Label(star_selector,
                              text='Custmer\'s Above:',
                              font=('orbitron',23),
                              fg='white',
                              bg = '#33334d')
        star_select.grid(row=0,column=0,pady=30)

        customer_type = tk.IntVar()
        star1 = str(customer_type.get())
        #radio button function 
        def fetchbystar(star):
            customer = MongoCommand.fetch_by_star(star)
            for row in bct.get_children():
                bct.delete(row)
            for i in customer:
                bct.insert(parent='',index = tk.END, values= tuple(i.values()))
            dis_entry.delete(0,END)
            dis_entry.insert(0,MongoCommand.fetch_discount(star))
            
        onestar = tk.Radiobutton(star_selector,
                                      text='⭐',
                                      indicatoron=0,
                                      font=('orbitron',23),
                                      bg='#33334d',
                                      foreground="yellow",
                                      command= lambda: fetchbystar(1),
                                      relief = FLAT,
                                      value= 1,
                                      variable=customer_type)                          
        onestar.grid(row=0,column=1)
        twostar = tk.Radiobutton(star_selector,
                                       text='⭐',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       bg='#33334d',
                                       foreground="yellow",
                                       command= lambda: fetchbystar(2),
                                       relief=FLAT,
                                       value= 2,
                                       variable=customer_type)                           
        twostar.grid(row=0,column=2)

        threestar = tk.Radiobutton(star_selector,   
                                       text='⭐',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       command= lambda: fetchbystar(3),
                                       bg='#33334d',
                                       foreground="yellow",
                                       value= 3,
                                       relief=FLAT,
                                       variable=customer_type)                           
        threestar.grid(row=0,column=3)

        fourstar = tk.Radiobutton(star_selector,
                                       text='⭐',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       command= lambda: fetchbystar(4),
                                       bg='#33334d',
                                       foreground="yellow",
                                       value= 4,
                                       relief=FLAT,
                                       variable=customer_type)                           
        fourstar.grid(row=0,column=4)

        fivestar = tk.Radiobutton(star_selector,
                                       text='⭐',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       command= lambda: fetchbystar(5),
                                       bg='#33334d',
                                       foreground="yellow",
                                       value= 5,
                                       relief=FLAT,
                                       variable=customer_type)                           
        fivestar.grid(row=0,column=5)

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
        
        # table style
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 15), rowheight=40)
        style.configure("Treeview.Heading", font=('Calibri', 15,'bold')) 
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        ######################################################################
        # Update Discount frame
        ######################################################################

        dis_label = tk.Label(update_frame,
                                 text='Active Discount: ',
                                 font=('orbitron',23,'bold'),
                                 foreground='#ffffff',
                                 background='#33334d')
        dis_label.grid(column=0,row=0,pady=5)

        dis_entry = tk.Entry(update_frame,
                             font=('orbitron',23),
                             width=5,borderwidth=1)
        dis_entry.grid(column=1,row=0,padx=5)
        
        # update function to update the active discount
        def update():
            discount = int(dis_entry.get())
            MongoCommand.update_discount(customer_type.get(),discount)
            
       
        update_button = tk.Button(update_frame,
                                 text='Update',font=('orbitron',20),
                                 command= update,
                                 relief='raised',fg='red',
                                 borderwidth = 1,
                                 width=10,
                                 )
        update_button.grid(column=2,row=0,padx=5)

        msg_entry = tk.Entry(msgbox_frame,
                             font=('orbitron',23),
                             width=40,borderwidth=3,
                             text = 'Enter message here'
                             )
        msg_entry.pack(fill=X, padx= 25)

        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = tk.Button(button_frame,
                                command=menu,fg='green',
                                text='Menu',font=('orbitron',20),
                                relief='raised',
                                borderwidth=1,
                                width=5,
                                )
        menu_button.pack(side=RIGHT, padx= 10)
        send_button = tk.Button(button_frame,
                                command=menu,fg='green',
                                text='send',font=('orbitron',20),
                                relief='raised',
                                borderwidth=1,
                                width=5,
                                )
        send_button.pack()

