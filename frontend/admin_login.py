# import tkinter as tk
# from tkinter import messagebox
# from backend.auth import login_admin
# from frontend.admin_dashboard import open_admin_dashboard


# def open_admin_login_window():
#     window = tk.Tk()
#     window.title("Admin Login")
#     window.geometry("300x250")

#     tk.Label(window, text="Admin Email").pack(pady=5)
#     email_entry = tk.Entry(window)
#     email_entry.pack()

#     tk.Label(window, text="Password").pack(pady=5)
#     password_entry = tk.Entry(window, show="*")
#     password_entry.pack()

#     def admin_login():
#         email = email_entry.get()
#         password = password_entry.get()

#         admin = login_admin(email, password)

#         if admin:
#             window.destroy()
#             open_admin_dashboard()
#         else:
#             messagebox.showerror("Error", "Invalid admin credentials!")

#     tk.Button(window, text="Login", command=admin_login).pack(pady=20)

#     window.mainloop()

import tkinter as tk
from tkinter import messagebox
from backend.auth import login_admin
from frontend.admin_dashboard import open_admin_dashboard


def open_admin_login_window():
    window = tk.Tk()
    window.title("CineBook - Admin Login")
    window.geometry("1000x600")
    window.configure(bg="white")
    window.resizable(False, False)

    # ================= TOP BAR =================
    top_bar = tk.Frame(window, height=60, bg="#2c3e50")
    top_bar.pack(fill="x")

    tk.Label(
        top_bar,
        text="CineBook - Admin",
        bg="#2c3e50",
        fg="white",
        font=("Arial", 18, "bold")
    ).pack(side="left", padx=20)

    # ================= LEFT PANEL =================
    left_panel = tk.Frame(window, width=300, bg="#34495e")
    left_panel.pack(side="left", fill="y")

    tk.Label(
        left_panel,
        text="Admin Login",
        bg="#34495e",
        fg="white",
        font=("Arial", 20, "bold")
    ).pack(pady=200)

    # ================= RIGHT CONTENT =================
    main_content = tk.Frame(window, bg="white")
    main_content.pack(expand=True, fill="both")

    form_frame = tk.Frame(main_content, bg="white")
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(form_frame, text="Admin Email", font=("Arial", 12), bg="white").pack(anchor="w")
    email_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
    email_entry.pack(pady=10)

    tk.Label(form_frame, text="Password", font=("Arial", 12), bg="white").pack(anchor="w")
    password_entry = tk.Entry(form_frame, font=("Arial", 14), width=30, show="*")
    password_entry.pack(pady=10)

    # ================= LOGIN ACTION =================
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

    # ================= BUTTON =================
    tk.Button(
        form_frame,
        text="Login",
        width=25,
        height=2,
        bg="#2c3e50",
        fg="white",
        bd=0,
        command=admin_login
    ).pack(pady=20)

    window.mainloop()