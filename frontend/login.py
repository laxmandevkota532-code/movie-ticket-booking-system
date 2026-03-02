import tkinter as tk
from tkinter import messagebox
from backend.auth import login_user
from frontend.signup import open_signup
from frontend.user_dashboard import open_user_dashboard
from frontend.forgot_password import open_forgot_password
from frontend.admin_login import open_admin_login_window


def open_login():
    window = tk.Tk()
    window.title("CineBook - Login")
    window.state("zoomed")
    window.configure(bg="#e6e6e6")
    window.resizable(False, False)

    #  Center Card 
    card = tk.Frame(window, bg="white",highlightthickness=1,highlightbackground="#d0d0d0")
    card.place(relx=0.5, rely=0.5, anchor="center",
               width=420, height=380)

    #  Title
    tk.Label(card, text="User Login", font=("Arial", 20, "bold"), bg="white").pack(pady=25)

    #  Email 
    tk.Label(card, text="Email", bg="white").pack(anchor="w", padx=95, pady=(5,2))

    email_entry = tk.Entry(card,   width=30,   relief="flat",   highlightthickness=1,   highlightbackground="#cccccc")
    email_entry.pack(pady=(0,8), ipady=4)

    

    #Password 
    tk.Label(card, text="Password", bg="white").pack(anchor="w", padx=95, pady=(5,2))

    password_entry = tk.Entry(card,  width=30,  show="*",  relief="flat",  highlightthickness=1,  highlightbackground="#cccccc")
    password_entry.pack(pady=(0,10), ipady=4)

    # Login Logic 
    def login_action():
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "Please enter email and password")
            return

        user = login_user(email, password)

        if user:
            window.destroy()
            open_user_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    # Login Button 
    tk.Button(card,text="Login",bg="#3b7ddd",fg="white",width=22,height=1,bd=0,command=login_action).pack(pady=15)

    #  Forgot Password (Clickable Label) 
    forgot_label = tk.Label(card,text="Forgot Password?",fg="#3b7ddd",bg="white",cursor="hand2")
    forgot_label.pack()
    forgot_label.bind("<Button-1>",
                      lambda e: [window.destroy(), open_forgot_password()])

    # Divider
    tk.Frame(card, height=1, bg="#dddddd").pack(fill="x", pady=15, padx=50)

    # Create Account
    tk.Button(card,text="Create Account",width=22,height=1,relief="solid",bd=1,command=lambda: [window.destroy(), open_signup()]).pack(pady=5)

   #  Top Bar 
    top_bar = tk.Frame(window, bg="#ffffff")
    top_bar.pack(fill="x", pady=10)

    admin_btn = tk.Button(top_bar,text="Admin Login",bg="#60c7d2",fg="white",bd=0,padx=15,pady=5,command=lambda: [window.destroy(), open_admin_login_window()]) 
    admin_btn.pack(side="right", padx=20)


    window.mainloop()
