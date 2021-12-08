import tkinter as tk
from tkinter.constants import BOTTOM

#=========================
#Creating Menu Page======
#=========================


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
   
        heading_label = tk.Label(self,
                                 text='Customer-Management-System',
                                 font=('orbitron',45,'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('orbitron',20),
                                   fg='white',
                                   bg='#3d3d5c')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='Please make a selection',
                                   font=('orbitron',18),
                                   fg='white',
                                   bg='#3d3d5c',
                                   anchor='w')
        selection_label.pack()

        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        def insert_detail_page():
            controller.show_frame('Insert_detail_page')
            
        withdraw_button = tk.Button(button_frame,
                                    text='Insert Customer Detail',
                                    command=insert_detail_page,
                                    relief='raised',
                                    font=('orbitron',12),
                                    borderwidth=3,
                                    width=50,
                                    height=3)
        withdraw_button.pack()

        def New_shopping_page():
            controller.show_frame('New_shopping_page')
            
        Search_Student_Detail_button = tk.Button(button_frame,
                                                text='Shopping',
                                                command= New_shopping_page,
                                                font=('orbitron',12),
                                                relief='raised',
                                                borderwidth=3,
                                                width=50,
                                                height=3)
        Search_Student_Detail_button.pack()
        

        def best_customer_page():
            controller.show_frame('best_customer_page')
            
        Update_button = tk.Button(button_frame,
                                    text='Best Customer',
                                    command=best_customer_page,
                                    font=('orbitron',12),
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=3)
        Update_button.pack()

        def Delete_Entry():
            controller.show_frame('delete_customer')
            
        delete_student_button = tk.Button(button_frame,
                                            text='Delete Customer details',font=('orbitron',12),
                                            command=Delete_Entry,
                                            relief='raised',
                                            borderwidth=3,
                                            width=50,
                                            height=3)
        delete_student_button.pack()


        def Display_All_detail():
            controller.show_frame('find_customer')
        
        display_detail_button = tk.Button(button_frame,
                                            text='Find Customer',font=('orbitron',12),
                                            command=Display_All_detail,
                                            relief='raised',
                                            borderwidth=3,
                                            width=50,
                                            height=3)
        display_detail_button.pack()

        def exit():
            controller.show_frame('StartPage')
        exit_button = tk.Button(button_frame,
                                text='Exit',font=('orbitron',12),
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=3)
        exit_button.pack()

