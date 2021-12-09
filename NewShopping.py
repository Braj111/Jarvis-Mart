from tkinter.constants import BOTTOM, CENTER, END, LEFT, RIGHT, TOP, X, Y
from tkinter.font import BOLD
import MongoCommand
import tkinter as tk
from tkinter import ttk



class New_shopping_page(tk.Frame):
    
    
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
                                      text='Shopping',
                                      font=('orbitron',23),
                                      fg='white',
                                      bg='#3d3d5c')
        Enter_Detail_label.pack()

        ##################################################################################
        # Frames
        ##################################################################################

        invoice_frame = tk.Frame(self,
                                 bg='#ff0000')
        invoice_frame.pack(fill= Y, side= LEFT, padx = 15)

        detail_frame = tk.Frame(invoice_frame,
                                 bg='#ff0f00')
        detail_frame.pack(fill= X, padx=20)

        detail_frame1 = tk.Frame(detail_frame, bg='#ff0f00')
        detail_frame1.pack(fill = X)

        detail_frame2 = tk.Frame(detail_frame, bg='#ff0f00')
        detail_frame2.pack(fill = X)


        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        LEFT PACK
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        invoice_label = tk.Label(invoice_frame,
                                      text='Invoice',
                                      font=('orbitron',23),
                                      fg='white',
                                      bg='#3d3d5c')
        invoice_label.pack(fill=X, pady= 5)
        
        invoice_heading = tk.Frame(invoice_frame, bg='#ff0f00')
        invoice_heading.pack(fill = X)       

        Name_Label = tk.Label(detail_frame1,
            text='Custmer\'s Name:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Name_Label.grid(row=0,column=0,pady=5,padx=5)

        Name_box = tk.Entry(detail_frame1,
                                                              
                                                              font=('orbitron',23),
                                                              width=15,borderwidth=2,
                                                              justify='center')
        Name_box.grid(row=0,column=1,pady=5)

        Phone_label = tk.Label(detail_frame1,
            text='Phone:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Phone_label.grid(row=0,column=2,pady=5, padx= 5)


        Phone_box = tk.Entry(detail_frame1,
                                                              
                            font=('orbitron',23),
                            width=12,borderwidth=2,
                            justify= 'center')
        Phone_box.grid(row=0,column=3,pady=5)

        Age_Label = tk.Label(detail_frame2,
            text='Age:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Age_Label.grid(row=0,column=0,pady=5, padx= 5)


        Age_box = tk.Entry(detail_frame2,
                                                              
                                                              font=('orbitron',23),
                                                              width=5,borderwidth=2,
                                                              justify= 'center')
        Age_box.grid(row=0,column=1,pady=5,padx=10)

        Star_Label = tk.Label(detail_frame2,
            text='Star:',
            font=('orbitron',23),
            fg='white',
            bg='#3d3d5c')
        Star_Label.grid(row=0,column=2,pady=5, padx= 5)

        star_box = tk.Entry(detail_frame2,
                                                              
                                                              font=('orbitron',23),
                                                              width=5,borderwidth=2,
                                                              justify= 'center')
        star_box.grid(row=0,column=3,pady=5,padx=10)



        item_Label = tk.Label(invoice_heading,
            text='Items',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        item_Label.grid(row=0,column=0,sticky="ew")

        price_Label = tk.Label(invoice_heading,
            text='Price',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        price_Label.grid(row=0,column=1,sticky="ew")

        qty_Label = tk.Label(invoice_heading,
            text='Quantity',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        qty_Label.grid(row=0,column=2,sticky="ew")

        total_Label = tk.Label(invoice_heading,
            text='Total',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        total_Label.grid(row=0,column=3,sticky="ew")

        languages = {'Python':10, 'JavaScript':20, 'Java':30,
                        'Swift':40, 'GoLang':50, 'C#':60, 'C++':70, 'Scala':80}
        
        # invoice widgits list
        itemscb = []
        priceeb = []
        qtysb = []
        totaleb = []

        # Grand Total function
        def GT():
            print("In GT")
            total = 0
            total_box.delete(0, END)
            GT_box.delete(0, END)
            for price in totaleb:
                if len(price.get()) != 0:
                    total += int(price.get())
                    print(total)
            total_box.insert(0, total)
            discount = 0
            if len(discount_box.get()) != 0:
                discount = int(discount_box.get().replace('-','').replace('%',''))
                discount  = (discount/100) * total
            Gtotal = total - discount
            GT_box.insert(0, '₹'+str(Gtotal))
        
        def qty_changed(row):
            totaleb[row].delete(0,END)
            total = int(priceeb[row].get()) * int(qtysb[row].get())
           
            totaleb[row].insert(0,total)
            GT()
        
        def option_changed(event, row):
            priceeb[row].delete(0,END)
            priceeb[row].insert(0, languages[itemscb[row].get()])
            qty_changed(row)
        
        # ttk style theme choosing
        self.style = ttk.Style(self)
        self.style.theme_use('xpnative')
         
        #############################################################
        # Loop to create the invoce frame
        #############################################################
        for row in range(8):
            for column in range(4):
                if column == 0:
                    cb = tk.StringVar()
                    cb = ttk.Combobox(invoice_heading, textvariable=cb)
                    cb['values'] = ('Python', 'JavaScript', 'Java','Swift', 'GoLang', 'C#', 'C++', 'Scala')
                    cb['state'] = 'readonly'
                    cb.config(justify= CENTER, font=('orbitron',16), width= 17)
                    cb.grid(row=row+1,column=column)
                    cb.bind('<<ComboboxSelected>>', lambda event, x = row: option_changed(event,x))
                    itemscb.append(cb)
                elif column == 1:  
                    pb = tk.Entry(invoice_heading, width=14, justify= 'center', font=('orbitron',18))
                    pb.grid(row=row+1,column=column)
                    priceeb.append(pb)
                elif column == 2:
                    qbvar = tk.StringVar(value=1) 
                    qb = ttk.Spinbox(invoice_heading, from_=0, to= 10,
                                     textvariable= qbvar,
                                     style= 'My.TSpinbox',
                                     command= lambda x = row: qty_changed(x))
                    qb.config(justify= CENTER, font=('orbitron',19),width=15)
                    qb.grid(row=row+1,column=column)
                    #qb.config(justify= CENTER, font=('orbitron',18), width= 10)
                    qtysb.append(qb)
                else:
                    tb = tk.Entry(invoice_heading, width=18, justify= 'center', font=('orbitron',18))
                    tb.grid(row=row+1,column=column)
                    totaleb.append(tb)

        

        total_foot_Label = tk.Label(invoice_heading,
            text='Total',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        total_foot_Label.grid(row=10,column=2,sticky="ew")

        total_box = tk.Entry(invoice_heading, width=16, justify= 'center', font=('orbitron',20))
        total_box.grid(row=10,column=3)

        discount_foot_Label = tk.Label(invoice_heading,
            text='Discount',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        discount_foot_Label.grid(row=11,column=2,sticky="ew")

        discount_box = tk.Entry(invoice_heading, width=16, justify= 'center', font=('orbitron',20))
        discount_box.grid(row=11,column=3)

        GT_foot_Label = tk.Label(invoice_heading,
            text='Grand Total',
            font=('orbitron',20),
            fg='white',
            bg='#000000')
        GT_foot_Label.grid(row=12,column=2,sticky="ew")
    
        GT_box = tk.Entry(invoice_heading, width=16, justify= 'center', font=('orbitron',20))
        GT_box.grid(row=12,column=3)


        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        Right PACK
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        button_frame = tk.Frame(self,
                                 bg='#781D42')
        button_frame.pack(expand=True, fill='both')

        cid_Label = tk.Label(button_frame,
                            text='Customer Id',
                            font=('orbitron',23),
                            fg='white',
                            bg='#3d3d5c')
        cid_Label.pack(fill=X, padx=40, pady=20)

        cid_box = tk.Entry(button_frame,
                                                              
                            font=('orbitron',23),
                            width=8,borderwidth=2,
                            justify= 'center')
        cid_box.pack(fill=X, padx=100, pady=10)

        def validate():
            cid = int(cid_box.get())
            customer = MongoCommand.fetch_by_id(cid)
            Name_box.delete(0, END)
            Name_box.insert(0, customer.Name)
            Age_box.delete(0, END)
            Age_box.insert(0, customer.Age)
            Phone_box.delete(0, END)
            Phone_box.insert(0, customer.Phone)
            discount_box.delete(0, END)
            discount_text = '-'+str(MongoCommand.fetch_discount(customer.star))+'%'
            discount_box.insert(0,discount_text)
            star_box.delete(0, END)
            star_box.insert(0, customer.star)
            GT()
            

        validate_button = tk.Button(button_frame,
                                 text='Validate',font=('orbitron',20),
                                 command= validate,
                                 relief='raised',fg='Green',
                                 borderwidth = 1,
                                 width=10,
                                 )
        validate_button.pack(anchor= CENTER, pady=10)  

        generate_cid_button = tk.Button(button_frame,
                                 text='Generate Customer Id',font=('orbitron',20),
                                 command= validate,
                                 relief='raised',fg='Green',
                                 borderwidth = 1,
                                 )
        generate_cid_button.pack(anchor= CENTER, pady=10)

        generate_invoice_button = tk.Button(button_frame,
                                 text='Generate Invoice',font=('orbitron',23,BOLD),
                                 command= validate,
                                 relief='raised',fg='Green',
                                 borderwidth = 1,
                                 )
        generate_invoice_button.pack(side= BOTTOM,anchor= CENTER, pady=20)       