import MongoCommand
import tkinter as tk


class Insert_detail_page(tk.Frame):
    
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
            text='Enter The Details You Want to Insert',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Enter_Detail_label.pack()

        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

            
        Name_Label = tk.Label(button_frame,
            text='Custmer\'s Name:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Name_Label.grid(row=0,column=0,pady=5)

        Age_Label = tk.Label(button_frame,
            text='Customer\'s Age:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Age_Label.grid(row=1,column=0,pady=5)

        Phone_Label = tk.Label(button_frame,
            text='Customer\' Mobile Number: ',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Phone_Label.grid(row=2,column=0,pady=5)
        
        Amount_Label = tk.Label(button_frame,
                                                           text='Customer\'s Shopping Amount:',
                                                           font=('orbitron',23),
                                                           fg='white',
                                                           bg='#3d3d5c')
        Amount_Label.grid(row=3,column=0,pady=5)

        freq_Label = tk.Label(button_frame,
                                                           text='Customer\'s Visiting Frequency:',
                                                           font=('orbitron',23),
                                                           fg='white',
                                                           bg='#3d3d5c')
        freq_Label.grid(row=4,column=0,pady=5)

        
        Name_box = tk.Entry(button_frame,
                                                              
                                                              font=('orbitron',23),
                                                              width=22,borderwidth=2)
        Name_box.grid(row=0,column=1,pady=5)

       
        Age_box = tk.Entry(button_frame,
                                                              
                                                              font=('orbitron',23),
                                                              width=22,borderwidth=2)
        Age_box.grid(row=1,column=1,pady=5)
        
        Phone_box = tk.Entry(button_frame,
                                                             
                                                              font=('orbitron',23),
                                                              width=22,borderwidth=2)
        Phone_box.grid(row=2,column=1,pady=5)
       
        Amount_box = tk.Entry(button_frame,
                                                              
                                                              font=('orbitron',23),
                                                              width=22,borderwidth=2)
        Amount_box.grid(row=3,column=1,pady=5)
        
        freq_box = tk.Entry(button_frame,
                                                              
                                                              font=('orbitron',23),
                                                              width=22,borderwidth=2)
        freq_box.grid(row=4,column=1,pady=5)

        def insert():
            name_cust = str(Name_box.get())
            age_cust = int(Age_box.get())
            phone_cust = int(Phone_box.get())
            amount_cust = int(Amount_box.get())
            freq_cust = int(freq_box.get())
            MongoCommand.add_cust(name_cust,age_cust,phone_cust,amount_cust,freq_cust)

            Conf_Label = tk.Label(button_frame,
                                                           text='Data Sucessfully inserted',
                                                           font=('orbitron',23),
                                                           fg='white',
                                                           bg='#3d3d5c')
            Conf_Label.grid(row=7,column=1,pady=5)
            #controller.show_frame('MenuPage')
            #Name_box.set('')
            #Age_box.set('')
            #Phone_box.set('')
            #Amount_box.set('')
            #freq_box.set('')
            
            

        Insert_button = tk.Button(button_frame,
                                                     text='Insert',font=('orbitron',20),
                                                     command=insert,
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
