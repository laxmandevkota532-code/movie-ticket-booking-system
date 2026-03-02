import tkinter as tk
from tkinter import messagebox
from backend.auth import reset_password


def open_forgot_password():
    window = tk.Tk()
    window.title("CineBook - Reset Password")
    window.state("zoomed")
    window.configure(bg="#e6e6e6")
    window.resizable(False, False)

    #  Center Card 
    card = tk.Frame(window,
                    bg="white",
                    highlightthickness=1,
                    highlightbackground="#d0d0d0")
    card.place(relx=0.5, rely=0.5, anchor="center",
               width=420, height=360)

    #  Title
    tk.Label(card,
             text="Reset Password",
             font=("Arial", 20, "bold"),
             bg="white").pack(pady=25)

    # Email
    tk.Label(card,
             text="Email",
             bg="white").pack(anchor="w", padx=95, pady=(5,2))

    email_entry = tk.Entry(card,
                           width=30,
                           relief="flat",
                           highlightthickness=1,
                           highlightbackground="#cccccc")
    email_entry.pack(pady=(0,8), ipady=4)

    #  New Password 
    tk.Label(card,
             text="New Password",
             bg="white").pack(anchor="w", padx=95, pady=(5,2))

    password_entry = tk.Entry(card,
                              width=30,
                              show="*",
                              relief="flat",
                              highlightthickness=1,
                              highlightbackground="#cccccc")
    password_entry.pack(pady=(0,15), ipady=4)

    # Reset Action 
    def reset_action():
        email = email_entry.get().strip()
        new_password = password_entry.get().strip()

        if email == "" or new_password == "":
            messagebox.showerror("Error", "Please fill all fields")
            return

        success = reset_password(email, new_password)

        if success:
            messagebox.showinfo("Success", "Password updated successfully!")
            window.destroy()
            from frontend.login import open_login
            open_login()
        else:
            messagebox.showerror("Error", "Email not found!")

    def go_back():
        window.destroy()
        from frontend.login import open_login
        open_login()

    #  Reset Button
    tk.Button(card,
              text="Reset Password",
              bg="#2c3e50",
              fg="white",
              width=22,
              height=2,
              bd=0,
              command=reset_action).pack(pady=10)
    
    tk.Button(form_frame,text="Back to Login",bg="white",fg="#2c3e50",font=("Arial", 11, "bold"),relief="flat",
              command=lambda: go_back()
    ).pack(pady=10)

    window.mainloop()