from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Connection import Item
from Connection import Order


class OrderView:
    """
            This class present food orders to customers staying in hotel.

            Methods:
                add_items_in_list()
                submit_order()
                reset_tree_view()
                show_item_tree()
                ser_item()
                show_orders()
                delete_orders()

            """

    def __init__(self, cus_id, cus_name, cus_room):
        self.window = Toplevel()
        self.window.title("Hotel Management System")
        self.window.geometry("1366x768+0+0")
        self.window.configure(bg="sky blue")

        self.bg_search = PhotoImage(file="Pictures/search.png")
        self.bg_save = PhotoImage(file="Pictures/save.png")
        self.bg_show = PhotoImage(file="Pictures/show.png")
        self.bg_add = PhotoImage(file="Pictures/add.png")
        self.bg_reset = PhotoImage(file="Pictures/reset.png")
        self.bg_del = PhotoImage(file="Pictures/delete.png")
        self.bg_back = PhotoImage(file="Pictures/back.png")

        self.cus_id = cus_id
        self.cus_name = cus_name
        self.cus_room = cus_room

        self.frame2 = Frame(self.window, bg="sky blue")
        self.frame2.pack()

        self.label_name = Label(self.frame2, text=("Guest Name: " + cus_name), font=("arial", 16),
                                fg="navy blue", bg="sky blue")
        self.label_name.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        self.label_room = Label(self.frame2, text=("Room No: " + cus_room), font=("arial", 16),
                                fg="navy blue", bg="sky blue")
        self.label_room.grid(row=0, column=2, padx=5, pady=5)

        self.line = Canvas(self.frame2, width=800, height=2, bg="navy blue").grid(row=1, columnspan=3)

        # search in menu
        self.label_ser = Label(self.frame2, text="Search in Menu:", font=("arial", 16), fg="#000000", bg="sky blue")
        self.label_ser.grid(row=2, column=0, padx=5, pady=5)
        self.item_ser = Entry(self.frame2, font=("arial", 16))
        self.item_ser.grid(row=2, column=1, padx=5, pady=5)
        self.btn_ser = Button(self.frame2, text="Search", command=self.ser_item, font=("arial", 16),
                              bg="sky blue", activebackground="blue", image=self.bg_search, compound=LEFT)
        self.btn_ser.grid(row=2, column=2, sticky=W + E, padx=5, pady=5)

        # show menu for ordering food
        self.item_tree = ttk.Treeview(self.frame2, columns=('id', 'type', 'name', 'rate'))
        self.item_tree.grid(row=3, column=0, columnspan=3)
        self.item_tree['show'] = 'headings'
        self.item_tree.column('id', width=150)
        self.item_tree.column('name', width=250)
        self.item_tree.column('type', width=250)
        self.item_tree.column('rate', width=150)
        self.item_tree.heading('id', text="ID")
        self.item_tree.heading('name', text="Name")
        self.item_tree.heading('type', text="Type")
        self.item_tree.heading('rate', text="Rate")
        self.scroll = ttk.Scrollbar(self.frame2, orient="vertical", command=self.item_tree.yview)
        self.scroll.grid(row=3, column=0, columnspan=3, sticky='e' + 'ns')
        self.item_tree.configure(yscrollcommand=self.scroll.set)

        self.ordered_item_list = []

        # quantity
        self.label_qty = Label(self.frame2, text="Quantity", font=("arial", 16, "bold"), fg="#000000", bg="sky blue")
        self.label_qty.grid(row=4, column=0, padx=5, pady=5)
        self.entry_qty = Entry(self.frame2, font=("arial", 16))
        self.entry_qty.grid(row=4, column=1, padx=5, pady=5)

        self.btn_add_items = Button(self.frame2, text="Add Item", width=20, font=("arial", 16), bg="sky blue",
                                    activebackground="blue", command=self.add_items_in_list, image=self.bg_add,
                                    compound=LEFT)
        self.btn_add_items.grid(row=4, column=2, sticky=W + E, padx=5, pady=5)

        # button to command show orders
        self.btn_show_orders = Button(self.frame2, text="Show Orders", width=20, font=("arial", 16), bg="sky blue",
                                      activebackground="blue", command=self.show_orders, image=self.bg_show,
                                      compound=LEFT)
        self.btn_show_orders.grid(row=5, column=1, sticky=W + E, padx=5, pady=5)

        # displays orders
        self.order_tree = ttk.Treeview(self.frame2, columns=('id', 'type', 'name', 'qty'), height=9)
        self.order_tree.grid(row=6, column=0, columnspan=3)
        self.order_tree['show'] = 'headings'
        self.order_tree.column('id', width=150)
        self.order_tree.column('name', width=250)
        self.order_tree.column('type', width=250)
        self.order_tree.column('qty', width=150)
        self.order_tree.heading('id', text="ID")
        self.order_tree.heading('name', text="Name")
        self.order_tree.heading('type', text="Type")
        self.order_tree.heading('qty', text="Qty")
        self.scroll = ttk.Scrollbar(self.frame2, orient="vertical", command=self.order_tree.yview)
        self.scroll.grid(row=6, column=0, columnspan=3, sticky='e' + 'ns')
        self.order_tree.configure(yscrollcommand=self.scroll.set)

        # buttons
        self.btn_add_order = Button(self.frame2, text="Submit Order", width=15, font=("arial", 16), bg="sky blue",
                                    activebackground="blue", command=self.submit_order, image=self.bg_add,
                                    compound=LEFT)
        self.btn_add_order.grid(row=7, column=1, sticky=W + E, padx=5, pady=5)

        self.btn_reset = Button(self.frame2, text="Reset", width=15, font=("arial", 16), activebackground="yellow",
                                bg="sky blue", command=self.reset_tree_view, image=self.bg_reset, compound=LEFT)
        self.btn_reset.grid(row=7, column=0, sticky=W + E, padx=5, pady=5)

        self.btn_del = Button(self.frame2, text="Remove Order", width=15, font=("arial", 16), bg="sky blue",
                              activebackground="yellow", command=self.delete_order, image=self.bg_del, compound=LEFT)
        self.btn_del.grid(row=7, column=2, sticky=W + E, padx=5, pady=5)

        self.btn_back = Button(self.frame2, text="Back", width=20, font=("arial", 16), activebackground="yellow",
                               bg="sky blue", command=self.window.destroy, image=self.bg_back, compound=LEFT)
        self.btn_back.grid(row=8, column=1, sticky=W + E, padx=5, pady=5)

        self.show_item_tree()

        self.window.mainloop()

    def add_items_in_list(self):
        """take order from customer"""
        try:
            selected_item = self.item_tree.selection()[0]
            food_data = self.item_tree.item(selected_item, 'values')
            qty = self.entry_qty.get()
            if qty == "" or not qty.isnumeric():
                messagebox.showerror("Error", "Please enter a value for quantity")
            else:
                self.ordered_item_list.append((food_data[0], qty))
                self.order_tree.insert('', 'end', text='', value=('', food_data[1], food_data[2], qty))
        except IndexError:
            messagebox.showerror("Error", "Select food from menu")

    def submit_order(self):
        """save ordered foods in database"""
        order = Order()
        order.add_order(self.ordered_item_list, self.cus_id)
        messagebox.showinfo("Order", "Order Added")
        self.reset_tree_view()
        self.show_orders()

    def reset_tree_view(self):
        """clears entry fields and treeview"""
        self.order_tree.delete(*self.order_tree.get_children())
        self.ordered_item_list.clear()

        self.entry_qty.delete(0, END)
        self.item_ser.delete(0, END)

    def show_item_tree(self):
        """show menu to order foods"""
        self.item_tree.delete(*self.item_tree.get_children())
        item = Item()
        data = item.show_items()
        for i in data:
            self.item_tree.insert("", "end", text=i[0], value=(i[0], i[2], i[1], i[3]))

    def ser_item(self):
        """search for food item to order"""
        search = self.item_ser.get()
        self.item_tree.delete(*self.item_tree.get_children())
        item = Item()
        data = item.search_item(search)
        for i in data:
            self.item_tree.insert("", "end", text=i[0], value=(i[0], i[2], i[1], i[3]))

    def show_orders(self):
        """display all orders"""
        self.order_tree.delete(*self.order_tree.get_children())
        cus_id = self.cus_id
        order = Order()
        orders = order.show_orders(cus_id)
        for i in orders:
            self.order_tree.insert("", "end", text=i[1], values=i)

    def delete_order(self):
        """delete selected order made by customer"""
        try:
            selected_item = self.order_tree.selection()[0]
            order_data = self.order_tree.item(selected_item, 'values')
            order_id = order_data[0]
            up = Order()
            up.delete_order(order_id)
            self.show_orders()
        except IndexError:
            messagebox.showerror("Error", "Select food from menu")
