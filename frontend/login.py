# import tkinter as tk
# from tkinter import messagebox
# from backend.auth import login_user
# from frontend.signup import open_signup
# from frontend.user_dashboard import open_user_dashboard
# from frontend.admin_dashboard import open_admin_dashboard
# from frontend.forgot_password import open_forgot_password


# def open_login():
#     window = tk.Tk()
#     window.title("Login")
#     window.geometry("500x500")
#     window.configure(bg="#78a9f3")

#     tk.Label(window, text="Email").pack(pady=5)
#     email_entry = tk.Entry(window)
#     email_entry.pack()

#     tk.Label(window, text="Password").pack(pady=5)
#     password_entry = tk.Entry(window, show="*")
#     password_entry.pack()

#     def login_action():
#         email = email_entry.get()
#         password = password_entry.get()

#     def login_action():
#         email = email_entry.get().strip()
#         password = password_entry.get().strip()

#         # 🚨 Empty check
#         if email == "" or password == "":
#             messagebox.showerror("Error", "Please enter email and password")
#             return

#         user = login_user(email, password)

#         if user:
#             window.destroy()
#             open_user_dashboard()
#         else:
#             messagebox.showerror("Error", "Invalid user credentials")

#     # Admin login 
#     def open_admin_login():
#         window.destroy()
#         from frontend.admin_login import open_admin_login_window
#         open_admin_login_window()



#     def go_to_signup():
#         window.destroy()
#         open_signup()

#     tk.Button(window, text="Login", command=login_action).pack(pady=5)
#     tk.Button(window, text="Signup", command=go_to_signup).pack(pady=5)
#     tk.Button(window, text="Forgot Password", command=open_forgot_password).pack(pady=5)
#     tk.Button(window, text="Admin Login", command=open_admin_login).pack(pady=5)
  
#     window.mainloop()

import tkinter as tk
from tkinter import messagebox
from backend.auth import login_user
from frontend.signup import open_signup
from frontend.user_dashboard import open_user_dashboard
from frontend.forgot_password import open_forgot_password


def open_login():
    window = tk.Tk()
    window.title("CineBook - Login")
    window.geometry("1000x600")
    window.configure(bg="white")
    window.resizable(False, False)

    # ================= TOP BAR =================
    top_bar = tk.Frame(window, height=60, bg="#2c3e50")
    top_bar.pack(fill="x")

    tk.Label(
        top_bar,
        text="CineBook",
        bg="#2c3e50",
        fg="white",
        font=("Arial", 18, "bold")
    ).pack(side="left", padx=20)

    # ================= LEFT PANEL =================
    left_panel = tk.Frame(window, width=300, bg="#34495e")
    left_panel.pack(side="left", fill="y")

    tk.Label(
        left_panel,
        text="User Login",
        bg="#34495e",
        fg="white",
        font=("Arial", 20, "bold")
    ).pack(pady=200)

    # ================= RIGHT CONTENT =================
    main_content = tk.Frame(window, bg="white")
    main_content.pack(expand=True, fill="both")

    form_frame = tk.Frame(main_content, bg="white")
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(form_frame, text="Email", font=("Arial", 12), bg="white").pack(anchor="w")
    email_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
    email_entry.pack(pady=10)

    tk.Label(form_frame, text="Password", font=("Arial", 12), bg="white").pack(anchor="w")
    password_entry = tk.Entry(form_frame, font=("Arial", 14), width=30, show="*")
    password_entry.pack(pady=10)

    # ================= LOGIN ACTION =================
    def login_action():
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if email == "" or password == "":
            messagebox.showerror("Error", "Please enter email and password")
            return

        user = login_user(email, password)

        if user:
            window.destroy()
            open_user_dashboard()
        else:
            messagebox.showerror("Error", "Invalid user credentials")

    # ================= ADMIN LOGIN =================
    def open_admin_login():
        window.destroy()
        from frontend.admin_login import open_admin_login_window
        open_admin_login_window()

    def go_to_signup():
        window.destroy()
        open_signup()

    # ================= BUTTON STYLE =================
    def sidebar_button(text, command):
        return tk.Button(
            form_frame,
            text=text,
            width=25,
            height=2,
            bg="#2c3e50",
            fg="white",
            bd=0,
            command=command
        )

    sidebar_button("Login", login_action).pack(pady=10)
    sidebar_button("Signup", go_to_signup).pack(pady=5)
    sidebar_button("Forgot Password", open_forgot_password).pack(pady=5)
    sidebar_button("Admin Login", open_admin_login).pack(pady=5)

    window.mainloop()