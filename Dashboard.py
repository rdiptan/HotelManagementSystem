from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from datetime import datetime, timedelta
from Registration import Register
from Rooms import Rooms
from Bookings import Bookings
from Connection import Room
from Connection import Booking
from Bill import BillView


class Dashboard:
    """
                This class works with new booking and display rooms and acts as homepage to system.

                Methods:
                    date_time()
                    combo_rooms()
                    on_room_search()
                    show_room_tree()
                    send_room()
                    show_book_tree()
                    on_save_click()
                    on_reset_click()
                    on_room_change()
                    on_check_out()
                    open_login()
                    open_register()
                    open_rooms()
                    open_booking()
                    exit_handler()


                """
    def __init__(self, user):
        self.window = Tk()
        self.window.title("Hotel Management System")
        self.window.geometry("1366x768+0+0")
        self.window.configure(bg="sky blue")

        self.user = user

        menubar = Menu(self.window, bg="sky blue")
        menubar.add_command(label="Rooms", activebackground="blue", font=("arial", 16, "bold"), command=self.open_rooms)
        menubar.add_command(label="Booking", activebackground="blue", font=("arial", 16, "bold"),
                            command=self.open_booking)
        if self.user[-1] == 'Admin':
            menubar.add_command(label="Register", activebackground="blue", font=("arial", 16, "bold"),
                                command=self.open_register)
        menubar.add_command(label="Log Out", activebackground="yellow", font=("arial", 16, "bold"),
                            command=self.open_login)
        menubar.add_command(label="Exit", activebackground="red", font=("arial", 16, "bold"), command=self.exit_handler)
        self.window.config(menu=menubar)

        self.lblInfo = Label(self.window, font=('arial', 19, 'bold'), bg='sky blue', fg="navy blue")
        self.lblInfo.pack()
        self.date_time()

        self.line = Canvas(self.window, width=1280, height=2, bg="navy blue").pack()

        self.frame1 = Frame(self.window, bg="sky blue")
        self.frame1.place(x=0, y=40)

        self.frame2 = Frame(self.window, bg="sky blue")
        self.frame2.place(x=600, y=40)

        self.label_name = Label(self.frame1, text="Name", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = Entry(self.frame1, font=("arial", 18))
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_phone = Label(self.frame1, text="Phone", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_phone.grid(row=1, column=0, padx=5, pady=5)
        self.entry_phone = Entry(self.frame1, font=("arial", 18))
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.label_address = Label(self.frame1, text="Address", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_address.grid(row=2, column=0, padx=5, pady=5)
        self.entry_address = Entry(self.frame1, font=("arial", 18))
        self.entry_address.grid(row=2, column=1, padx=5, pady=5)

        self.label_email = Label(self.frame1, text="Email", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_email.grid(row=3, column=0, padx=5, pady=5)
        self.entry_email = Entry(self.frame1, font=("arial", 18))
        self.entry_email.grid(row=3, column=1, padx=5, pady=5)

        self.label_stay = Label(self.frame1, text="Staying Days", font=("arial", 18, "bold"), fg="#000000",
                                bg="sky blue")
        self.label_stay.grid(row=5, column=0, padx=5, pady=5)
        self.combo_stay = ttk.Combobox(self.frame1, values=[x for x in range(1, 33)], width=19, font=("arial", 18))
        self.combo_stay.grid(row=5, column=1, padx=5, pady=5)

        self.label_room = Label(self.frame1, text="Room No", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_room.grid(row=6, column=0, padx=5, pady=5)
        self.combo_room = ttk.Combobox(self.frame1, width=19, font=("arial", 18), state='readonly')
        self.combo_room.grid(row=6, column=1, padx=5, pady=5)

        self.combo_rooms()

        self.label_adult = Label(self.frame1, text="Adults", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_adult.grid(row=7, column=0, padx=5, pady=5)
        self.entry_adult = Entry(self.frame1, font=("arial", 18))
        self.entry_adult.grid(row=7, column=1, padx=5, pady=5)

        self.label_child = Label(self.frame1, text="Children", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_child.grid(row=8, column=0, padx=5, pady=5)
        self.entry_child = Entry(self.frame1, font=("arial", 18))
        self.entry_child.grid(row=8, column=1, padx=5, pady=5)

        self.btn_save = Button(self.frame1, text="Save", width=20, font=("arial", 16, "bold"), bg="sky blue",
                               activebackground="blue", command=self.on_save_click)
        self.btn_save.grid(row=10, column=0, sticky=W + E, padx=5, pady=5)

        self.btn_reset = Button(self.frame1, text="Reset", width=20, font=("arial", 16, "bold"), bg="sky blue",
                                activebackground="yellow", command=self.on_reset_click)
        self.btn_reset.grid(row=10, column=1, sticky=W + E, padx=5, pady=5)

        # self.btn_back = Button(self.frame1, text="Back", width=20, font=("arial", 16, "bold"), bg="sky blue",
        #                        activebackground="yellow", command=self.on_back_click)
        # self.btn_back.grid(row=11, column=1, padx=5, sticky=W + E, pady=5)

        self.line = Canvas(self.frame1, width=550, height=2, bg="#ffffff").grid(row=12, columnspan=2)

        self.label_room1 = Label(self.frame1, text="Room No", font=("arial", 16, "bold"), fg="#000000", bg="sky blue")
        self.label_room1.grid(row=13, column=0, padx=5, pady=5)
        self.entry_room1 = Entry(self.frame1, font=("arial", 16))
        self.entry_room1.grid(row=13, column=1, padx=5, pady=5)

        self.label_change = Label(self.frame1, text="Change Status To", font=("arial", 16, "bold"), fg="#000000",
                                  bg="sky blue")
        self.label_change.grid(row=14, column=0, padx=5, pady=5)
        self.combo_change = ttk.Combobox(self.frame1, values=['Available', 'Cleaning'], width=19, font=("arial", 16),
                                         state='readonly')
        self.combo_change.grid(row=14, column=1, padx=5, pady=5)

        self.btn_submit = Button(self.frame1, text="Submit", width=20, font=("arial", 16), bg="sky blue",
                                 activebackground="blue", command=self.on_room_change)
        self.btn_submit.grid(row=15, column=1, sticky=W + E, padx=5, pady=5)

        self.label_room = Label(self.frame2, text="Active Rooms", font=("arial", 16, "bold"), fg="#000000",
                                bg="sky blue")
        self.label_room.grid(row=0, column=0, columnspan=4)

        self.label_search1 = Label(self.frame2, text="Search By", font=("arial", 16, "bold"), fg="#000000",
                                   bg="sky blue")
        self.label_search1.grid(row=1, column=0, padx=5, pady=5)
        self.combo_search1 = ttk.Combobox(self.frame2, values=['room_status', 'room_description'], state='readonly')
        self.combo_search1.grid(row=1, column=1, padx=5, pady=5)
        self.entry_search1 = Entry(self.frame2)
        self.entry_search1.grid(row=1, column=2, padx=5, pady=5)
        self.btn_search1 = Button(self.frame2, text="Search", font=("arial", 16, "bold"), bg="sky blue",
                                  activebackground="blue", command=self.on_room_search)
        self.btn_search1.grid(row=1, column=3, sticky=E, padx=5, pady=5)

        self.room_tree = ttk.Treeview(self.frame2, columns=('Room No', 'Category', 'Description', 'Price', 'Status'))
        self.room_tree.grid(row=3, column=0, columnspan=4)
        self.room_tree['show'] = 'headings'
        self.room_tree.column('Room No', width=75)
        self.room_tree.column('Category', width=100)
        self.room_tree.column('Description', width=200)
        self.room_tree.column('Price', width=75)
        self.room_tree.column('Status', width=125)
        self.room_tree.heading('Room No', text="Room No")
        self.room_tree.heading('Category', text="Category")
        self.room_tree.heading('Description', text="Description")
        self.room_tree.heading('Price', text="Price")
        self.room_tree.heading('Status', text="Status")
        self.scroll = ttk.Scrollbar(self.frame2, orient="vertical", command=self.room_tree.yview)
        self.scroll.grid(row=3, column=0, columnspan=4, sticky='e' + 'ns')
        self.room_tree.configure(yscrollcommand=self.scroll.set)

        self.show_room_tree()

        self.label_booking = Label(self.frame2, text="Active Bookings", font=("arial", 16, "bold"), fg="#000000",
                                   bg="sky blue")
        self.label_booking.grid(row=11, column=0, columnspan=4, padx=5, pady=5)

        self.book_tree = ttk.Treeview(self.frame2, columns=('1', '2', '3', '4', '5'))
        self.book_tree.grid(row=14, column=0, columnspan=4)
        self.book_tree['show'] = 'headings'
        self.book_tree.column('1', width=75)
        self.book_tree.column('2', width=150)
        self.book_tree.column('3', width=75)
        self.book_tree.column('4', width=125)
        self.book_tree.column('5', width=150)
        self.book_tree.heading('1', text="ID")
        self.book_tree.heading('2', text="Name")
        self.book_tree.heading('3', text="Room")
        self.book_tree.heading('4', text="Check_In")
        self.book_tree.heading('5', text="est.CheckOUT")
        self.scroll = ttk.Scrollbar(self.frame2, orient="vertical", command=self.book_tree.yview)
        self.scroll.grid(row=14, column=0, columnspan=4, sticky='e' + 'ns')
        self.book_tree.configure(yscrollcommand=self.scroll.set)

        self.show_book_tree()

        self.btn_out = Button(self.frame2, text="Check Out", width=20, font=("arial", 16, "bold"), bg="sky blue",
                              activebackground="blue", command=self.on_check_out)
        self.btn_out.grid(row=15, column=2, columnspan=2, sticky=E, padx=5, pady=5)

        self.window.mainloop()

    def date_time(self):
        d = datetime.now()
        today = '{:%B %d, %Y}'.format(d)
        my_time = time.strftime('%I:%M:%S %p')
        self.lblInfo.config(text=('Time: ' + my_time + '     Date: ' + today))
        self.lblInfo.after(200, self.date_time)

    def combo_rooms(self):
        ret = Room()
        data = ret.available_rooms()
        self.combo_room['values'] = data

    def on_room_search(self):
        category = self.combo_search1.get()
        value = self.entry_search1.get()
        if category == "" or value == "":
            messagebox.showerror("Error", "Enter all the values for searching")
        else:
            self.room_tree.delete(*self.room_tree.get_children())
            ret = Room()
            data = ret.search_rooms(category, value)
            for i in data:
                self.room_tree.insert("", "end", text=i[0], values=i)

    def show_room_tree(self):
        self.room_tree.delete(*self.room_tree.get_children())
        ret = Room()
        data = ret.show_rooms_stat()
        for i in data:
            self.room_tree.insert("", "end", text=i[0], values=i)
        self.room_tree.bind("<Double-1>", self.send_room)

    def send_room(self, event):
        selected_item = self.room_tree.selection()[0]
        self.room_index = self.room_tree.item(selected_item, 'text')
        room_data = self.room_tree.item(selected_item, 'values')
        self.entry_room1.delete(0, END)
        self.entry_room1.insert(0, room_data[0])

    def show_book_tree(self):
        self.book_tree.delete(*self.book_tree.get_children())
        ret = Booking()
        data = ret.show_active_booking()
        for i in data:
            self.book_tree.insert("", "end", text=i[0], values=i)

    def on_save_click(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()
        email = self.entry_email.get()
        staying = self.combo_stay.get()
        room = self.combo_room.get()
        adults = self.entry_adult.get()
        children = self.entry_child.get()
        if not staying.isnumeric() or not adults.isnumeric() or not room.isnumeric():
            messagebox.showerror("Error", "Enter Number for adults and children and staying days")
        else:
            check_in = datetime.now().strftime('%Y/%m/%d')
            stay = datetime.now() + timedelta(days=int(staying))
            check_out = '{:%Y/%m/%d}'.format(stay)
            status = "Occupied"

            save = Booking()
            stat = Room()

            if name == "" or room == "":
                messagebox.showerror("Error", "Name and Room No is must")

            else:
                if save.new_booking(name, phone, address, email, check_in, check_out, room, adults, children):
                    stat.change_status(status, room)
                    a = messagebox.showinfo('Success', 'Room Booked successfully')
                    if a == 'ok':
                        self.on_reset_click()
                        self.show_room_tree()
                        self.show_book_tree()
                        self.combo_rooms()
                else:
                    messagebox.showerror('Booking Failed', 'Please Try Again')

    def on_reset_click(self):
        self.entry_name.delete(0, END)
        self.entry_phone.delete(0, END)
        self.entry_address.delete(0, END)
        self.entry_email.delete(0, END)
        self.combo_stay.set("")
        self.combo_room.set("")
        self.entry_adult.delete(0, END)
        self.entry_child.delete(0, END)
        self.combo_search1.set("")
        self.entry_search1.delete(0, END)
        self.entry_room1.delete(0, END)
        self.combo_change.set("")
        self.show_room_tree()
        self.show_book_tree()

    def on_room_change(self):
        room_no = self.entry_room1.get()
        room_stat = self.combo_change.get()
        if room_stat == "":
            messagebox.showerror("Error", "Select the current room status")
        else:
            ret = Room()
            ret.change_status(room_stat, room_no)
            self.show_room_tree()

    def on_check_out(self):
        try:
            user = self.user[2]
            check_out = datetime.now().strftime('%Y/%m/%d')
            selected_item = self.book_tree.selection()[0]
            self.book_index = self.book_tree.item(selected_item, 'text')
            book_data = self.book_tree.item(selected_item, 'values')
            booking_id = book_data[0]
            up = Booking()
            up.check_out(check_out, booking_id)
            BillView(booking_id, user)
        except IndexError:
            messagebox.showerror("Check Out Error", "Select the customer from active bookings")

    def open_login(self):
        self.window.withdraw()
        self.newwindow = Toplevel(self.window)
        from Login import Login
        Login(self.newwindow)

    def open_register(self):
        self.newwindow = Toplevel(self.window)
        Register(self.newwindow)

    def open_rooms(self):
        self.newwindow = Toplevel(self.window)
        Rooms(self.newwindow)

    def open_booking(self):
        self.newwindow = Toplevel(self.window)
        Bookings(self.newwindow)

    def exit_handler(self):
        a = messagebox.askyesno("EXIT", "Are you sure you want to exit")
        if a == 1:
            self.window.destroy()
