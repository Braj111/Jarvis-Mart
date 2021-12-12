from tkinter.constants import CENTER, E, END, LEFT, RIGHT, W, X, Y, YES
from tkinter.font import BOLD
import MongoCommand
import tkinter as tk
import tkinter.messagebox

class find_customer(tk.Frame):
    
    
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
                                   text='Search Customer',
                                   font=('orbitron',21,BOLD),
                                   fg='#B7C304',
                                   bg='#0B4619')
        searchcustomer_label.pack()

        body_frame2 = tk.Frame(self,bg='#116530')
        body_frame2.pack(side=RIGHT,fill=Y,expand=True)

        body_frame1 = tk.Frame(self,bg='#116530')
        body_frame1.pack(side=LEFT,fill=Y,expand=True, ipadx=100)

        body_frame1.grid_anchor(anchor=CENTER)

        cid_Label = tk.Label(body_frame1,
                            text='Customer Id:',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        cid_Label.grid(row=0, column=0, sticky=E)

        cid_box = tk.Entry(body_frame1,
                                                              
                            font=('orbitron',23),
                            width=20,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        cid_box.grid(row=0, column=1,sticky=W)
        
        name_Label = tk.Label(body_frame1,
                            text='Name:',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        name_Label.grid(row=1, column=0, sticky= 'e')

        name_box = tk.Entry(body_frame1,
                                                              
                            font=('orbitron',23),
                            width=20,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        name_box.grid(row=1, column=1)
        
        age_Label = tk.Label(body_frame1,
                            text='Age:',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        age_Label.grid(row=2, column=0, sticky= E)

        age_box = tk.Entry(body_frame1,
                                                              
                            font=('orbitron',23),
                            width=20,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        age_box.grid(row=2, column=1,sticky=W)

        phone_Label = tk.Label(body_frame1,
                            text='Phone:',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        phone_Label.grid(row=3, column=0, sticky= E)

        phone_box = tk.Entry(body_frame1,
                                                              
                            font=('orbitron',23),
                            width=20,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        phone_box.grid(row=3, column=1,sticky=W)

        star_Label = tk.Label(body_frame1,
                            text='Star:',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        star_Label.grid(row=4, column=0, sticky= E)

        star_box = tk.Entry(body_frame1,
                                                              
                            font=('orbitron',23),
                            width=20,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        star_box.grid(row=4, column=1,sticky=W)

        amt_Label = tk.Label(body_frame1,
                            text='Total Shopping:',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        amt_Label.grid(row=5, column=0, sticky= E)

        amt_box = tk.Entry(body_frame1,
                                                              
                            font=('orbitron',23),
                            width=20,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        amt_box.grid(row=5, column=1,sticky=W)

        freq_Label = tk.Label(body_frame1,
                            text='Frequency:',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        freq_Label.grid(row=6, column=0, sticky= E)

        freq_box = tk.Entry(body_frame1,
                                                              
                            font=('orbitron',23),
                            width=20,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        freq_box.grid(row=6, column=1,sticky=W)

        ##################################################################################
        # Right Frame
        ##################################################################################

        custid_Label = tk.Label(body_frame2,
                            text='Find by Customer Id',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        custid_Label.pack(fill=X, padx=40, pady=20)

        custid_box = tk.Entry(body_frame2,
                                                              
                            font=('orbitron',23),
                            width=8,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        custid_box.pack(fill=X, padx=100, pady=10)
        
        # clear all the field
        def clear():
            cid_box.delete(0,END)
            name_box.delete(0,END)
            age_box.delete(0,END)
            phone_box.delete(0,END)
            amt_box.delete(0,END)
            freq_box.delete(0,END)
            star_box.delete(0,END)
        
        # put data in the boxes
        def setdata(customer):
            cid_box.insert(0,customer._id)
            name_box.insert(0,customer.Name)
            age_box.insert(0,customer.Age)
            phone_box.insert(0,customer.Phone)
            amt_box.insert(0,customer.Amount)
            freq_box.insert(0,customer.Frequency)
            star_box.insert(0,customer.star)
        
        def findid():
            customer = MongoCommand.fetch_by_id(int(custid_box.get()))
            clear()
            setdata(customer)
            

        find_button = tk.Button(body_frame2,
                                 text='Find by id',font=('orbitron',20),
                                 command= findid,
                                 bg = '#3C4A3E',
                                 relief='raised',fg='#FFCC1D',
                                 borderwidth = 1,
                                 width=10,
                                 )
        find_button.pack(anchor= CENTER, pady=10)

        custphone_Label = tk.Label(body_frame2,
                            text='Find by Customer Phone',
                            font=('orbitron',24, BOLD),
                            fg='white',
                            bg='#116530')
        custphone_Label.pack(fill=X, padx=40, pady=20)

        custphone_box = tk.Entry(body_frame2,
                                                              
                            font=('orbitron',23),
                            width=8,borderwidth=2,
                            background='#E8E8CC',
                            justify= 'center')
        custphone_box.pack(fill=X, padx=100, pady=10)

        def findphone():
            customer = MongoCommand.fetch_by_phone(custphone_box.get())
            clear()
            setdata(customer)
            

        find_button = tk.Button(body_frame2,
                                text='Find by phone',
                                font=('orbitron',20),
                                command= findphone,
                                bg = '#3C4A3E',
                                relief='raised',
                                fg='#FFCC1D',
                                borderwidth = 1,
                                width=13)
        find_button.pack(anchor= CENTER, pady=10)

        def deletecus():
            custid_box.delete(0,END)
            ans = tkinter.messagebox.askyesno('Warning!', 'Do you want to Delete this customer?')
            if ans == YES:
                cid = int(cid_box.get())
                MongoCommand.remove_cust(cid)
                tkinter.messagebox.showinfo('Removed', 'Customer id '+str(cid)+' is deleted successfully')
                clear()

        del_button = tk.Button(body_frame2,
                                text='Delete Customer',
                                font=('orbitron',20, BOLD),
                                command= deletecus,
                                bg = '#3C4A3E',
                                relief='raised',
                                fg='red',
                                borderwidth = 1,
                                width=16)
        del_button.pack(anchor= CENTER, pady=10)

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

   