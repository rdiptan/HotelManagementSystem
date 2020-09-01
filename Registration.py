from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Connection import Staff


class Register:
    """
        This class provides a form to register new users.

        Methods:
            on_register_click()
            on_reset_click()
            on_back_click()
            search_user()
            binary_search()

        """
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x768+0+0")
        self.window.configure(bg="sky blue")

        # label frame
        self.frame = LabelFrame(self.window, bg="sky blue", fg="white", text="User Register",
                                font=("arial", 20, "bold"), bd=10, padx=25, pady=25)
        self.frame.pack(padx=25, pady=25)

        # username
        self.label_un = Label(self.frame, text="Username", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_un.grid(row=0, column=0, padx=5, pady=5)
        self.entry_un = Entry(self.frame, font=("arial", 18))
        self.entry_un.grid(row=0, column=1, padx=5, pady=5)

        # name
        self.label_name = Label(self.frame, text="Name", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_name.grid(row=1, column=0, padx=5, pady=5)
        self.entry_name = Entry(self.frame, font=("arial", 18))
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        # gender
        self.label_gender = Label(self.frame, text="Gender", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_gender.grid(row=2, column=0, padx=5, pady=5)
        self.combo_gender = ttk.Combobox(self.frame, values=['Male', 'Female', 'Others'], width=19, font=("arial", 18))
        self.combo_gender.grid(row=2, column=1, padx=5, pady=5)

        # date of birth
        self.label_dob = Label(self.frame, text="DOB (DD/MM/YYYY)", font=("arial", 18, "bold"), fg="#000000", bg="sky "
                                                                                                                 "blue")
        self.label_dob.grid(row=3, column=0, padx=5, pady=5)
        self.combo_day = ttk.Combobox(self.frame, values=[x for x in range(1, 33)], justify='right', width=6,
                                      font=("arial", 18))
        self.combo_day.grid(row=3, column=1, sticky=NW, padx=5, pady=5)
        self.combo_month = ttk.Combobox(self.frame, values=[x for x in range(1, 13)], justify='right', width=5,
                                        font=("arial", 18))
        self.combo_month.grid(row=3, column=1, padx=5, pady=5)
        self.combo_year = ttk.Combobox(self.frame, values=[x for x in range(2020, 1970, -1)], justify='right', width=6,
                                       font=("arial", 18))
        self.combo_year.grid(row=3, column=1, sticky=NE, padx=5, pady=5)

        # address
        self.label_address = Label(self.frame, text="Address", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_address.grid(row=4, column=0, padx=5, pady=5)
        self.entry_address = Entry(self.frame, font=("arial", 18))
        self.entry_address.grid(row=4, column=1, padx=5, pady=5)

        # phone
        self.label_phone = Label(self.frame, text="Phone", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_phone.grid(row=5, column=0, padx=5, pady=5)
        self.entry_phone = Entry(self.frame, font=("arial", 18))
        self.entry_phone.grid(row=5, column=1, padx=5, pady=5)

        # email
        self.label_email = Label(self.frame, text="Email", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_email.grid(row=6, column=0, padx=5, pady=5)
        self.entry_email = Entry(self.frame, font=("arial", 18))
        self.entry_email.grid(row=6, column=1, padx=5, pady=5)

        # password
        self.label_pass = Label(self.frame, text="Password", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_pass.grid(row=7, column=0, padx=5, pady=5)
        self.entry_pass = Entry(self.frame, font=("arial", 18), show='*')
        self.entry_pass.grid(row=7, column=1, padx=5, pady=5)

        # conforming password
        self.label_pw = Label(self.frame, text="Confirm Password", font=("arial", 18, "bold"), fg="#000000",
                              bg="sky blue")
        self.label_pw.grid(row=8, column=0, padx=5, pady=5)
        self.entry_pw = Entry(self.frame, font=("arial", 18), show='*')
        self.entry_pw.grid(row=8, column=1, padx=5, pady=5)

        self.label_type = Label(self.frame, text="Type", font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_type.grid(row=9, column=0, padx=5, pady=5)
        self.combo_type = ttk.Combobox(self.frame, values=['Admin', 'User'], width=19, font=("arial", 18))
        self.combo_type.grid(row=9, column=1, padx=5, pady=5)

        # register button
        self.btn_reg = Button(self.frame, text="Register", width=20, font=("arial", 16, "bold"), bg="sky blue",
                              activebackground="blue", command=self.on_register_click)
        self.btn_reg.grid(row=10, column=0, columnspan=2, sticky=W + E, padx=5, pady=5)

        # reset button
        self.btn_reset = Button(self.frame, text="Reset", width=20, font=("arial", 16, "bold"), bg="sky blue",
                                activebackground="yellow", command=self.on_reset_click)
        self.btn_reset.grid(row=11, column=0, sticky=W + E, padx=5, pady=5)

        # back button
        self.btn_back = Button(self.frame, text="Back", width=20, font=("arial", 16, "bold"), bg="sky blue",
                               activebackground="yellow", command=self.on_back_click)
        self.btn_back.grid(row=11, column=1, padx=5, sticky=W + E, pady=5)

    def on_register_click(self):
        """
                verify if user id is taken or not
                check if any values is left empty or not
                check for password match
                saves the user registration data in database

                """
        username = self.entry_un.get()
        pw = self.entry_pass.get()
        password = self.entry_pw.get()
        name = self.entry_name.get()
        dob = str(self.combo_year.get()) + '/' + str(self.combo_month.get()) + '/' + str(self.combo_day.get())
        gender = self.combo_gender.get()
        address = self.entry_address.get()
        mobile = self.entry_phone.get()
        email = self.entry_email.get()
        type_ = self.combo_type.get()

        res = self.search_user(username)

        if res:
            messagebox.showerror("Error", "Username is occupied")
        else:
            if username == "" or pw == "" or password == "" or name == "" or dob == "" or gender == "" or \
                    address == "" or mobile == "" or email == "" or type_ == "":
                messagebox.showerror("Error", "Enter all values")
            elif password != pw:
                messagebox.showerror("Error", "Passwords does not match")
            else:
                reg = Staff()
                if reg.register(username, password, name, dob, gender, address, mobile, email, type_):
                    a = messagebox.showinfo('Success', 'User Registered successfully')
                    if a == 'ok':
                        self.window.destroy()
                    else:
                        self.on_reset_click()
                else:
                    messagebox.showerror('Registration Failed', 'Please Try Again')

    def on_reset_click(self):
        """resets the input values to blank"""
        self.entry_un.delete(0, END)
        self.entry_name.delete(0, END)
        self.combo_gender.set("")
        self.combo_year.set("")
        self.combo_month.set("")
        self.combo_day.set("")
        self.entry_address.delete(0, END)
        self.entry_phone.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_pass.delete(0, END)
        self.entry_pw.delete(0, END)
        self.combo_type.set("")

    def on_back_click(self):
        """takes back to hotel management system homepage"""
        self.window.destroy()

    def search_user(self, username):
        """checks for username is already present or not"""
        reg = Staff()
        data = reg.check_username()
        result = (self.binary_search(data, username))
        if result != -1:
            return True
        else:
            return False

    def binary_search(self, list, key):
        """binary search algorithm"""
        start = 0
        end = len(list) - 1
        while start <= end:
            mid = (start + end) // 2
            if list[mid][0] == key:
                return mid
            elif list[mid][0] > key:
                end = mid - 1
            else:
                start = mid + 1
        return -1


def main():
    wn = Tk()
    wn.title("Hotel Management System")
    Register(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()
