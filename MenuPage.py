import tkinter as tk
from tkinter.constants import BOTTOM
from tkinter.font import BOLD
import pymongo

#=========================
#Creating Menu Page=======
#=========================


class MenuPage(tk.Frame):
    #Mongo Connection
    client = pymongo.MongoClient("mongodb+srv://harsh8833:harsh8833@cluster0.9hs91.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["g10"]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#0B4619')
        self.controller = controller
   
        heading_label = tk.Label(self,
                                 text='Customer-Management-System',
                                 font=('orbitron',45,'bold'),
                                 foreground='#FFCC1D',
                                 background='#0B4619')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('orbitron',20,BOLD),
                                   fg='#B7C304',
                                   bg='#0B4619')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='Please make a selection',
                                   font=('orbitron',18),
                                   fg='white',
                                   bg='#0B4619',
                                   anchor='w')
        selection_label.pack()

        button_frame = tk.Frame(self,bg='#116530')
        button_frame.pack(fill='both',expand=True)


        def New_shopping_page():
            controller.show_frame('New_shopping_page')
            
        newshopping_button = tk.Button(button_frame,
                                                text='New Shopping',
                                                command= New_shopping_page,
                                                font=('orbitron',18,BOLD),
                                                fg='#FFCC1D',
                                                bg = '#3C4A3E',
                                                relief='flat',                                
                                                width=40,
                                                height=2)
        newshopping_button.pack(pady=1)
        

        def best_customer_page():
            controller.show_frame('best_customer_page')
            
        Update_button = tk.Button(button_frame,
                                    text='Best Customer',
                                    command=best_customer_page,
                                    font=('orbitron',18,BOLD),
                                    fg='#FFCC1D',
                                    bg = '#3C4A3E',
                                    relief='flat',                  
                                    width=40,
                                    height=2)
        Update_button.pack(pady=1)

        def invohis():
            controller.show_frame('invoice_history')
            
        invoice_history_button = tk.Button(button_frame,
                                            text='Invoice History',
                                            command=invohis,
                                            font=('orbitron',18,BOLD),
                                            fg='#FFCC1D',
                                            bg = '#3C4A3E',
                                            relief='flat',                           
                                            width=40,
                                            height=2)
        invoice_history_button.pack(pady=1)


        def find_customer():
            controller.show_frame('find_customer')
        
        find_customer_button = tk.Button(button_frame,
                                            text='Find Customer',
                                            command=find_customer,
                                            font=('orbitron',18,BOLD),
                                            fg='#FFCC1D',
                                            bg = '#3C4A3E',
                                            relief='flat',                               
                                            width=40,
                                            height=2)
        find_customer_button.pack(pady=1)

        def prod_page():
            controller.show_frame('find_customer')
        
        find_customer_button = tk.Button(button_frame,
                                            text='Manage Products',
                                            command=prod_page,
                                            font=('orbitron',18,BOLD),
                                            fg='#FFCC1D',
                                            bg = '#3C4A3E',
                                            relief='flat',                               
                                            width=40,
                                            height=2)
        find_customer_button.pack(pady=1)

        def exit():
            parent.quit()
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                font=('orbitron',18,BOLD),
                                fg='Red',
                                bg = '#3C4A3E',
                                relief='flat',
                    
                                width=40,
                                height=2)
        exit_button.pack(pady=1)

