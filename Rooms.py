from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Connection import Room


class Rooms:
    """
                This class manages rooms of the hotel.

                Methods:
                    show_room_tree()
                    select_item()
                    on_save_click()
                    on_update_click()
                    on_reset_click()
                    on_submit_click()
                    on_delete_click()

                """

    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x768+0+0")
        self.window.configure(bg="sky blue")

        self.bg_save = PhotoImage(file="Pictures/save.png")
        self.bg_update = PhotoImage(file="Pictures/update.png")
        self.bg_del = PhotoImage(file="Pictures/delete.png")
        self.bg_reset = PhotoImage(file="Pictures/reset.png")
        self.bg_back = PhotoImage(file="Pictures/back.png")

        self.label_number = Label(self.window, text="Rooms", font=("arial", 20, "bold"), fg="navy blue", bg="sky blue")
        self.label_number.pack()

        self.line = Canvas(self.window, width=1000, height=2, bg="navy blue").pack()

        self.frame1 = Frame(self.window, bg="sky blue")
        self.frame1.pack()

        # room entry form
        self.label_number = Label(self.frame1, text="Room No", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_number.grid(row=0, column=0, padx=5, pady=5)
        self.entry_number = Entry(self.frame1, font=("arial", 18))
        self.entry_number.grid(row=0, column=1, padx=5, pady=5)

        self.label_category = Label(self.frame1, text="Room Category", font=("arial", 18, "bold"), fg="#000000",
                                    bg="sky blue")
        self.label_category.grid(row=1, column=0, padx=5, pady=5)
        self.combo_category = ttk.Combobox(self.frame1, width=19, font=("arial", 18))
        self.combo_category['values'] = ['Single', 'Double', 'Twin', 'King', 'Suit']
        self.combo_category.grid(row=1, column=1, padx=5, pady=5)

        self.label_description = Label(self.frame1, text="Room Description", font=("arial", 18, "bold"), fg="#000000",
                                       bg="sky blue")
        self.label_description.grid(row=2, column=0, padx=5, pady=5)
        self.entry_description = Entry(self.frame1, font=("arial", 18))
        self.entry_description.grid(row=2, column=1, padx=5, pady=5)

        self.label_price = Label(self.frame1, text="Room Price", font=("arial", 18, "bold"), fg="#000000",
                                 bg="sky blue")
        self.label_price.grid(row=3, column=0, padx=5, pady=5)
        self.entry_price = Entry(self.frame1, font=("arial", 18))
        self.entry_price.grid(row=3, column=1, padx=5, pady=5)

        # buttons for different operations
        self.btn_save = Button(self.frame1, text="Save", width=20, font=("arial", 16, "bold"), bg="sky blue",
                               activebackground="blue", command=self.on_save_click, image=self.bg_save, compound=LEFT)
        self.btn_save.grid(row=6, column=1, sticky=W + E, padx=5, pady=5)

        self.btn_update = Button(self.frame1, text="Update", width=20, font=("arial", 16, "bold"), bg="sky blue",
                                 activebackground="yellow", command=self.on_update_click, image=self.bg_update,
                                 compound=LEFT)
        self.btn_update.grid(row=6, column=0, padx=5, sticky=W + E, pady=5)

        self.btn_del = Button(self.frame1, text="Delete", width=20, font=("arial", 16, "bold"), bg="sky blue",
                              activebackground="red", command=self.on_delete_click, image=self.bg_del, compound=LEFT)
        self.btn_del.grid(row=7, column=0, padx=5, sticky=W + E, pady=5)

        self.btn_reset = Button(self.frame1, text="Reset", width=20, font=("arial", 16, "bold"), bg="sky blue",
                                activebackground="yellow", command=self.on_reset_click, image=self.bg_reset,
                                compound=LEFT)
        self.btn_reset.grid(row=7, column=1, sticky=W + E, padx=5, pady=5)

        # treeview to display rooms
        self.room_tree = ttk.Treeview(self.frame1, columns=('Room No', 'Category', 'Description', 'Price', 'Status'))
        self.room_tree.grid(row=10, column=0, columnspan=4)
        self.room_tree['show'] = 'headings'
        self.room_tree.column('Room No', width=75)
        self.room_tree.column('Category', width=100)
        self.room_tree.column('Description', width=200)
        self.room_tree.column('Price', width=75)
        self.room_tree.column('Status', width=120)
        self.room_tree.heading('Room No', text="Room No")
        self.room_tree.heading('Category', text="Category")
        self.room_tree.heading('Description', text="Description")
        self.room_tree.heading('Price', text="Price")
        self.room_tree.heading('Status', text="Status")
        self.scroll = ttk.Scrollbar(self.frame1, orient="vertical", command=self.room_tree.yview)
        self.scroll.grid(row=10, column=0, columnspan=4, sticky='e' + 'ns')
        self.room_tree.configure(yscrollcommand=self.scroll.set)

        self.show_room_tree()

        self.label_room1 = Label(self.frame1, text="Room No", font=("arial", 16, "bold"), fg="#000000", bg="sky blue")
        self.label_room1.grid(row=13, column=0, padx=5, pady=5)
        self.entry_room1 = Entry(self.frame1, font=("arial", 16))
        self.entry_room1.grid(row=13, column=1, padx=5, pady=5)

        # form to change room's current status
        self.label_status = Label(self.frame1, text="Change Status To", font=("arial", 16, "bold"), fg="#000000",
                                  bg="sky blue")
        self.label_status.grid(row=14, column=0, padx=5, pady=5)
        self.combo_status = ttk.Combobox(self.frame1, values=['Available', 'Cleaning', 'Not Available'],
                                         width=19, font=("arial", 16), state='readonly')
        self.combo_status.grid(row=14, column=1, padx=5, pady=5)

        self.btn_submit = Button(self.frame1, text="Submit", width=20, font=("arial", 16, "bold"), bg="sky blue",
                                 activebackground="blue", command=self.on_submit_click, image=self.bg_save,
                                 compound=LEFT)
        self.btn_submit.grid(row=15, column=1, sticky=W + E, padx=5, pady=5)

        self.btn_back = Button(self.frame1, text="Back", width=20, font=("arial", 16, "bold"), bg="sky blue",
                               activebackground="yellow", command=self.window.destroy, image=self.bg_back,
                               compound=LEFT)
        self.btn_back.grid(row=16, column=1, padx=5, sticky=W + E, pady=5)

        self.stat = ""

    def show_room_tree(self):
        """show all rooms details of hotel"""
        self.room_tree.delete(*self.room_tree.get_children())
        ret = Room()
        data = ret.show_rooms()
        for i in data:
            self.room_tree.insert("", "end", text=i[0], values=i)
        self.room_tree.bind("<Double-1>", self.select_item)

    def select_item(self, event):
        """when double click to rooms in treeview
         it display the selected room details in entrybox for other operations"""
        selected_item = self.room_tree.selection()[0]
        room_data = self.room_tree.item(selected_item, 'values')
        self.entry_number.delete(0, END)
        self.entry_number.insert(0, room_data[0])
        self.combo_category.set("")
        self.combo_category.insert(0, room_data[1])
        self.entry_description.delete(0, END)
        self.entry_description.insert(0, room_data[2])
        self.entry_price.delete(0, END)
        self.entry_price.insert(0, room_data[3])

        self.entry_room1.delete(0, END)
        self.entry_room1.insert(0, room_data[0])
        self.stat = room_data[4]

    def on_save_click(self):
        """save new room details to database"""
        room_no = self.entry_number.get()
        room_category = self.combo_category.get()
        room_description = self.entry_description.get()
        price = self.entry_price.get()

        save = Room()
        if room_no == "" or room_category == "" or room_description == "" or price == "":
            messagebox.showerror("Error", "Enter all values")
        else:
            if save.create_rooms(room_no, room_category, room_description, price):
                a = messagebox.showinfo('Success', 'Room Registered successfully')
                if a == 'ok':
                    self.on_reset_click()
                    self.show_room_tree()
            else:
                messagebox.showerror('Room Registration Failed', 'Please Try Again')

    def on_update_click(self):
        """update room details in database"""
        room_no = self.entry_number.get()
        room_category = self.combo_category.get()
        room_description = self.entry_description.get()
        price = self.entry_price.get()

        update = Room()
        if update.update_rooms(room_category, room_description, price, room_no):
            a = messagebox.showinfo('Success', 'Room Updated successfully')
            if a == 'ok':
                self.on_reset_click()
                self.show_room_tree()
        else:
            messagebox.showerror('Room Update Failed', 'Please Try Again')

    def on_reset_click(self):
        """clears out the entry fields"""
        self.entry_number.delete(0, END)
        self.combo_category.set("")
        self.entry_description.delete(0, END)
        self.entry_price.delete(0, END)
        self.entry_room1.delete(0, END)
        self.combo_status.set("")

    def on_submit_click(self):
        """changes the current room status to  cleaning or available"""
        room_no = self.entry_room1.get()
        room_stat = self.combo_status.get()

        if room_stat == "":
            messagebox.showerror("Error", "Select the current room status")
        elif self.stat == "Occupied":
            messagebox.showerror("Error", "Occupied room's status can not be changed")
        else:
            ret = Room()
            ret.change_status(room_stat, room_no)
            self.show_room_tree()

    def on_delete_click(self):
        """deletes the room from database"""
        room_no = self.entry_number.get()
        a = messagebox.askyesno("Delete", "Are you sure you want to delete room: " + str(room_no))
        if a == 1:
            delete = Room()
            delete.delete_rooms(room_no)
            self.show_room_tree()


def main():
    wn = Tk()
    wn.title("Hotel Management System")
    Rooms(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()
