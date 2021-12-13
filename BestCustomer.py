from tkinter.constants import ANCHOR, BOTH, BOTTOM, CENTER, END,FLAT, LEFT, RIGHT, TOP, X, Y
from tkinter.font import BOLD
import MongoCommand
import tkinter as tk
from  tkinter import Toplevel, ttk
import tkinter.messagebox
from whatauto import whatsappautomation


class best_customer_page(tk.Frame):
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#0B4619')
        self.controller = controller

        #################################################################
        # Frames and Label
        #################################################################
        heading_label = tk.Label(self,
                                 text='Customer-Management-System',
                                 font=('orbitron',45,'bold'),
                                 foreground='#FFCC1D',
                                 background='#0B4619')
        heading_label.pack(pady=25)

        best_customer_label = tk.Label(self,
                                      text='Best Customer',
                                      font=('orbitron',23, BOLD),
                                      fg='#B7C304',
                                      bg='#0B4619')
        best_customer_label.pack(fill=X)

        Star_frame = tk.Frame(self,bg='#116530')
        Star_frame.pack(fill= X)
        selectedstar_label = tk.Label(self,
                                      text='Select stars to see customer list',
                                      font=('orbitron',20),
                                      fg='white',
                                      bg='#0B4619')
        selectedstar_label.pack(fill=X)
        
        table_frame = tk.Frame(self,bg='#116530')
        table_frame.pack(fill= X)
        
        star_selector = tk.Frame(Star_frame,bg='#116530')
        star_selector.pack(side=LEFT)

        update_frame = tk.Frame(Star_frame,bg='#116530')
        update_frame.pack(side=RIGHT)

        automsg_label = tk.Label(self,
                                      text='Send whatsapp message to the selected customers',
                                      font=('orbitron',20),
                                      fg='white',
                                      bg='#0B4619')
        automsg_label.pack(fill=X)

        msgbox_frame = tk.Frame(self, bg='#116530')
        msgbox_frame.pack(fill= X)

        button_frame = tk.Frame(self, bg='#116530')
        button_frame.pack(fill= BOTH, expand= True)
        

        ################################################################
        #   Star selecting frame
        ################################################################
        star_select = tk.Label(star_selector,
                              text='Custmer star:',
                              font=('orbitron',23),
                              fg='white',
                              bg = '#116530')
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
            dis = str(MongoCommand.fetch_discount(star))+'%'
            dis_entry.insert(0, dis)
            selectedstar_label.configure(text="Showing "+str(star)+" star customers")
            
        onestar = tk.Radiobutton(star_selector,
                                      text='★',
                                      indicatoron=0,
                                      font=('orbitron',23),
                                      bg='#0B4619',
                                      foreground="#FFCC1D",
                                      command= lambda: fetchbystar(1),
                                      relief = FLAT,
                                      value= 1,
                                      variable=customer_type)                          
        onestar.grid(row=0,column=1, ipadx = 10)
        twostar = tk.Radiobutton(star_selector,
                                       text='★',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       bg='#0B4619',
                                       foreground="#FFCC1D",
                                       command= lambda: fetchbystar(2),
                                       relief=FLAT,
                                       value= 2,
                                       variable=customer_type)                           
        twostar.grid(row=0,column=2, ipadx = 10)

        threestar = tk.Radiobutton(star_selector,   
                                       text='★',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       command= lambda: fetchbystar(3),
                                       bg='#0B4619',
                                       foreground="#FFCC1D",
                                       value= 3,
                                       relief=FLAT,
                                       variable=customer_type)                           
        threestar.grid(row=0,column=3, ipadx = 10)

        fourstar = tk.Radiobutton(star_selector,
                                       text='★',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       command= lambda: fetchbystar(4),
                                       bg='#0B4619',
                                       fg="#FFCC1D",
                                       value= 4,
                                       relief=FLAT,
                                       variable=customer_type)                           
        fourstar.grid(row=0,column=4, ipadx = 10)

        fivestar = tk.Radiobutton(star_selector,
                                       text='★',
                                       indicatoron=0,
                                       font=('orbitron',23),
                                       command= lambda: fetchbystar(5),
                                       bg='#0B4619',
                                       foreground="#FFCC1D",
                                       value= 5,
                                       relief=FLAT,
                                       variable=customer_type)                           
        fivestar.grid(row=0,column=5, ipadx = 10)

        ################################################################
        #   Table frame
        ################################################################
        self.style = ttk.Style(self)
        self.style.theme_use("xpnative")
        self.style.map("Treeview")
        self.style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 15), rowheight=40)
        self.style.configure("Treeview.Heading", font=('Calibri', 15,'bold'), background='black', foreground='dark blue') 
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

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
        
        

        ######################################################################
        # Update Discount frame
        ######################################################################

        dis_label = tk.Label(update_frame,
                                 text='Active Discount:',
                                 font=('orbitron',23),
                                 foreground='#ffffff',
                                 background='#116530')
        dis_label.grid(column=0,row=0,pady=5)

        dis_entry = tk.Entry(update_frame,
                             font=('orbitron',23),
                             width=5,borderwidth=1,
                             bg='#E8E8CC',
                             justify=CENTER)
        dis_entry.grid(column=1,row=0,padx=5)
        
        # update function to update the active discount
        def update():
            discount = int(dis_entry.get().replace('%',''))
            MongoCommand.update_discount(customer_type.get(),discount)
            tkinter.messagebox.showinfo('Update', 'Discount Updated.')
       
        update_button = tk.Button(update_frame,
                                 text='Update',font=('orbitron',21,BOLD),
                                 command= update,
                                 relief='raised',fg='#3C4A3E',
                                 bg='#FFCC1D',
                                 borderwidth = 1,
                                 width=9,
                                 )
        update_button.grid(column=2,row=0,padx=5)

        msg_entry = tk.Entry(msgbox_frame,
                             font=('orbitron',23),
                             width=40,borderwidth=3,
                             text = 'Enter message here',
                             bg='#E8E8CC',
                             justify=CENTER
                             )
        msg_entry.pack(fill=X, padx= 45, pady=20)
        button_frame.grid_anchor(anchor=CENTER)
        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = tk.Button(button_frame,
                                command=menu,fg='#FFCC1D',
                                bg = '#3C4A3E',
                                text='Menu',font=('orbitron',20),
                                relief='raised',
                                borderwidth=1,
                                width=5)
        menu_button.grid(row = 0, column=1, padx=10, sticky='nsew')

        ############################################################################
        # Whatsapp automation to send message
        ############################################################################
       
        def send():
            raw_message = msg_entry.get()
            data = MongoCommand.fetch_by_star(customer_type.get())
            for user in data:
                message = raw_message.replace("@name", user['Name']).replace('@star', str(user['star']))
                #print(message)
                whatsappautomation(user['Phone'], message)
            msg_entry.delete(0,END)
            tkinter.messagebox.showinfo('Sent', 'Message sent to the selected customers')

        send_button = tk.Button(button_frame,
                                command=send,fg='#3C4A3E',
                                bg='#FFCC1D',
                                text='Send',font=('orbitron',20, BOLD),
                                relief='raised',
                                borderwidth=1,
                                width=8,
                                )
        send_button.grid(row = 0, column= 0,padx=10, sticky='nsew')


