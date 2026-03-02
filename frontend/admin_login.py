import tkinter as tk
from tkinter import messagebox
from backend.auth import login_admin
from frontend.admin_dashboard import open_admin_dashboard


def open_admin_login_window():
    window = tk.Tk()
    window.title("CineBook - Admin Login")
    window.state("zoomed")
    window.configure(bg="#e6e6e6")
    window.resizable(False, False)

    # Center Card 
    card = tk.Frame(window, bg="white",highlightthickness=1,highlightbackground="#d0d0d0")
    card.place(relx=0.5, rely=0.5, anchor="center",
    width=420, height=360)

    # Back Function 
    def go_back():
        window.destroy()
        from frontend.login import open_login
        open_login()

    # Top Row (Back Button) 
    top_row = tk.Frame(card, bg="white")
    top_row.pack(fill="x", pady=(10, 0), padx=10)

    tk.Button(top_row,text="← Back",bg="white",fg="#2c3e50",font=("Arial", 10, "bold"),relief="flat",bd=0,command=go_back
    ).pack(side="left")

    # Title
    tk.Label(card, text="Admin Login", font=("Arial", 20, "bold"), bg="white").pack(pady=20)

    #  Email
    tk.Label(card text="Admin Email", bg="white").pack(anchor="w", padx=95, pady=(5,2))

    email_entry = tk.Entry(card,width=30,relief="flat",highlightthickness=1,highlightbackground="#cccccc")
    email_entry.pack(pady=(0,8), ipady=4)

    # Password 
    tk.Label(card,text="Password",bg="white").pack(anchor="w", padx=95, pady=(5,2))

    password_entry = tk.Entry(card,width=30,show="*",relief="flat",highlightthickness=1,highlightbackground="#cccccc")
    password_entry.pack(pady=(0,15), ipady=4)

    #  Login Action 
    def admin_login():
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if email == "" or password == "":
            messagebox.showerror("Error", "Please enter email and password")
            return

        admin = login_admin(email, password)

        if admin:
            window.destroy()
            open_admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid admin credentials!")

    #  Login Button 
    tk.Button(card,text="Login",bg="#2c3e50",fg="white",width=22,height=2,bd=0,command=admin_login).pack(pady=10)

    window.mainloop()