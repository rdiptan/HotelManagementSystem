from tkinter import *
from tkinter import messagebox
import sys
from Connection import Staff
from Dashboard import Dashboard


class Login:
    """
        This class provides login form to use the programme.

        Methods:
            on_login_click()
            on_reset_lick()
            show()
            exit_handler()

        """

    def __init__(self, window):
        self.root = window
        self.root.title("Hotel Management System")
        self.root.geometry("600x300+400+200")

        self.root.configure(bg="sky blue")

        self.root.resizable(0, 0)

        self.un = StringVar()
        self.pw = StringVar()

        # images
        canvas = Canvas()
        self.bg_entry = PhotoImage(file="Pictures/hotel2.png")
        new_image = self.bg_entry.subsample(5, 10)
        canvas.create_image(0, 0, image=new_image, anchor="nw")
        self.canvas_image = new_image

        self.bg_uname = PhotoImage(file="Pictures/uname.png")
        self.bg_pass = PhotoImage(file="Pictures/password.png")
        self.bg_log = PhotoImage(file="Pictures/logout.png")
        self.bg_reset = PhotoImage(file="Pictures/reset.png")
        self.bg_exit = PhotoImage(file="Pictures/exit.png")

        # title
        self.title0 = Label(self.root, text="Please Login", image=self.canvas_image, compound=LEFT,
                            font=('Arial', 24, 'bold'), bg="sky blue")
        self.title0.pack(pady=10)

        # frame
        self.frame_login = Frame(self.root, bg="sky blue")
        self.frame_login.pack()

        # user name
        self.label_un = Label(self.frame_login, text=" Username", image=self.bg_uname, compound=LEFT,
                              font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_un.grid(row=0, column=0, padx=5, pady=5)
        self.entry_un = Entry(self.frame_login, font=("arial", 18), textvariable=self.un)
        self.entry_un.grid(row=0, column=1, padx=5, pady=5)
        self.entry_un.focus()

        # password
        self.label_pw = Label(self.frame_login, text=" Password", image=self.bg_pass, compound=LEFT,
                              font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.label_pw.grid(row=1, column=0, padx=5, pady=5)
        self.entry_pw = Entry(self.frame_login, font=("arial", 18), textvariable=self.pw)
        self.entry_pw.default_show_val = self.entry_pw["show"]
        self.entry_pw["show"] = "*"
        self.entry_pw.grid(row=1, column=1, padx=5, pady=5)

        # checkbutton for password view
        self.check = IntVar()
        self.pa = Checkbutton(self.frame_login, bg="#ffffff", variable=self.check, command=self.show)
        self.pa.place(x=400, y=55)

        # login button
        self.btn_login = Button(self.frame_login, text="Log In", width=20, font=("arial", 16, "bold"), bg="sky blue",
                                activebackground="blue", command=self.on_login_click, image=self.bg_log, compound=LEFT)
        self.btn_login.grid(row=2, column=0, columnspan=2, sticky=W + E, padx=5, pady=5)

        # reset button
        self.btn_reset = Button(self.frame_login, text="Reset", width=20, font=("arial", 16, "bold"), bg="sky blue",
                                activebackground="yellow", command=self.on_reset_click, image=self.bg_reset,
                                compound=LEFT)
        self.btn_reset.grid(row=3, column=0, sticky=W + E, padx=5, pady=5)

        # quit button
        self.btn_exit = Button(self.frame_login, text="Exit", width=20, font=("arial", 16, "bold"), bg="sky blue",
                               activebackground="red", command=self.exit_handler, image=self.bg_exit, compound=LEFT)
        self.btn_exit.grid(row=3, column=1, sticky=W + E, padx=5, pady=5)

        # disclaimer
        self.title1 = Label(self.root, text="You are accessing the portal of ### Hotel Pvt. Ltd.\n "
                                            "Any misuse will be against hotel law. And addressed as Federal crime.",
                            font=("arial", 8, "bold"), fg="#000000", bg="sky blue")
        self.title1.pack(side=BOTTOM)

        # separation line
        self.line = Canvas(self.root, width=500, height=2, bg="#ffffff").pack(side=BOTTOM)

    def on_login_click(self):
        """check for if input fields are empty or not then verify the user id and password
                and then logged into the system"""
        username = self.un.get()
        password = self.pw.get()
        valid = Staff()
        if username == "" or password == "":
            messagebox.showerror("Error", "Enter all values")
        else:
            usr = valid.login(username, password)
            if len(usr) > 0:
                self.root.destroy()
                Dashboard(usr[0])
            else:
                messagebox.showerror('Error', 'Wrong id or password')

    def on_reset_click(self):
        """resets the input values to blank"""
        self.entry_un.delete(0, END)
        self.entry_pw.delete(0, END)

    def show(self):
        """shows the password if checkbutton is clicked"""
        if self.check.get() == 0:
            self.entry_pw["show"] = "*"
        else:
            self.entry_pw["show"] = ""

    def exit_handler(self):
        """quits the application"""
        a = messagebox.askyesno("EXIT", "Are you sure you want to exit")
        if a == 1:
            self.root.destroy()
            sys.exit()


def main():
    wn = Tk()
    Login(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()
