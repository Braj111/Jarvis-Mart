from tkinter.constants import BOTH, BOTTOM, CENTER, LEFT, RIGHT, TOP, X
import MongoCommand
import tkinter as tk
from tkinter import ttk


class invoice_generator_page(tk.Frame):
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        serial_number = 0
        Total_count = []
        total_label = tk.IntVar()


        heading_label = tk.Label(self,
                                 text='Customer-Management-System',
                                 font=('orbitron',45,'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        Enter_Detail_label = tk.Label(self,
                                      text='Invoice Generator',
                                      font=('orbitron',23),
                                      fg='white',
                                      bg='#3d3d5c')
        Enter_Detail_label.pack()
        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)


        button_frame_0 = tk.Frame(button_frame,bg='#33334d')
        button_frame_0.pack(fill='both',expand=False)
        columns = ('s_no','item', 'qty', 'price','total')

        bct = ttk.Treeview(button_frame_0, columns= columns, show='headings',height=8)
       
        bct.column('s_no', anchor=CENTER)
        bct.column('item', anchor=CENTER)
        bct.column('qty', anchor=CENTER)
        bct.column('price', anchor=CENTER)
        bct.column('total', anchor=CENTER)

        bct.heading('s_no', text='S.no', anchor=CENTER)
        bct.heading('item', text='Item',anchor=CENTER)
        bct.heading('qty', text='Qty',anchor=CENTER)
        bct.heading('price', text='Price',anchor=CENTER)
        bct.heading('total', text='Total',anchor=CENTER)
        bct.pack(fill= X)
        
        # table style
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 15), rowheight=40)
        style.configure("Treeview.Heading", font=('Calibri', 15,'bold')) 
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        button_frame_0_0 = tk.Frame(button_frame_0,bg='#33334d')
        button_frame_0_0.pack(side=RIGHT)
        Name_Label = tk.Label(button_frame_0_0,
                              text='Total:',
                              font=('orbitron',23),
                              fg='white',
                              bg='#3d3d5c')
        Name_Label.grid(row=0,column=0,pady=5)
        Name_Label = tk.Label(button_frame_0_0,
                              textvariable=total_label,
                              font=('orbitron',23),
                              width=7,
                              fg='white',
                              bg='#3d3d5c')
        Name_Label.grid(row=0,column=1,pady=5)
        
        button_frame_1 = tk.Frame(button_frame,bg='#33334d')
        button_frame_1.pack(fill='both',expand=False)

        button_frame_2 = tk.Frame(button_frame_1,bg='#33334d')
        button_frame_2.pack(side=TOP,fill=BOTH)

        Name_Label = tk.Label(button_frame_2,
                              text='S.No',
                              font=('orbitron',23),
                              fg='white',
                              bg='#3d3d5c')
        Name_Label.grid(row=0,column=0,pady=5)

        Age_Label = tk.Label(button_frame_2,
                             text='Item',
                             font=('orbitron',23),
                             fg='white',
                             bg='#3d3d5c')
        Age_Label.grid(row=0,column=1,pady=5)

        Phone_Label = tk.Label(button_frame_2,
                               text='Qty',
                               font=('orbitron',23),
                               fg='white',
                               bg='#3d3d5c')
        Phone_Label.grid(row=0,column=2,pady=5)
        
        Amount_Label = tk.Label(button_frame_2,
                                text='Price',
                                font=('orbitron',23),
                                fg='white',
                                bg='#3d3d5c')
        Amount_Label.grid(row=0,column=3,pady=5)

        freq_Label = tk.Label(button_frame_2,
                              text='Total',
                              font=('orbitron',23),
                              fg='white',
                              bg='#3d3d5c')
        freq_Label.grid(row=0,column=4,pady=5)
        
        sno = tk.StringVar()
        item = tk.StringVar()
        qty = tk.StringVar()
        price = tk.StringVar()
        total = tk.StringVar()
        


        Name_box = tk.Entry(button_frame_2,                                                      
                             font=('orbitron',23),
                             textvariable=sno,
                             width=2,borderwidth=2)
        Name_box.grid(row=1,column=0,pady=5)

       
        Age_box = tk.Entry(button_frame_2,                                       
                           font=('orbitron',23),
                           textvariable=item,
                           width=10,borderwidth=2)
        Age_box.grid(row=1,column=1,pady=5)
        
        Phone_box = tk.Entry(button_frame_2,
                             font=('orbitron',23),
                             textvariable=qty,
                             width=5,borderwidth=2)
        Phone_box.grid(row=1,column=2,pady=5)
       
        Amount_box = tk.Entry(button_frame_2,   
                              font=('orbitron',23),
                              textvariable=price,
                              width=5,borderwidth=2)
        Amount_box.grid(row=1,column=3,pady=5)
        
        
        freq_box = tk.Entry(button_frame_2,                                                             
                            font=('orbitron',23),
                            textvariable=total,
                            width=8,borderwidth=2)
        freq_box.grid(row=1,column=4,pady=5)

        def insert_tree():
            s_no=str(sno.get())
            item_=str(item.get())
            qty_=str(qty.get())
            price_=str(price.get())
            total_=str(total.get())
            if s_no!='' and item_!='' and qty_!=''and price_!='' and total_!='':
                Total_count.append(int(total_))
                data=(s_no,item_,qty_,price_,total_)
                bct.insert(parent='',index = tk.END, values= data)
            total_label.set(sum(Total_count))
            sno.set('')
            qty.set('')
            item.set('')
            price.set('')
            total.set('')
            

        Insert_button = tk.Button(button_frame_1,
                                 text='Insert',font=('orbitron',20),
                                 command=insert_tree,
                                 relief='raised',fg='red',
                                 borderwidth = 1,
                                 width=5,
                                 )
        Insert_button.pack(side=LEFT)
        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = tk.Button(button_frame_1,
                                                    command=menu,fg='green',
                                                    text='Menu',font=('orbitron',20),
                                                    relief='raised',
                                                    borderwidth=1,
                                                    width=5,
                                                    )
        menu_button.pack(side=LEFT)

        menu_button = tk.Button(button_frame,
                                                    command=menu,fg='red',
                                                    text='Generate',font=('orbitron',20),
                                                    relief='raised',
                                                    borderwidth=2,
                                                    width=20,
                                                    height=5
                                                    )
        menu_button.pack(side=BOTTOM)

