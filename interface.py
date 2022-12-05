import customtkinter as ctk
import tkinter.ttk as ttk
from PIL import Image

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class Interface(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        ### config window
        self.height = 700
        self.width = 950
        self.geometry(f"{self.width}x{self.height}")
        self.title("I Sales")
        self.minsize(700,680)
        
        ### constant variables
        self.SIZE_BUTON = 40
        self.PADX_BUTON = 20
        self.TOOL_BAR_SIZE = (500,48)
        
        
        
        ### Buton Image
        self.search_image = ctk.CTkImage(dark_image=Image.open("image/icon/search.png"))
        self.add_image = ctk.CTkImage(dark_image=Image.open("image/icon/plus-circle.png"))
        self.edit_image = ctk.CTkImage(dark_image=Image.open("image/icon/edit.png"))
        self.delete_image = ctk.CTkImage(dark_image=Image.open("image/icon/trash.png"))
        self.dollar_image = ctk.CTkImage(dark_image=Image.open("image/icon/dollar-sign.png"))
        
        ### Stock Tool Bar
        self.stock_botons_top_frame = ctk.CTkFrame(self,
                                                   self.TOOL_BAR_SIZE[0],
                                                   self.TOOL_BAR_SIZE[1])
        self.stock_botons_top_frame.pack_propagate(False)
        self.stock_botons_top_frame.pack(pady=10)
        
        ### Stock Boton
        
        self.search_entry = ctk.CTkEntry(self.stock_botons_top_frame)
        self.search_entry.pack(side="left", padx=self.PADX_BUTON)
        
        self.search_buton = ctk.CTkButton(self.stock_botons_top_frame,
                                          image=self.search_image,
                                          text="",
                                          width=self.SIZE_BUTON,
                                          height=self.SIZE_BUTON
                                          )
        self.search_buton.pack(side="left", padx=self.PADX_BUTON)
        
        self.add_product_buton = ctk.CTkButton(self.stock_botons_top_frame,
                                          image=self.add_image,
                                          text="",
                                          width=self.SIZE_BUTON,
                                          height=self.SIZE_BUTON,
                                          fg_color="green3",
                                          hover_color="green"
                                          )
        self.add_product_buton.pack(side="left", padx=self.PADX_BUTON)
        
        self.edit_product_buton = ctk.CTkButton(self.stock_botons_top_frame,
                                          image=self.edit_image,
                                          text="",
                                          width=self.SIZE_BUTON,
                                          height=self.SIZE_BUTON,
                                          )
        self.edit_product_buton.pack(side="left", padx=self.PADX_BUTON)
        
        self.delete_product_buton = ctk.CTkButton(self.stock_botons_top_frame,
                                          image=self.delete_image,
                                          text="",
                                          width=self.SIZE_BUTON,
                                          height=self.SIZE_BUTON,
                                          fg_color="red",
                                          hover_color="red4"
                                          )
        self.delete_product_buton.pack(side="left", padx=self.PADX_BUTON)
        
        ### Stock List
        self.stock_list = ttk.Treeview(self, columns=(
                                                        "Products",
                                                        "Stock",
                                                        "Price"
                                                        )
                                          )
        
        self.stock_list.column('#0', width=100)
        self.stock_list.heading('#0', text="ID")
        
        self.stock_list.column('Products', width=500)
        self.stock_list.heading('Products', text="Products")
        
        self.stock_list.column('Stock', width=100)
        self.stock_list.heading('Stock', text="Stock")
        
        self.stock_list.column('Price', width=100)
        self.stock_list.heading('Price', text="Price")
        
        self.stock_list.pack()
        
        ### Sale Tool Bar 
        self.sales_botons_top_frame = ctk.CTkFrame(self,
                                                   250,
                                                   height=self.TOOL_BAR_SIZE[1])
        self.sales_botons_top_frame.pack_propagate(False)
        self.sales_botons_top_frame.pack(pady=10)
        
        ### Sale Boton
        self.add_sale_buton = ctk.CTkButton(self.sales_botons_top_frame,
                                          image=self.add_image,
                                          text="",
                                          width=self.SIZE_BUTON,
                                          height=self.SIZE_BUTON,
                                          fg_color="green3",
                                          hover_color="green"
                                          )
        self.add_sale_buton.pack(side="left", padx=self.PADX_BUTON)
        
        self.edit_sale_buton = ctk.CTkButton(self.sales_botons_top_frame,
                                          image=self.edit_image,
                                          text="",
                                          width=self.SIZE_BUTON,
                                          height=self.SIZE_BUTON,
                                          )
        self.edit_sale_buton.pack(side="left", padx=self.PADX_BUTON)
        
        self.delete_sale_buton = ctk.CTkButton(self.sales_botons_top_frame,
                                          image=self.delete_image,
                                          text="",
                                          width=self.SIZE_BUTON,
                                          height=self.SIZE_BUTON,
                                          fg_color="red",
                                          hover_color="red4"
                                          )
        self.delete_sale_buton.pack(side="left", padx=self.PADX_BUTON)
        
        self.sales_list = ttk.Treeview(self, columns=(
                                                        "Products",
                                                        "Amount",
                                                        "Price"
                                                        )
                                          )
        
        self.sales_list.column('#0', width=100)
        self.sales_list.heading('#0', text="ID")
        
        self.sales_list.column('Products', width=500)
        self.sales_list.heading('Products', text="Products")
        
        self.sales_list.column('Amount', width=100)
        self.sales_list.heading('Amount', text="Amount")
        
        self.sales_list.column('Price', width=100)
        self.sales_list.heading('Price', text="Price")
        
        self.sales_list.pack()

        ### total and sale boton
        self.sales_botons_bottom_frame = ctk.CTkFrame(self,
                                                   300,
                                                   80)
        self.sales_botons_bottom_frame.pack_propagate(False)
        self.sales_botons_bottom_frame.pack(side="bottom", pady=10, padx=200)
        
        self.sales_text_total = ctk.CTkLabel(self.sales_botons_bottom_frame,
                                        text="Total: $0")
        self.sales_text_total.cget("font").configure(size=20)
        self.sales_text_total.pack(side="left", padx=self.PADX_BUTON)
        
        self.sale_buton = ctk.CTkButton(self.sales_botons_bottom_frame,
                                          image=self.dollar_image,
                                          text="",
                                          width=self.SIZE_BUTON,
                                          height=self.SIZE_BUTON,
                                          fg_color="green3",
                                          hover_color="green",
                                          command=self.sale
                                          )
        self.sale_buton.pack(padx=20 , side="left")
        self.sales_text_total.pack(side="left", padx=self.PADX_BUTON)

    def insert_product(self, product_dicts):
        """insert 15 product in list stock

        Args:
            product_dicts (dict): dictionari the products
        """
        for product in product_dicts[:15]:
            data = (
                    product["product_id"],
                    product["name"],
                    product["stock"],
                    product["price"])
            self.stock_list.insert('', ctk.END, values=data)
    
    def product_delete(self):
        """delete product the database and stock_list
        """
        select_id = self.stock_list.focus()
        if select_id != "":
            select = self.stock_list.item(select_id)['values']
            delete = messagebox.askquestion("Delete",
                                f"wants delete product {select[1]}?"
                                )
            if delete == "yes":
                db.product_delete(select[0])
                self.stock_list.delete(select_id)
    
    def product_search(self):
        """search product and update stock_list
        """
        text= self.search_entry.get()
        for product in self.stock_list.get_children():
            self.stock_list.delete(product)
            
        for product in db.product_search(text):
            data = (
                    product.product_id,
                    product.name,
                    product.stock,
                    product.price)
            self.stock_list.insert('', ctk.END, values=data)
    
        
    def window_add(self):
        """create window for insert data and add product
        """
        new_window = ctk.CTkToplevel(self)
        new_window.geometry("500x600")
        new_window.resizable(0,0)
        new_window.title("Add")
        
        name_text = ctk.CTkLabel(master=new_window,text="Name:")
        name_text.cget("font").configure(size=20)
        name_text.pack(pady=10)
        name_entry = ctk.CTkEntry(master=new_window,width=300)
        name_entry.pack()
        
        info_text = ctk.CTkLabel(master=new_window,text="Info:")
        info_text.cget("font").configure(size=20)
        info_text.pack(pady=10)
        info_entry = ctk.CTkTextbox(master=new_window,height=150,width=300)
        info_entry.pack()
        
        price_var = ctk.StringVar()
        price_text = ctk.CTkLabel(master=new_window,text="Price:")
        price_text.cget("font").configure(size=20)
        price_text.pack(pady=10)
        price_entry = ctk.CTkEntry(master=new_window, width=300, textvariable=price_var)
        price_var.set("0.0")
        price_entry.pack()
        
        stock_var = ctk.StringVar()
        stock_text = ctk.CTkLabel(master=new_window,text="Stock:")
        stock_text.cget("font").configure(size=20)
        stock_text.pack(pady=10)
        stock_entry = ctk.CTkEntry(master=new_window,width=300, textvariable=stock_var)
        stock_var.set("0")
        stock_entry.pack()

        create_boton = ctk.CTkButton(master=new_window,
                                     image=self.add_image,
                                     width=50,
                                     height=50,
                                     text="",
                                     fg_color="green3",
                                     hover_color="green",
                                     command=lambda:self.product_add(
                                         new_window,
                                         name_entry.get(),
                                         info_entry.get("1.0",ctk.END),
                                         price_entry.get(),
                                         stock_entry.get(),
                                        )
                                    )
        create_boton.pack(side="left", padx=100)
        
        cancel_boton = ctk.CTkButton(master=new_window,
                                     image=self.cancel_image,
                                     width=50,
                                     height=50,
                                     text="",
                                     fg_color="red",
                                     hover_color="red4",
                                     command=new_window.destroy
                                     )
        cancel_boton.pack(side="right", padx=100)

    def window_update(self):
        """create window for insert data and update product
        """
        select_id = self.stock_list.focus()
        if select_id != "":
            select = self.stock_list.item(select_id)['values']
            select = db.product_info(select[0])
            for x in select:
                product = [x["product_id"],
                            x["name"],
                            x["info"],
                            x["price"],
                            x["stock"]
                           ]

            
            new_window = ctk.CTkToplevel(self)
            new_window.geometry("500x600")
            new_window.resizable(0,0)
            new_window.title("Update")


            name_text = ctk.CTkLabel(master=new_window,text="Name:")
            name_text.cget("font").configure(size=20)
            name_text.pack(pady=10)
            name_entry = ctk.CTkEntry(master=new_window,width=300)
            name_entry.insert(0,product[1])
            name_entry.pack()
            
            info_text = ctk.CTkLabel(master=new_window,text="Info:")
            info_text.cget("font").configure(size=20)
            info_text.pack(pady=10)
            info_entry = ctk.CTkTextbox(master=new_window,height=150,width=300)
            info_entry.insert(ctk.INSERT,product[2])
            info_entry.pack()
            
            price_text = ctk.CTkLabel(master=new_window,text="Price:")
            price_text.cget("font").configure(size=20)
            price_text.pack(pady=10)
            price_entry = ctk.CTkEntry(master=new_window, width=300)
            price_entry.insert(0,product[3])
            price_entry.pack()
            
            stock_text = ctk.CTkLabel(master=new_window,text="Stock:")
            stock_text.cget("font").configure(size=20)
            stock_text.pack(pady=10)
            stock_entry = ctk.CTkEntry(master=new_window,width=300)
            stock_entry.insert(0,product[4])
            stock_entry.pack()

            create_boton = ctk.CTkButton(master=new_window,
                                        image=self.add_image,
                                        width=50,
                                        height=50,
                                        text="",
                                        fg_color="green3",
                                        hover_color="green",
                                        command=lambda:self.product_update(
                                            new_window,
                                            product[0],
                                            name_entry.get(),
                                            info_entry.get("1.0",ctk.END),
                                            price_entry.get(),
                                            stock_entry.get(),
                                            )
                                        )
            create_boton.pack(side="left", padx=100)
            
            cancel_boton = ctk.CTkButton(master=new_window,
                                        image=self.cancel_image,
                                        width=50,
                                        height=50,
                                        text="",
                                        fg_color="red",
                                        hover_color="red4",
                                        command=new_window.destroy
                                        )
            cancel_boton.pack(side="right", padx=100)

    def product_add(self,window,name,info,price,stock):
        """add product to database

        Args:
            window (Toplevel): for close 
            name (str): productname
            info (str): product info
            price (float): product price
            stock (int): product stock
        """
        save = True
        if name == "":
            messagebox.showwarning( title="Error",message="Insert Name", parent=window)
            save = False
        try:
            if price == "":
                price = 0
            else:
                price = float(price)
        except:
            messagebox.showwarning(title="Error", message="insert number value in price", parent=window)
            save = False
        
        try:
            if stock == "":
                stock = 0
            else:
                stock = int(stock)
        except:
            messagebox.showwarning(title="Error", message="insert number value in stock", parent=window)
            save = False
        if save == True:
            db.product_add(name,info,price,stock)
            window.destroy()

    def product_update(self,window,id,name,info,price,stock):
        """update product for database

        Args:
            window (Toplevel): for close
            id (str): id the product for search in database
            name (str): for update name
            info (str): for update info
            price (float): for update price
            stock (int): for update stock
        """
        save = True
        if name == "":
            messagebox.showwarning( title="Error",message="Insert Name", parent=window)
            save = False
        try:
            if price == "":
                price = 0
            else:
                price = float(price)
        except:
            messagebox.showwarning(title="Error", message="insert number value in price", parent=window)
            save = False
        
        try:
            if stock == "":
                stock = 0
            else:
                stock = int(stock)
        except:
            messagebox.showwarning(title="Error", message="insert number value in stock", parent=window)
            save = False
        if save == True:
            db.product_update(id,name,info,price,stock)
            window.destroy()

    def product_add_sale(self):
        """add a prodct of the stock list to sales list
        if the sum exists
        """
        select_id = self.stock_list.focus()
        if select_id != "":
            select = self.stock_list.item(select_id)['values']
            repit = False
            for id in self.sales_list.get_children():
                item = self.sales_list.item(id)['values']
                if item[0] == select[0]:
                    repit = True
                    item[2] = str(int(item[2]) + 1)
                    item[4] = str(float(item[2]) * float(item[3]))
                    self.sales_list.item(id, values=item)
            if not repit:
                product = [
                            select[0],
                            select[1],
                            1,
                            select[3],
                            select[3]
                        ]
                self.sales_list.insert('',ctk.END, values=product)
            self.update_total()

    def product_minus_sale(self):
        """minus product in sale list 
        if stock is one the quit
        """
        select_id = self.sales_list.focus()
        if select_id != "":
            item = self.sales_list.item(select_id)['values']
            if int(item[2]) == 1:
                self.sales_list.delete(select_id)
            else:
                item[2] = int(item[2]) - 1
                item[4] = float(item[2]) * float(item[3])
                self.sales_list.item(select_id, values=item)
            self.update_total()
                
    def product_delete_sale(self):
        """delte product selection in the sales list
        """
        select_id = self.sales_list.focus()
        if select_id != "":
            select = self.sales_list.item(select_id)['values']
            delete = messagebox.askquestion("Delete",
                                f"wants delete product {select[1]} in sale?"
                                )
            if delete == "yes":
                self.sales_list.delete(select_id)
                self.update_total()

    def update_total(self):
        self.total = 0
        for id in self.sales_list.get_children():
            self.total += float(self.sales_list.item(id)["values"][4])
        total = "{:,}".format(self.total)
        self.sales_text_total.configure(text=f"Total: $ {total}")

    def sale(self):
        id_sale = self.sales_list.get_children()
        if len(id_sale) > 0:
            new_window = ctk.CTkToplevel(self)
            new_window.geometry("300x200")
            new_window.resizable(0,0)
            new_window.title("Pay")
            
            pay_text = ctk.CTkLabel(new_window,text="Pay with:")
            pay_text.pack(pady=10)
            pay_entry = ctk.CTkEntry(new_window)
            pay_entry.pack(pady=10)
            
            pay_boton = ctk.CTkButton(master=new_window,
                                     image=self.dollar_image,
                                     width=50,
                                     height=50,
                                     text="",
                                     fg_color="green3",
                                     hover_color="green",
                                     command=lambda:self.pay(id_sale,
                                                             pay_entry.get(),
                                                             new_window)
                                     )
        self.sale_buton.pack(pady=self.PADX_BUTON)



if __name__ == "__main__":
    app = Interface()
    app.mainloop()