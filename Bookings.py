from tkinter import *
from tkinter import ttk
from Connection import Booking
from Connection import Bill


class Bookings:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x768+0+0")
        self.window.configure(bg="sky blue")

        self.frame1 = Frame(self.window, bg="sky blue")
        self.frame1.pack()

        self.label_1 = Label(self.frame1, text="Bookings", font=("arial", 16, "bold"), fg="#000000",
                             bg="sky blue")
        self.label_1.grid(row=0, column=0, columnspan=4)
        self.book_tree = ttk.Treeview(self.frame1, columns=('1', '2', '3', '4', '5', '6', '7', '8', '9'))
        self.book_tree.grid(row=4, column=0, columnspan=4, sticky=E + W)
        self.book_tree['show'] = 'headings'
        self.book_tree.column('1', width=100)
        self.book_tree.column('2', width=150)
        self.book_tree.column('3', width=100)
        self.book_tree.column('4', width=150)
        self.book_tree.column('5', width=150)
        self.book_tree.column('6', width=50)
        self.book_tree.column('7', width=200)
        self.book_tree.column('8', width=50)
        self.book_tree.column('9', width=75)
        self.book_tree.heading('1', text="Name")
        self.book_tree.heading('2', text="Address")
        self.book_tree.heading('3', text="Mobile")
        self.book_tree.heading('4', text="Check IN")
        self.book_tree.heading('5', text="Check OUT")
        self.book_tree.heading('6', text="Room No")
        self.book_tree.heading('7', text="Room Category")
        self.book_tree.heading('8', text="Adults")
        self.book_tree.heading('9', text="Child")
        self.scroll = ttk.Scrollbar(self.frame1, orient="vertical", command=self.book_tree.yview)
        self.scroll.grid(row=4, column=0, columnspan=4, sticky='e' + 'ns')
        self.book_tree.configure(yscrollcommand=self.scroll.set)

        self.show_book_tree()

        self.label_2 = Label(self.frame1, text="Payments", font=("arial", 16, "bold"), fg="#000000",
                             bg="sky blue")
        self.label_2.grid(row=13, column=0, columnspan=4)
        self.pay_tree = ttk.Treeview(self.frame1, columns=('1', '2', '3', '4', '5', '6', '7', '8', '9'), height=15)
        self.pay_tree.grid(row=14, column=0, columnspan=4, sticky=E + W)
        self.pay_tree['show'] = 'headings'
        self.pay_tree.column('1', width=100)
        self.pay_tree.column('2', width=150)
        self.pay_tree.column('3', width=100)
        self.pay_tree.column('4', width=100)
        self.pay_tree.column('5', width=50)
        self.pay_tree.column('6', width=50)
        self.pay_tree.column('7', width=150)
        self.pay_tree.column('8', width=150)
        self.pay_tree.column('9', width=75)
        self.pay_tree.heading('1', text="Name")
        self.pay_tree.heading('2', text="Address")
        self.pay_tree.heading('3', text="Mobile")
        self.pay_tree.heading('4', text="Billed Amount")
        self.pay_tree.heading('5', text="Discount")
        self.pay_tree.heading('6', text="Payment Type")
        self.pay_tree.heading('7', text="Check IN")
        self.pay_tree.heading('8', text="Check OUT")
        self.pay_tree.heading('9', text="Room")
        self.scroll = ttk.Scrollbar(self.frame1, orient="vertical", command=self.pay_tree.yview)
        self.scroll.grid(row=14, column=0, columnspan=4, sticky='e' + 'ns')
        self.pay_tree.configure(yscrollcommand=self.scroll.set)

        self.show_pay_tree()

    def show_book_tree(self):
        self.book_tree.delete(*self.book_tree.get_children())
        ret = Booking()
        data = ret.view_booking()
        for i in data:
            self.book_tree.insert("", "end", text=i[0], values=i)

    def show_pay_tree(self):
        self.pay_tree.delete(*self.pay_tree.get_children())
        ret = Bill()
        data = ret.view_bill()
        for i in data:
            self.pay_tree.insert("", "end", text=i[0], values=i)


def main():
    wn = Tk()
    wn.title("Hotel Management System")
    Bookings(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()
