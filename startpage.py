import SampleApp
import tkinter as tk

#=========================
#Creating First Page======
#=========================


class StartPage(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Customer Management System')
        self.controller.state('zoomed')
        

        heading_label = tk.Label(self,
                                                     text='Mongodb Connection',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()

        usr_label = tk.Label(self,
                                                      text='Enter your Username',
                                                      font=('orbitron',13),
                                                      bg='#3d3d5c',
                                                      fg='white')
        usr_label.pack()

        my_user = tk.StringVar()
        User_entry_box = tk.Entry(self,
                                                              textvariable=my_user,
                                                              font=('orbitron',12),
                                                              width=22)
        User_entry_box.pack(ipady=7)

        password_label = tk.Label(self,
                                                      text='Enter your password',
                                                      font=('orbitron',13),
                                                      bg='#3d3d5c',
                                                      fg='white')
        password_label.pack(pady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self,
                                                              textvariable=my_password,
                                                              font=('orbitron',12),
                                                              width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)

        def handle_focus_in(_):
            password_entry_box.configure(fg='black',show='*')
            
        password_entry_box.bind('<FocusIn>',handle_focus_in)

        def connect_mongo():
         usr=my_user.get()
         pa=my_password.get()
         #mydb=mysql.connector.connect(host="localhost",port="3306",user=str(usr),passwd=str(pa),database="try")
         #mycursor=mydb.cursor()
         my_password.set('')
         incorrect_Credientials_label['text']=''
         controller.show_frame('MenuPage')

                  
        enter_button = tk.Button(self,
                                                     text='Connect',
                                                     command=connect_mongo,
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=40,
                                                     height=3)
        enter_button.pack(pady=10)

        incorrect_Credientials_label = tk.Label(self,
                                                                        text='',
                                                                        font=('orbitron',13),
                                                                        fg='white',
                                                                        bg='#33334d',
                                                                        anchor='n')
        incorrect_Credientials_label.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

