from tkinter import *
from tkinter import messagebox
from Connection import Staff
from Dashboard import Dashboard


class Login:
    def __init__(self, window):
        self.window = window
        self.window.title("Hotel Management System")
        self.window.geometry("550x300+450+200")

        self.window.configure(bg="sky blue")

        self.window.resizable(0, 0)

        self.un = StringVar()
        self.pw = StringVar()

        canvas = Canvas()
        self.bg_entry = PhotoImage(file="hotel2.png")
        new_image = self.bg_entry.subsample(5, 10)
        canvas.create_image(0, 0, image=new_image, anchor="nw")
        self.canvas_image = new_image

        self.bg_uname = PhotoImage(file="u25.png")
        self.bg_pass = PhotoImage(file="p25.png")

        self.title0 = Label(self.window, text="Please Login", image=self.canvas_image, compound=LEFT,
                                font=('Arial', 24, 'bold'), bg="sky blue")
        self.title0.pack(pady=10)

        self.frame_login = Frame(self.window, bg="sky blue")
        self.frame_login.pack()

        self.label_un = Label(self.frame_login, text="Username", image=self.bg_uname, compound=LEFT,
                              font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_un.grid(row=0, column=0, padx=5, pady=5)
        self.entry_un = Entry(self.frame_login, font=("arial", 18), textvariable=self.un)
        self.entry_un.grid(row=0, column=1, padx=5, pady=5)
        self.entry_un.focus()

        self.label_pw = Label(self.frame_login, text="Password", image=self.bg_pass, compound=LEFT,
                              font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_pw.grid(row=1, column=0, padx=5, pady=5)
        self.entry_pw = Entry(self.frame_login, font=("arial", 18), textvariable=self.pw)
        self.entry_pw.default_show_val = self.entry_pw["show"]
        self.entry_pw["show"] = "*"
        self.entry_pw.grid(row=1, column=1, padx=5, pady=5)

        self.check = IntVar()
        self.pa = Checkbutton(self.frame_login, bg="#ffffff", variable=self.check, command=self.show)
        self.pa.place(x=390, y=55)

        self.btn_login = Button(self.frame_login, text="Log In", width=20, font=("arial", 16, "bold"), bg="sky blue",
                                activebackground="blue", command=self.on_login_click)
        self.btn_login.grid(row=2, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)

        self.btn_reset = Button(self.frame_login, text="Reset", font=("arial", 16, "bold"), bg="sky blue",
                                activebackground="yellow", command=self.on_reset_click)
        self.btn_reset.grid(row=3, column=0, sticky=W+E, padx=5, pady=5)

        self.btn_exit = Button(self.frame_login, text="Exit", font=("arial", 16, "bold"), bg="sky blue",
                               activebackground="red", command=self.window.withdraw)
        self.btn_exit.grid(row=3, column=1, sticky=W+E, padx=5, pady=5)

        self.title1 = Label(self.window, text="You are accessing the portal of ### Hotel Pvt. Ltd.\n "
                                              "Any misuse will be against hotel law. And addressed as Federal crime.",
                            font=("arial", 8, "bold"), fg="#000000", bg="sky blue")
        self.title1.pack(side=BOTTOM)

        self.line = Canvas(self.window, width=500, height=2, bg="#ffffff").pack(side=BOTTOM)

    def on_login_click(self):
        username = self.un.get()
        password = self.pw.get()
        valid = Staff()
        if username == "" or password == "":
            messagebox.showerror("Error", "Enter all values")
        else:
            usr = valid.login(username, password)
            if len(usr) > 0:
                self.window.destroy()
                Dashboard(usr[0])
            else:
                messagebox.showerror('Error', 'Wrong id or password')

    def on_reset_click(self):
        self.entry_un.delete(0, END)
        self.entry_pw.delete(0, END)

    def show(self):
        if self.check.get() == 0:
            self.entry_pw["show"] = "*"
        else:
            self.entry_pw["show"] = ""


def main():
    wn = Tk()
    Login(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()