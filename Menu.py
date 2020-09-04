from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Connection import Item


class ItemView:
    """
            This class manages menu of the hotel.

            Methods:
                add_item()
                del_item()
                update_item()
                show_item_tree()
                select_item()
                reset_btn()
                ser_item()

            """

    def __init__(self, window):
        self.window = window
        self.window.title("Hotel Management System")
        self.window.geometry("1366x768+0+0")
        self.window.configure(bg="sky blue")

        self.bg_save = PhotoImage(file="Pictures/save.png")
        self.bg_update = PhotoImage(file="Pictures/update.png")
        self.bg_del = PhotoImage(file="Pictures/delete.png")
        self.bg_reset = PhotoImage(file="Pictures/reset.png")
        self.bg_back = PhotoImage(file="Pictures/back.png")
        self.bg_search = PhotoImage(file="Pictures/search.png")

        self.label_number = Label(self.window, text="Menu", font=("arial", 20, "bold"), fg="navy blue", bg="sky blue")
        self.label_number.pack()

        self.line = Canvas(self.window, width=1200, height=2, bg="navy blue").pack()

        self.item_index = ""
        self.my_index = 1

        # frames
        self.frame1 = Frame(self.window, bg="sky blue")
        self.frame1.place(x=50, y=50)
        self.frame2 = Frame(self.window, bg="sky blue")
        self.frame2.place(x=750, y=50)

        # entry boxes and label to them
        self.title = Label(self.frame1, text="Add New Item to Menu", font=("arial", 16, "bold"), fg="#000000",
                           bg="sky blue")
        self.title.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.line = Canvas(self.frame1, width=600, height=2, bg="white").grid(row=1, columnspan=2)

        self.label_name = Label(self.frame1, text="Name", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_name.grid(row=2, column=0, padx=5, pady=5)
        self.item_name = Entry(self.frame1, font=("arial", 18))
        self.item_name.grid(row=2, column=1, padx=5, pady=5)

        self.label_type = Label(self.frame1, text="Type", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_type.grid(row=3, column=0, padx=5, pady=5)
        self.item_type = Entry(self.frame1, font=("arial", 18))
        self.item_type.grid(row=3, column=1, padx=5, pady=5)

        self.label_rate = Label(self.frame1, text="Rate", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_rate.grid(row=4, column=0, padx=5, pady=5)
        self.item_rate = Entry(self.frame1, font=("arial", 18))
        self.item_rate.grid(row=4, column=1, padx=5, pady=5)

        # buttons
        self.btn_add = Button(self.frame1, text="Add Item", command=self.add_item, width=20, font=("arial", 16, "bold"),
                              bg="sky blue", activebackground="blue", image=self.bg_save, compound=LEFT)
        self.btn_add.grid(row=5, column=1, padx=5, pady=5, sticky=W + E)

        self.btn_update = Button(self.frame1, text="Update Item", width=20, command=self.update_item, bg="sky blue",
                                 activebackground="yellow", font=("arial", 16, "bold"), image=self.bg_update,
                                 compound=LEFT)
        self.btn_update.grid(row=6, column=1, padx=5, pady=5, sticky=W + E)

        self.btn_del = Button(self.frame1, text="Delete Item", command=self.del_item, width=20, bg="sky blue",
                              font=("arial", 16, "bold"), activebackground="red", image=self.bg_del, compound=LEFT)
        self.btn_del.grid(row=7, column=1, padx=5, pady=5, sticky=W + E)

        self.btn_res = Button(self.frame1, text="Reset", command=self.reset_btn, width=20, font=("arial", 16, "bold"),
                              bg="sky blue", activebackground="blue", image=self.bg_reset, compound=LEFT)
        self.btn_res.grid(row=8, column=1, padx=5, pady=5, sticky=W + E)

        self.btn_back = Button(self.frame1, text="Back", command=self.window.destroy, width=20, bg="sky blue",
                               font=("arial", 16, "bold"), activebackground="red", image=self.bg_back, compound=LEFT)
        self.btn_back.grid(row=9, column=1, padx=5, pady=5, sticky=W + E)

        # search
        self.label_ser = Label(self.frame2, text="Search for:", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_ser.grid(row=1, column=0, padx=5, pady=5)
        self.item_ser = Entry(self.frame2, font=("arial", 18))
        self.item_ser.grid(row=1, column=1, padx=5, pady=5)

        self.btn_ser = Button(self.frame2, text="Search", command=self.ser_item, width=20, font=("arial", 16, "bold"),
                              bg="sky blue", activebackground="blue", image=self.bg_search, compound=LEFT)
        self.btn_ser.grid(row=2, column=1, padx=5, pady=5, sticky=W + E)

        self.item_tree = ttk.Treeview(self.frame2, columns=('type', 'name', 'rate'), height=15)
        self.item_tree.grid(row=3, column=0, columnspan=2)
        self.item_tree['show'] = 'headings'
        self.item_tree.column('name', width=175)
        self.item_tree.column('type', width=175)
        self.item_tree.column('rate', width=75)
        self.item_tree.heading('name', text="Name")
        self.item_tree.heading('type', text="Type")
        self.item_tree.heading('rate', text="Rate")
        self.scroll = ttk.Scrollbar(self.frame2, orient="vertical", command=self.item_tree.yview)
        self.scroll.grid(row=3, column=0, columnspan=4, sticky='e' + 'ns')
        self.item_tree.configure(yscrollcommand=self.scroll.set)

        self.show_item_tree()

    def add_item(self):
        """verify the entry values and add new item to menu"""
        name = self.item_name.get()
        type_ = self.item_type.get()
        price = self.item_rate.get()
        item = Item()
        if name == "" or price == "":
            messagebox.showerror("Error", "Enter all values")
        elif not price.isnumeric():
            messagebox.showerror("Error", "Enter numeric value for price")
        else:
            if item.add_item(name, type_, price):
                messagebox.showinfo("Item", "Item Added")
                self.show_item_tree()
                self.reset_btn()
            else:
                messagebox.showerror("Error", "Item cannot be added")

    def del_item(self):
        """delete an item from menu"""
        item = Item()
        a = messagebox.askyesno("Delete", "Are you sure you want to delete this item?")
        if a == 1:
            if item.delete_item(self.item_index):
                messagebox.showinfo("Item", "Item Deleted")
                self.show_item_tree()
                self.reset_btn()
            else:
                messagebox.showerror("Error", "Item cannot be deleted")

    def update_item(self):
        """update an item detail in menu"""
        name = self.item_name.get()
        type_ = self.item_type.get()
        price = self.item_rate.get()
        id_ = self.item_index
        item = Item()
        if item.update_item(id_, name, type_, price):
            messagebox.showinfo("Item", "Item Updated")
            self.show_item_tree()
            self.reset_btn()
        else:
            messagebox.showerror("Error", "Item cannot be added")

    def show_item_tree(self):
        """display menu"""
        self.item_tree.delete(*self.item_tree.get_children())
        item = Item()
        data = item.show_items()
        for i in data:
            self.item_tree.insert("", "end", text=i[0], value=(i[2], i[1], i[3]))
        self.item_tree.bind("<Double-1>", self.select_item)

    def select_item(self, event):
        """when double click to item in treeview it display the selected item in entrybox for other operation"""
        selected_item = self.item_tree.selection()[0]
        self.item_index = self.item_tree.item(selected_item, 'text')
        item_data = self.item_tree.item(selected_item, 'values')
        self.item_name.delete(0, END)
        self.item_name.insert(0, item_data[1])
        self.item_type.delete(0, END)
        self.item_type.insert(0, item_data[0])
        self.item_rate.delete(0, END)
        self.item_rate.insert(0, item_data[2])

    def reset_btn(self):
        """clears out the entry fields"""
        self.item_name.delete(0, END)
        self.item_type.delete(0, END)
        self.item_rate.delete(0, END)
        self.item_ser.delete(0, END)

    def ser_item(self):
        """search for item in menu"""
        search = self.item_ser.get()
        self.item_tree.delete(*self.item_tree.get_children())
        item = Item()
        data = item.search_item(search)
        for i in data:
            self.item_tree.insert("", "end", text=i[0], value=(i[2], i[1], i[3]))
        self.item_tree.bind("<Double-1>", self.select_item)


def main():
    wn = Tk()
    ItemView(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()
