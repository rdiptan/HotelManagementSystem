from tkinter import *
from tkinter import ttk
from Connection import Bill


class Bookings:
    """
            This class shows past customer details.

            Methods:
                show_pay_tree()
                search_by_data()
                sear_item()

            """

    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x768+0+0")
        self.window.configure(bg="sky blue")

        self.title = Label(self.window, text="Payments", font=("arial", 16, "bold"), fg="navy blue",
                           bg="sky blue").pack()
        self.line = Canvas(self.window, width=1200, height=2, bg="navy blue").pack()

        self.frame1 = Frame(self.window, bg="sky blue")
        self.frame1.pack()

        self.bg_search = PhotoImage(file="Pictures/search.png")
        self.bg_back = PhotoImage(file="Pictures/back.png")

        self.label_ser = Label(self.frame1, text="Search for:", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_ser.grid(row=0, column=0, padx=5, pady=5)
        self.item_ser = Entry(self.frame1, font=("arial", 18))
        self.item_ser.grid(row=0, column=1, padx=5, pady=5)

        self.btn_ser = Button(self.frame1, text="Search", command=self.ser_item, width=20, font=("arial", 16, "bold"),
                              bg="sky blue", activebackground="blue", image=self.bg_search, compound=LEFT)
        self.btn_ser.grid(row=0, column=2, padx=5, pady=5, sticky=W + E)

        self.label_1 = Label(self.frame1, text="From (DD/MM/YYYY)", font=("arial", 18, "bold"), fg="#000000", bg="sky "
                                                                                                                 "blue")
        self.label_1.grid(row=1, column=0, padx=5, pady=5)
        self.combo_day1 = ttk.Combobox(self.frame1, values=[x for x in range(1, 33)], justify='right', width=8,
                                       font=("arial", 18))
        self.combo_day1.grid(row=1, column=1, sticky=NW, padx=5, pady=5)
        self.combo_month1 = ttk.Combobox(self.frame1, values=[x for x in range(1, 13)], justify='right', width=8,
                                         font=("arial", 18))
        self.combo_month1.grid(row=1, column=1, padx=5, pady=5)
        self.combo_year1 = ttk.Combobox(self.frame1, values=[x for x in range(2020, 1970, -1)], justify='right',
                                        width=8,
                                        font=("arial", 18))
        self.combo_year1.grid(row=1, column=1, sticky=NE, padx=5, pady=5)

        self.label_2 = Label(self.frame1, text="To (DD/MM/YYYY)", font=("arial", 18, "bold"), fg="#000000", bg="sky "
                                                                                                               "blue")
        self.label_2.grid(row=4, column=0, padx=5, pady=5)
        self.combo_day2 = ttk.Combobox(self.frame1, values=[x for x in range(1, 33)], justify='right', width=8,
                                       font=("arial", 18))
        self.combo_day2.grid(row=4, column=1, sticky=NW, padx=5, pady=5)
        self.combo_month2 = ttk.Combobox(self.frame1, values=[x for x in range(1, 13)], justify='right', width=8,
                                         font=("arial", 18))
        self.combo_month2.grid(row=4, column=1, padx=5, pady=5)
        self.combo_year2 = ttk.Combobox(self.frame1, values=[x for x in range(2020, 1970, -1)], justify='right',
                                        width=8,
                                        font=("arial", 18))
        self.combo_year2.grid(row=4, column=1, sticky=NE, padx=5, pady=5)

        self.btn_search = Button(self.frame1, text="Search", width=20, font=("arial", 16, "bold"), bg="sky blue",
                                 activebackground="yellow", command=self.search_by_date,
                                 image=self.bg_search, compound=LEFT)
        self.btn_search.grid(row=5, column=1, padx=5, sticky=W + E, pady=5)

        # tree view
        self.pay_tree = ttk.Treeview(self.frame1, columns=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'),
                                     height=20)
        self.pay_tree.grid(row=14, column=0, columnspan=4, sticky=E + W)
        self.pay_tree['show'] = 'headings'
        self.pay_tree.column('1', width=100)
        self.pay_tree.column('2', width=150)
        self.pay_tree.column('3', width=100)
        self.pay_tree.column('4', width=100)
        self.pay_tree.column('5', width=75)
        self.pay_tree.column('6', width=75)
        self.pay_tree.column('7', width=125)
        self.pay_tree.column('8', width=125)
        self.pay_tree.column('9', width=75)
        self.pay_tree.column('10', width=50)
        self.pay_tree.column('11', width=75)
        self.pay_tree.heading('1', text="Name")
        self.pay_tree.heading('2', text="Address")
        self.pay_tree.heading('3', text="Mobile")
        self.pay_tree.heading('4', text="Amount")
        self.pay_tree.heading('5', text="Discount")
        self.pay_tree.heading('6', text="Type")
        self.pay_tree.heading('7', text="Check IN")
        self.pay_tree.heading('8', text="Check OUT")
        self.pay_tree.heading('9', text="Room")
        self.pay_tree.heading('10', text="Adults")
        self.pay_tree.heading('11', text="Child")
        self.scroll = ttk.Scrollbar(self.frame1, orient="vertical", command=self.pay_tree.yview)
        self.scroll.grid(row=14, column=0, columnspan=4, sticky='e' + 'ns')
        self.pay_tree.configure(yscrollcommand=self.scroll.set)

        self.show_pay_tree()

        self.btn_back = Button(self.frame1, text="Back", command=self.window.destroy, width=20, bg="sky blue",
                               font=("arial", 16, "bold"), activebackground="red", image=self.bg_back, compound=LEFT)
        self.btn_back.grid(row=15, column=0, padx=5, pady=5, sticky=W + E)

    def show_pay_tree(self):
        """returns checked out customer details"""
        self.pay_tree.delete(*self.pay_tree.get_children())
        ret = Bill()
        data = ret.view_bill()
        for i in data:
            self.pay_tree.insert("", "end", text=i[0], values=i)

    def search_by_date(self):
        """returns the detail of certain time period"""
        d1 = str(self.combo_year1.get()) + '-' + str(self.combo_month1.get()) + '-' + str(self.combo_day1.get())
        d2 = str(self.combo_year2.get()) + '-' + str(self.combo_month2.get()) + '-' + str(self.combo_day2.get())
        self.pay_tree.delete(*self.pay_tree.get_children())
        ret = Bill()
        data = ret.search_by_date(d1, d2)
        for i in data:
            self.pay_tree.insert("", "end", text=i[0], values=i)
        ret = Bill()
        data = ret.search_by_date_sum(d1, d2)
        self.label_2 = Label(self.frame1, text=("Total income: Rs." + str(data[0][0])), font=("arial", 16, "bold"),
                             fg="#000000", bg="sky blue")
        self.label_2.grid(row=15, column=3, columnspan=2)

    def ser_item(self):
        """search in pay tree"""
        search = self.item_ser.get()
        self.pay_tree.delete(*self.pay_tree.get_children())
        ret = Bill()
        data = ret.search(search)
        for i in data:
            self.pay_tree.insert("", "end", text=i[0], values=i)


def main():
    wn = Tk()
    wn.title("Hotel Management System")
    Bookings(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()
