import tkinter as tk
from tkinter import messagebox
from backend.auth import register_user
# from frontend.login import open_login

def open_signup():
    window = tk.Tk()
    window.title("CineBook - Sign Up")
    window.state("zoomed")
    window.configure(bg="#e6e6e6")
    window.resizable(False, False)

    # Center Card
    card = tk.Frame(window, bg="white", highlightthickness=1, highlightbackground="#d0d0d0")
    card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)

    #  Title
    tk.Label(card,text="Create Account",font=("Arial", 20, "bold"),bg="white").pack(pady=25)

    #  Name 
    tk.Label(card, text="Name", bg="white", anchor="w").pack(fill="x", padx=60)
    name_entry = tk.Entry(card, width=30, relief="flat",
                          highlightthickness=1, highlightbackground="#cccccc")
    name_entry.pack(pady=8, ipady=4)

    #  Email 
    tk.Label(card, text="Email", bg="white", anchor="w").pack(fill="x", padx=60)
    email_entry = tk.Entry(card, width=30, relief="flat",
                           highlightthickness=1, highlightbackground="#cccccc")
    email_entry.pack(pady=8, ipady=4)

    #  Password 
    tk.Label(card, text="Password", bg="white", anchor="w").pack(fill="x", padx=60)
    password_entry = tk.Entry(card, width=30, show="*", relief="flat",
                              highlightthickness=1, highlightbackground="#cccccc")
    password_entry.pack(pady=8, ipady=4)

    #  Confirm Password 
    tk.Label(card, text="Confirm Password", bg="white", anchor="w").pack(fill="x", padx=60)
    confirm_entry = tk.Entry(card, width=30, show="*", relief="flat",
                             highlightthickness=1, highlightbackground="#cccccc")
    confirm_entry.pack(pady=8, ipady=4)

    def signup_action():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        password = password_entry.get().strip()
        confirm = confirm_entry.get().strip()

        if not name or not email or not password or not confirm:
            messagebox.showerror("Error", "Please fill all fields")
            return

        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match")
            return

        success = register_user(name, email, password)

        if success:
            messagebox.showinfo("Success", "Account created successfully!")
            window.destroy()
            from frontend.login import open_login
            open_login()
        else:
            messagebox.showerror("Error", "Email already exists!")

    #  Sign Up Button 
    tk.Button(card,text="Sign Up",bg="#2250b5",fg="white",width=22,height=1,bd=0,command=signup_action).pack(pady=15)

    # Divider
    tk.Frame(card, height=1, bg="#dddddd").pack(fill="x", pady=15, padx=50)

    # Back to Login 
    
    def go_back():
        window.destroy()
        from frontend.login import open_login
        open_login()

    tk.Button(card,text="Back to Login",bg="white",fg="#2c3e50",font=("Arial", 11, "bold"),relief="flat",command=lambda: go_back()
    ).pack(pady=10)

    window.mainloop()