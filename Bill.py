from tkinter import *
from tkinter import ttk
from Connection import Bill
from Connection import Booking
from Connection import Room
from tkinter import messagebox


class BillView:
    """
            This class process billing of the customer.

            Methods:
                on_gen_click()
                on_return_click()
                order_bill()
                on_pay_click()

            """
    def __init__(self, cus_id, user):
        self.window = Toplevel()
        self.window.title("Hotel Management System")
        self.window.geometry("1366x768+0+0")
        self.window.configure(bg="sky blue")

        self.bg_pay = PhotoImage(file="Pictures/money.png")
        self.bg_gen = PhotoImage(file="Pictures/generate.png")
        self.bg_calc = PhotoImage(file="Pictures/calculate.png")

        self.id = cus_id
        self.user = user

        # customer stay details
        ret = Bill()
        val = ret.room_bill(self.id)
        data = val[0]

        # calculate hotel stay days from checked in and checking out date
        self.room_no = data[3]
        self.days = abs(data[1]-data[2]).days
        self.tot = float(data[4])*int(self.days)

        # calculating amount owe to hotel
        global total
        global total_bill
        ret = Bill()
        order_amt = ret.total_order(self.id)
        for i in order_amt:
            total = i[0]
        try:
            total_bill = self.tot + total
        except TypeError:
            total_bill = self.tot

        # bill ui
        self.frame1 = Frame(self.window, bg="sky blue")
        self.frame1.place(x=350)

        self.hotel = Label(self.frame1, text='### Hotel Pvt.Ltd.', font=("arial", 20, "bold"), fg="navy blue",
                           bg="sky blue")
        self.hotel.grid(row=0, column=0)

        self.address = Label(self.frame1, text='Kathmandu, Nepal', font=("arial", 16, "bold"), fg="navy blue",
                             bg="sky blue")
        self.address.grid(row=1, column=0)

        self.phone = Label(self.frame1, text='01-1234567', font=("arial", 16, "bold"), fg="navy blue", bg="sky blue")
        self.phone.grid(row=2, column=0)

        self.line = Canvas(self.frame1, width=500, height=2, bg="navy blue").grid(row=3)

        self.name = Label(self.frame1, text='Name: '+data[0], font=("arial", 16), fg="#000000", bg="sky blue")
        self.name.grid(row=5, column=0, sticky=W)

        self.room = Label(self.frame1, text='Room No: '+self.room_no, font=("arial", 16), fg="#000000", bg="sky blue")
        self.room.grid(row=6, column=0, sticky=W)

        self.stay = Label(self.frame1, text='Stay: '+str(data[1])+' to '+str(data[2]), font=("arial", 16),
                          fg="#000000", bg="sky blue")
        self.stay.grid(row=7, column=0, sticky=W)

        self.bill_by = Label(self.frame1, text='Bill By: '+user, font=("arial", 16), fg="#000000", bg="sky blue")
        self.bill_by.grid(row=8, column=0, sticky=W)

        self.bill_tree = ttk.Treeview(self.frame1, columns=('name', 'price', 'qty', 'amt'))
        self.bill_tree.grid(row=10, column=0)
        self.bill_tree['show'] = 'headings'
        self.bill_tree.column('name', width=200)
        self.bill_tree.column('price', width=100)
        self.bill_tree.column('qty', width=100)
        self.bill_tree.column('amt', width=100)
        self.bill_tree.heading('name', text="Name")
        self.bill_tree.heading('price', text="Rate")
        self.bill_tree.heading('qty', text="Qty")
        self.bill_tree.heading('amt', text="Amount")
        self.scroll = ttk.Scrollbar(self.frame1, orient="vertical", command=self.bill_tree.yview)
        self.scroll.grid(row=10, column=0, columnspan=4, sticky='e' + 'ns')
        self.bill_tree.configure(yscrollcommand=self.scroll.set)

        self.bill_tree.insert("", "end", text="", values=("Room Bill", data[4], self.days, self.tot))

        self.total = Label(self.frame1, text='Total Amount', font=("arial", 16), fg="#000000", bg="sky blue")
        self.total.grid(row=11, column=0, sticky=E+W)
        self.total_amt = Label(self.frame1, text=total_bill, font=("arial", 16), fg="#000000", bg="sky blue")
        self.total_amt.grid(row=11, column=0, sticky=E)

        self.discount = Label(self.frame1, text='Discount %', font=("arial", 16), fg="#000000", bg="sky blue")
        self.discount.grid(row=12, column=0, sticky=E+W)
        self.entry_discount = Entry(self.frame1, font=("arial", 16), width=13)
        self.entry_discount.grid(row=12, column=0, sticky=E)
        self.btn_generate = Button(self.frame1, text="Generate", font=("arial", 16, "bold"), bg="sky blue",
                                   activebackground="blue", command=self.on_gen_click, image=self.bg_gen, compound=LEFT)
        self.btn_generate.grid(row=13, column=0, sticky=E)

        self.lbl_grand_total = Label(self.frame1, text='Grand Total', font=("arial", 16), fg="#000000", bg="sky blue")
        self.lbl_grand_total.grid(row=14, column=0, sticky=E+W)
        self.grand_total = Label(self.frame1, font=("arial", 16), fg="#000000", bg="sky blue")
        self.grand_total.grid(row=14, column=0, sticky=E)

        self.payment = Label(self.frame1, text='Payment Mode', font=("arial", 16), fg="#000000", bg="sky blue")
        self.payment.grid(row=15, column=0, sticky=E+W)
        self.combo_pay = ttk.Combobox(self.frame1, values=['Cash', 'Card', 'Cheque', 'Online'], width=12,
                                      font=("arial", 16))
        self.combo_pay.grid(row=15, column=0, sticky=E)

        self.tender = Label(self.frame1, text='Tender', font=("arial", 16), fg="#000000", bg="sky blue")
        self.tender.grid(row=16, column=0, sticky=E+W)
        self.entry_tend = Entry(self.frame1, font=("arial", 16), width=13)
        self.entry_tend.grid(row=16, column=0, sticky=E)

        self.ret = Button(self.frame1, text='Return', font=("arial", 16, "bold"), bg="sky blue",
                          activeforeground="blue", command=self.on_return_click, image=self.bg_calc, compound=LEFT)
        self.ret.grid(row=17, column=0)
        self.ret_amt = Label(self.frame1, font=("arial", 16), fg="#000000", bg="sky blue")
        self.ret_amt.grid(row=17, column=0, sticky=E)

        self.btn_pay = Button(self.frame1, text="PAY", width=20, font=("arial", 16, "bold"), bg="sky blue",
                              activebackground="blue", command=self.on_pay_click, image=self.bg_pay, compound=LEFT)
        self.btn_pay.grid(row=18, column=0, sticky=W+E, padx=5, pady=5)

        self.order_bill()

        self.window.mainloop()

    def on_gen_click(self):
        """apply discount to total amount"""
        amt = total_bill
        dis = self.entry_discount.get()
        if dis == "" or not dis.isnumeric():
            messagebox.showerror("Error", "Please enter a value for discount")
        total = amt - ((int(dis)/100)*amt)
        self.grand_total['text'] = total

    def on_return_click(self):
        """calculate returns change amount - works as calculator"""
        ten = int(self.entry_tend.get())
        change = ten-float(self.grand_total.cget("text"))
        self.ret_amt['text'] = change

    def order_bill(self):
        """show bills details in treeview"""
        ret = Bill()
        data = ret.order_bill(self.id)
        for i in data:
            self.bill_tree.insert("", "end", text=i[0], value=(i[0], i[1], i[2], i[3]))

    def on_pay_click(self):
        """save payment details to database"""
        booking_id = self.id
        discount = self.entry_discount.get()
        paid_amount = self.grand_total.cget("text")
        payment_type = self.combo_pay.get()
        billed_by = self.user
        status = "Cleaning"
        if paid_amount == "":
            messagebox.showerror('Payment Failed', 'Please add a discount value and press generate button\n'
                                                   'if no discount is given enter 0')
        elif payment_type == "":
            messagebox.showerror('Payment Failed', 'Please select payment mode')
        else:
            room = self.room_no
            save = Bill()
            if save.save_payment(booking_id, discount, paid_amount, payment_type, billed_by):
                a = messagebox.showinfo('Success', 'Bill Paid successfully')
                up = Booking()
                up.booking_stat(booking_id)
                stat = Room()
                stat.change_status(status, room)
                if a == 'ok':
                    self.window.destroy()
            else:
                messagebox.showerror('Payment Failed', 'Please Try Again')
