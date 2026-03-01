import tkinter as tk
from tkinter import messagebox
from backend.auth import register_user


def open_signup():
    window = tk.Tk()
    window.title("CineBook - Signup")
    window.geometry("1000x600")
    window.configure(bg="white")
    window.resizable(False, False)

    top_bar = tk.Frame(window, height=60, bg="#2c3e50")
    top_bar.pack(fill="x")

    tk.Label(
        top_bar,
        text="CineBook",
        bg="#2c3e50",
        fg="white",
        font=("Arial", 18, "bold")
    ).pack(side="left", padx=20)

    left_panel = tk.Frame(window, width=300, bg="#34495e")
    left_panel.pack(side="left", fill="y")

    tk.Label(
        left_panel,
        text="Create Account",
        bg="#34495e",
        fg="white",
        font=("Arial", 20, "bold")
    ).pack(pady=200)

    main_content = tk.Frame(window, bg="white")
    main_content.pack(expand=True, fill="both")

    form_frame = tk.Frame(main_content, bg="white")
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(form_frame, text="Name", font=(
        "Arial", 12), bg="white").pack(anchor="w")
    name_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
    name_entry.pack(pady=10)

    tk.Label(form_frame, text="Email", font=(
        "Arial", 12), bg="white").pack(anchor="w")
    email_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
    email_entry.pack(pady=10)

    tk.Label(form_frame, text="Password", font=(
        "Arial", 12), bg="white").pack(anchor="w")
    password_entry = tk.Entry(form_frame, font=(
        "Arial", 14), width=30, show="*")
    password_entry.pack(pady=10)

    ### --Sign Up---##
    def signup_action():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if name == "" or email == "" or password == "":
            messagebox.showerror("Error", "Please fill all fields")
            return

        success = register_user(name, email, password)

        if success:
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showerror("Error", "Email already exists!")

    # ----Button---
    tk.Button(
        form_frame,
        text="Signup",
        width=25,
        height=2,
        bg="#2c3e50",
        fg="white",
        bd=0,
        command=signup_action
    ).pack(pady=20)

    window.mainloop()
