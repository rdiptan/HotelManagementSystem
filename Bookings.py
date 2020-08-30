from tkinter import *
from tkinter import ttk
from Connection import Booking


class Bookings:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x768+0+0")
        self.window.configure(bg="sky blue")

        self.frame1 = Frame(self.window, bg="sky blue")
        self.frame1.pack()

        self.book_tree = ttk.Treeview(self.frame1, columns=('1', '2', '3', '4', '5'))
        self.book_tree.grid(row=14, column=0, columnspan=4, sticky=E + W)
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
        self.scroll = ttk.Scrollbar(self.frame1, orient="vertical", command=self.book_tree.yview)
        self.scroll.grid(row=14, column=0, columnspan=4, sticky='e' + 'ns')
        self.book_tree.configure(yscrollcommand=self.scroll.set)

        self.show_book_tree()

    def show_book_tree(self):
        self.book_tree.delete(*self.book_tree.get_children())
        ret = Booking()
        data = ret.show_active_booking()
        for i in data:
            self.book_tree.insert("", "end", text=i[0], values=i)


def main():
    wn = Tk()
    wn.title("Hotel Management System")
    Bookings(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()
