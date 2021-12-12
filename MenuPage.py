import tkinter as tk
from tkinter.constants import BOTTOM
from tkinter.font import BOLD

#=========================
#Creating Menu Page=======
#=========================


class MenuPage(tk.Frame):

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
                                                font=('orbitron',15,BOLD),
                                                fg='#FFCC1D',
                                                bg = '#3C4A3E',
                                                relief='flat',                                
                                                width=50,
                                                height=3)
        newshopping_button.pack(pady=1)
        

        def best_customer_page():
            controller.show_frame('best_customer_page')
            
        Update_button = tk.Button(button_frame,
                                    text='Best Customer',
                                    command=best_customer_page,
                                    font=('orbitron',15,BOLD),
                                    fg='#FFCC1D',
                                    bg = '#3C4A3E',
                                    relief='flat',                  
                                    width=50,
                                    height=3)
        Update_button.pack(pady=1)

        # def Delete_Entry():
        #     controller.show_frame('delete_customer')
            
        # delete_student_button = tk.Button(button_frame,
        #                                     text='Delete Customer details',
        #                                     command=Delete_Entry,
        #                                     font=('orbitron',15,BOLD),
        #                                     fg='#FFCC1D',
        #                                     bg = '#3C4A3E',
        #                                     relief='flat',                           
        #                                     width=50,
        #                                     height=3)
        # delete_student_button.pack(pady=1)


        def Display_All_detail():
            controller.show_frame('find_customer')
        
        display_detail_button = tk.Button(button_frame,
                                            text='Find Customer',
                                            command=Display_All_detail,
                                            font=('orbitron',15,BOLD),
                                            fg='#FFCC1D',
                                            bg = '#3C4A3E',
                                            relief='flat',                               
                                            width=50,
                                            height=3)
        display_detail_button.pack(pady=1)

        def exit():
            parent.quit()
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                font=('orbitron',15,BOLD),
                                fg='Red',
                                bg = '#3C4A3E',
                                relief='flat',
                    
                                width=50,
                                height=3)
        exit_button.pack(pady=1)

