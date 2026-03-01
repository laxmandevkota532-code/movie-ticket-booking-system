# import tkinter as tk
# from tkinter import messagebox
# from backend.auth import reset_password


# def open_forgot_password():
#     window = tk.Tk()
#     window.title("Forgot Password")
#     window.geometry("300x250")

#     tk.Label(window, text="Email").pack(pady=5)
#     email_entry = tk.Entry(window)
#     email_entry.pack()

#     tk.Label(window, text="New Password").pack(pady=5)
#     password_entry = tk.Entry(window, show="*")
#     password_entry.pack()

#     def reset_action():
#         email = email_entry.get()
#         new_password = password_entry.get()

#         success = reset_password(email, new_password)

#         if success:
#             messagebox.showinfo("Success", "Password updated successfully!")
#             window.destroy()
#         else:
#             messagebox.showerror("Error", "Email not found!")

#     tk.Button(window, text="Reset Password", command=reset_action).pack(pady=20)

#     window.mainloop()


import tkinter as tk
from tkinter import messagebox
from backend.auth import reset_password


def open_forgot_password():
    window = tk.Tk()
    window.title("CineBook - Forgot Password")
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
        text="Reset Password",
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

    tk.Label(form_frame, text="New Password", font=("Arial", 12), bg="white").pack(anchor="w")
    password_entry = tk.Entry(form_frame, font=("Arial", 14), width=30, show="*")
    password_entry.pack(pady=10)

    # ================= RESET ACTION =================
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
        else:
            messagebox.showerror("Error", "Email not found!")

    # ================= BUTTON =================
    tk.Button(
        form_frame,
        text="Reset Password",
        width=25,
        height=2,
        bg="#2c3e50",
        fg="white",
        bd=0,
        command=reset_action
    ).pack(pady=20)

    window.mainloop()