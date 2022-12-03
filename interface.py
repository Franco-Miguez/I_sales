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
                                          hover_color="green"
                                          )
        self.sale_buton.pack(pady=self.PADX_BUTON)



if __name__ == "__main__":
    app = Interface()
    app.mainloop()