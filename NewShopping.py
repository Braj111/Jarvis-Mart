from tkinter.constants import BOTTOM, CENTER, END, LEFT, RIGHT, TOP, X, Y
from tkinter.font import BOLD
import MongoCommand
import tkinter as tk
from tkinter import ttk
from whatauto import whatsappautomation
import datetime

class New_shopping_page(tk.Frame):
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#0B4619')
        self.controller = controller


        heading_label = tk.Label(self,
                                 text='Customer-Management-System',
                                 font=('orbitron',45,'bold'),
                                 foreground='#FFCC1D',
                                 background='#0B4619')
        heading_label.pack(pady=25)

        shopping_frame = tk.Frame(self, bg='#0B4619')
        shopping_frame.pack(fill=X,expand=True)
       
        invoice_number_label = tk.Label(shopping_frame,
                                        text='Invoice No.',
                                        font=('orbitron',20),
                                        fg='#E8E8CC',
                                        bg='#0B4619')
        invoice_number_label.pack(side=LEFT)
        invoicenumber = MongoCommand.get_invoice_number()
        invo_no = tk.Label(shopping_frame,
                                text=invoicenumber,
                                font=('orbitron',20),
                                fg='#E8E8CC',
                                bg='#0B4619')
        invo_no.pack(side=LEFT)
        dtn = datetime.datetime.now()
        dtn = dtn.strftime("%d/%m/%Y")
        date_label = tk.Label(shopping_frame,
                                text=dtn,
                                font=('orbitron',20),
                                fg='#E8E8CC',
                                bg='#0B4619')
        date_label.pack(side=RIGHT)

        shopping_label = tk.Label(shopping_frame,
                                      text='New Shopping',
                                      font=('orbitron',23, BOLD),
                                      fg='#B7C304',
                                      bg='#0B4619')
        shopping_label.pack(side = TOP)
    
        ##################################################################################
        # Frames
        ##################################################################################

        invoice_frame = tk.Frame(self,
                                 bg='#116530')
        invoice_frame.pack(fill= Y, side= LEFT, padx = 15)

        detail_frame = tk.Frame(invoice_frame,
                                 bg='#116530')
        detail_frame.pack(fill= X, padx=20)

        detail_frame1 = tk.Frame(detail_frame, bg='#116530')
        detail_frame1.pack(fill = X)

        detail_frame2 = tk.Frame(detail_frame, bg='#116530')
        detail_frame2.pack(fill = X)


        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        LEFT PACK
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        invoice_label = tk.Label(invoice_frame,
                                      text='Invoice',
                                      font=('orbitron',23),
                                      fg='white',
                                      bg='#0B4619')
        invoice_label.pack(fill=X)
        
        invoice_heading = tk.Frame(invoice_frame, bg='#116530')
        invoice_heading.pack(fill = X)       

        Name_Label = tk.Label(detail_frame1,
            text='Custmer\'s Name:',
            font=('orbitron',23),
            fg='white',
            bg='#116530')
        Name_Label.pack(fill= X,side=LEFT,pady=5,padx=5)

        Name_box = tk.Entry(detail_frame1,
                                                              
                                                              font=('orbitron',23),
                                                              width=15,borderwidth=2,
                                                              justify='center',
                                                              background='#E8E8CC')
        Name_box.pack(fill =X,side = RIGHT,padx=5,pady=5, expand= True)

        Phone_label = tk.Label(detail_frame2,
            text='Phone:',
            font=('orbitron',23),
            fg='white',
            bg='#116530')
        Phone_label.grid(row=0,column=0,pady=5, padx= 5)


        Phone_box = tk.Entry(detail_frame2,
                                                              
                            font=('orbitron',23),
                            width=15,borderwidth=2,
                            justify= 'center',
                            background='#E8E8CC')
        Phone_box.grid(row=0,column=1,pady=5,padx=5)

        Age_Label = tk.Label(detail_frame2,
            text='Age:',
            font=('orbitron',23),
            fg='white',
            bg='#116530')
        Age_Label.grid(row=0,column=2,pady=5, padx= 5)


        Age_box = tk.Entry(detail_frame2,
                                                              
                                                              font=('orbitron',23),
                                                              width=5,borderwidth=2,
                                                              justify= 'center',
                                                              background='#E8E8CC')
        Age_box.grid(row=0,column=3,pady=5,padx=5)

        Star_Label = tk.Label(detail_frame2,
            text='Star:',
            font=('orbitron',23),
            fg='white',
            bg='#116530')
        Star_Label.grid(row=0,column=4,pady=5, padx= 5)

        star_box = tk.Entry(detail_frame2,
                                                              
                                                              font=('orbitron',23),
                                                              width=5,borderwidth=2,
                                                              justify= 'center',
                                                              background='#E8E8CC')
        star_box.grid(row=0,column=5,pady=5,padx=5)



        item_Label = tk.Label(invoice_heading,
            text='Items',
            font=('orbitron',20),
            fg='white',
            bg='#3C4A3E')
        item_Label.grid(row=0,column=0,sticky="ew")

        price_Label = tk.Label(invoice_heading,
            text='Price',
            font=('orbitron',20),
            fg='white',
            bg='#3C4A3E')
        price_Label.grid(row=0,column=1,sticky="ew")

        qty_Label = tk.Label(invoice_heading,
            text='Quantity',
            font=('orbitron',20),
            fg='white',
            bg='#3C4A3E')
        qty_Label.grid(row=0,column=2,sticky="ew")

        total_Label = tk.Label(invoice_heading,
            text='Total',
            font=('orbitron',20),
            fg='white',
            bg='#3C4A3E')
        total_Label.grid(row=0,column=3,sticky="ew")

        # Fetching products from prod_db 
        products = MongoCommand.fetch_prod()
        prod_name = tuple(products.keys())
        # invoice widgits list
        itemscb = []
        priceeb = []
        qtysb = []
        totaleb = []

        # Grand Total function
        def GT():
            total = 0
            total_box.delete(0, END)
            GT_box.delete(0, END)
            for price in totaleb:
                if len(price.get()) != 0:
                    total += int(price.get())
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
            priceeb[row].insert(0, products[itemscb[row].get()])
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
                    cb['values'] = prod_name
                    cb['state'] = 'readonly'
                    cb.config(justify= CENTER, font=('orbitron',16), width= 17, background='#E8E8CC')
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
                    qb.config(justify= CENTER, font=('orbitron',19),width=15,background='#E8E8CC')
                    qb.grid(row=row+1,column=column)
                    #qb.config(justify= CENTER, font=('orbitron',18), width= 10)
                    qtysb.append(qb)
                else:
                    tb = tk.Entry(invoice_heading, width=18, justify= 'center', font=('orbitron',18),background='#E8E8CC')
                    tb.grid(row=row+1,column=column)
                    totaleb.append(tb)

        

        total_foot_Label = tk.Label(invoice_heading,
            text='Total',
            font=('orbitron',20),
            fg='white',
            bg='#3C4A3E')
        total_foot_Label.grid(row=10,column=2,sticky="ew")

        total_box = tk.Entry(invoice_heading, width=16, justify= 'center', font=('orbitron',20),background='#E8E8CC')
        total_box.grid(row=10,column=3,sticky='ewns', pady=1)

        discount_foot_Label = tk.Label(invoice_heading,
            text='Discount',
            font=('orbitron',20),
            fg='white',
            bg='#3C4A3E')
        discount_foot_Label.grid(row=11,column=2,sticky="ew",pady=1)

        discount_box = tk.Entry(invoice_heading, width=16, justify= 'center', font=('orbitron',20),background='#E8E8CC')
        discount_box.grid(row=11,column=3,sticky='ewns',pady=1)

        GT_foot_Label = tk.Label(invoice_heading,
            text='Grand Total',
            font=('orbitron',20, BOLD),
            fg='white',
            bg='#3C4A3E')
        GT_foot_Label.grid(row=12,column=2,sticky="ew",pady=1)
    
        GT_box = tk.Entry(invoice_heading, width=16, justify= 'center', font=('orbitron',20, BOLD),background='#E8E8CC')
        GT_box.grid(row=12,column=3,sticky='ewns',pady=1)


        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        Right PACK
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        button_frame = tk.Frame(self,
                                 bg='#116530')
        button_frame.pack(expand=True, fill='both')

        cid_Label = tk.Label(button_frame,
                            text='Customer Id',
                            font=('orbitron',24, BOLD),
                            fg='#B7C304',
                            bg='#116530')
        cid_Label.pack(fill=X, padx=40, pady=20)

        cid_box = tk.Entry(button_frame,
                                                              
                            font=('orbitron',23),
                            width=8,borderwidth=2,
                            background='#E8E8CC',
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
                                 bg = '#FFCC1D',
                                 relief='raised',fg='Black',
                                 borderwidth = 1,
                                 width=10,
                                 )
        validate_button.pack(anchor= CENTER, pady=10)  

        def gencid():
            amt = 0
            if len(GT_box.get()) != 0:
                amt = float(GT_box.get().replace('₹',''))
            cid = MongoCommand.add_cust(name=Name_box.get(),
                                  age= int(Age_box.get()),
                                  phone= Phone_box.get(),
                                  amount= amt,
                                  freq=1)
            cid_box.delete(0, END)
            cid_box.insert(0,cid)

        generate_cid_button = tk.Button(button_frame,
                                 text='Generate Customer Id',font=('orbitron',20),
                                 command= gencid,
                                 bg = '#FFCC1D',
                                 relief='raised',fg='Green',
                                 borderwidth = 1,
                                 )
        generate_cid_button.pack(anchor= CENTER, pady=10)
        
        def clear_stuffs():
            for i in itemscb:
                i.set('')
            for i in priceeb:
                i.delete(0, END)
            for i in qtysb:
                i.delete(0, END)
            for i in totaleb:
                i.delete(0, END)
            Name_box.delete(0, END)
            Age_box.delete(0, END)
            Phone_box.delete(0, END)
            star_box.delete(0, END)
            GT_box.delete(0, END)
            total_box.delete(0, END)
            discount_box.delete(0, END)
            cid_box.delete(0, END)


        # Generate bill function triggers whatsapp automation and clear entry boxes, push invoice in database
        def generate_bill():
            cid = int(cid_box.get())
            billamount = float(GT_box.get().replace('₹', ''))
            bamt = GT_box.get()
            MongoCommand.update_cusotmer(cid, billamount)
            customer = MongoCommand.fetch_by_id(cid)
            items = list()
            for i in itemscb:
                if len(i.get()) != 0:
                    items.append(i.get())
            discount = discount_box.get().replace('%', '')
            invno = MongoCommand.invoice_creation(cid, billamount,items, discount)
            message = "Hello "+customer.Name+", Thanks for visiting us! You have just compleated shopping of "+bamt+" on Invoice No. xyz. Keep shopping to increase your stars and get exciting discount in future"
            whatsappautomation(customer.Phone, message)
            newinvoicenumber = MongoCommand.get_invoice_number()
            invo_no.configure(text=newinvoicenumber)
            clear_stuffs()
       
        generate_invoice_button = tk.Button(button_frame,
                                 text='Generate Invoice',font=('orbitron',23,BOLD),
                                 command= generate_bill,
                                 bg = '#FFCC1D',
                                 relief='raised',fg='#3C4A3E',
                                 borderwidth = 1)
        generate_invoice_button.pack(side= BOTTOM,anchor= CENTER, pady=20)       

        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = tk.Button(button_frame,
                                command=menu,fg='black',
                                bg = '#6B7B6E',
                                text='Menu',font=('orbitron',20),
                                relief='raised',
                                borderwidth=1,
                                width=5)
        menu_button.pack(side = BOTTOM,anchor= CENTER, pady=20)