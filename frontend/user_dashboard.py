import tkinter as tk
from backend.admin import get_all_movies
from backend.booking import get_shows_by_movie


def open_user_dashboard():

    dashboard = tk.Tk()
    dashboard.title("User Dashboard")
    dashboard.geometry("1000x600")
    dashboard.configure(bg="white")

    top_bar = tk.Frame(dashboard, height=50, bg="#2c3e50")
    top_bar.pack(fill="x")

    tk.Label(
        top_bar,
        text="Welcome to CineBook",
        bg="#2c3e50",
        fg="white",
        font=("Arial", 14)
    ).pack(side="left", padx=20)

    tk.Button(top_bar,
              text="Profile",
              bg="white",
              command=lambda: print("Profile")
              ).pack(side="right", padx=20)

    # --SIDEBAR---
    sidebar = tk.Frame(dashboard, width=200, bg="#34495e")
    sidebar.pack(side="left", fill="y")

    tk.Label(
        sidebar,
        text="User Panel",
        bg="#34495e",
        fg="white",
        font=("Arial", 12)
    ).pack(pady=20)

    # ----MAIN CONTENT--
    main_content = tk.Frame(dashboard, bg="white")
    main_content.pack(expand=True, fill="both")

    # -----UTIL FUNCTION----
    def clear_main():
        for widget in main_content.winfo_children():
            widget.destroy()

    # ---FEATURES---
    def show_dashboard():
        clear_main()
        tk.Label(
            main_content,
            text="Welcome User 👋",
            font=("Arial", 18),
            bg="white"
        ).pack(pady=100)

    def show_movies():
        clear_main()

        tk.Label(
            main_content,
            text="Available Movies",
            font=("Arial", 16),
            bg="white"
        ).pack(pady=20)

        movies = get_all_movies()

        if not movies:
            tk.Label(
                main_content,
                text="No movies available.",
                bg="white"
            ).pack(pady=20)
            return

        for movie in movies:
            name = movie[1]
            description = movie[2]
            duration = movie[3]
            genre = movie[4]

            frame = tk.Frame(main_content, bg="#ecf0f1")
            frame.pack(fill="x", padx=50, pady=10)

            tk.Label(
                frame,
                text=f"{name} ({duration}) - {genre}",
                bg="#ecf0f1",
                font=("Arial", 12, "bold")
            ).pack(anchor="w", padx=10, pady=5)

            tk.Label(
                frame,
                text=description,
                bg="#ecf0f1",
                wraplength=600,
                justify="left"
            ).pack(anchor="w", padx=10, pady=5)

            tk.Button(
                frame,
                text="View Details",
                bg="blue",
                fg="white",
                command=lambda mid=movie[0], mname=name: show_movie_details(
                    mid, mname)
            ).pack(side="right", padx=10)

    # ----Show book tickets----
    def show_book_tickets():
        clear_main()

        tk.Label(
            main_content,
            text="Select Movie to Book 🎬",
            font=("Arial", 16),
            bg="white"
        ).pack(pady=20)

        movies = get_all_movies()

        if not movies:
            tk.Label(
                main_content,
                text="No movies available.",
                bg="white"
            ).pack(pady=20)
            return

        for movie in movies:
            movie_id = movie[0]
            name = movie[1]
            duration = movie[3]
            genre = movie[4]

            frame = tk.Frame(main_content, bg="#ecf0f1")
            frame.pack(fill="x", padx=50, pady=10)

            tk.Label(
                frame,
                text=f"{name} ({duration}) - {genre}",
                bg="#ecf0f1",
                font=("Arial", 12, "bold")
            ).pack(side="left", padx=10)

            tk.Button(
                frame,
                text="Select Show",
                bg="green",
                fg="white",
                command=lambda mid=movie_id, mname=name: show_shows(mid, mname)
            ).pack(side="right", padx=10)

    def show_my_bookings():
        clear_main()
        tk.Label(
            main_content,
            text="My Bookings Screen",
            font=("Arial", 16),
            bg="white"
        ).pack(pady=50)

    def logout():
        dashboard.destroy()
        from frontend.login import open_login
        open_login()

    def show_movie_details(movie_id, movie_name):
        clear_main()

        tk.Label(
            main_content,
            text=f"{movie_name} Details",
            font=("Arial", 16),
            bg="white"
        ).pack(pady=20)

        movies = get_all_movies()

        for movie in movies:
            if movie[0] == movie_id:
                description = movie[2]
                duration = movie[3]
                genre = movie[4]

                tk.Label(
                    main_content,
                    text=f"Duration: {duration}",
                    bg="white"
                ).pack(pady=5)

                tk.Label(
                    main_content,
                    text=f"Genre: {genre}",
                    bg="white"
                ).pack(pady=5)

                tk.Label(
                    main_content,
                    text=f"Description:\n{description}",
                    bg="white",
                    wraplength=600,
                    justify="left"
                ).pack(pady=10)

                break

    # ---Show shows---
    def show_shows(movie_id, movie_name):
        clear_main()

        tk.Label(
            main_content,
            text=f"Shows for {movie_name}",
            font=("Arial", 16),
            bg="white"
        ).pack(pady=20)

        shows = get_shows_by_movie(movie_id)

        if not shows:
            tk.Label(
                main_content,
                text="No shows available.",
                bg="white"
            ).pack(pady=20)
            return

        for show in shows:
            show_id = show[0]
            date = show[1]
            time = show[2]
            price = show[3]

            frame = tk.Frame(main_content, bg="#ecf0f1")
            frame.pack(fill="x", padx=50, pady=10)

            tk.Label(
                frame,
                text=f"{date} | {time} | Rs.{price}",
                bg="#ecf0f1"
            ).pack(side="left", padx=10)

            tk.Button(
                frame,
                text="Select",
                bg="blue",
                fg="white",
                command=lambda sid=show_id: open_seat_selection(sid)
            ).pack(side="right", padx=10)

    def open_seat_selection(show_id):
        clear_main()

        tk.Label(
            main_content,
            text="Select Your Seat 🎟️",
            font=("Arial", 16),
            bg="white"
        ).pack(pady=20)

        seat_frame = tk.Frame(main_content, bg="white")
        seat_frame.pack(pady=20)

        selected_seats = []

        rows = 5
        cols = 6

        def toggle_seat(button, seat_name):
            if seat_name in selected_seats:
                selected_seats.remove(seat_name)
                button.config(bg="green")
            else:
                selected_seats.append(seat_name)
                button.config(bg="red")

        for r in range(rows):
            for c in range(cols):
                seat_name = f"{chr(65+r)}{c+1}"

                btn = tk.Button(
                    seat_frame,
                    text=seat_name,
                    width=4,
                    bg="green"
                )

                btn.config(
                    command=lambda b=btn, s=seat_name: toggle_seat(b, s)
                )

                btn.grid(row=r, column=c, padx=5, pady=5)

        # ----Confirm booking----

        def confirm_booking():
            if not selected_seats:
                tk.Label(
                    main_content,
                    text="No seat selected!",
                    fg="red",
                    bg="white"
                ).pack()
                return

            from backend.booking import save_booking

            user_id = 1
            seats_str = ", ".join(selected_seats)

            save_booking(user_id, show_id, seats_str)

            tk.Label(
                main_content,
                text="Booking Confirmed ✅",
                fg="green",
                bg="white",
                font=("Arial", 12, "bold")
            ).pack(pady=10)

            tk.Label(
                main_content,
                text=f"Seats Selected: {', '.join(selected_seats)}",
                fg="green",
                bg="white"
            ).pack(pady=10)

        tk.Button(
            main_content,
            text="Book Now",
            bg="blue",
            fg="white",
            command=confirm_booking
        ).pack(pady=20)

    # ---My bookings---

    def show_my_bookings():
        clear_main()

        tk.Label(
            main_content,
            text="My Bookings 🎟️",
            font=("Arial", 16),
            bg="white"
        ).pack(pady=20)

        from backend.booking import get_user_bookings

        user_id = 1

        bookings = get_user_bookings(user_id)

        if not bookings:
            tk.Label(
                main_content,
                text="No bookings yet.",
                bg="white"
            ).pack(pady=50)
            return
        for booking in bookings:
            movie_name = booking[0]
            date = booking[1]
            time = booking[2]
            seats = booking[3]
            booking_time = booking[4]

            frame = tk.Frame(main_content, bg="#ecf0f1")
            frame.pack(fill="x", padx=50, pady=10)

            tk.Label(
                frame,
                text=f"{movie_name}",
                font=("Arial", 12, "bold"),
                bg="#ecf0f1"
            ).pack(anchor="w", padx=10)

            tk.Label(
                frame,
                text=f"Date: {date} | Time: {time}",
                bg="#ecf0f1"
            ).pack(anchor="w", padx=10)
            tk.Label(
                frame,
                text=f"Seats: {seats}",
                bg="#ecf0f1"
            ).pack(anchor="w", padx=10)
            tk.Label(
                frame,
                text=f"Booked At: {booking_time}",
                fg="gray",
                bg="#ecf0f1"
            ).pack(anchor="w", padx=10, pady=(0, 5))

    # ----Show Profile-----

    # ----SIDEBAR BUTTONS----
    tk.Button(sidebar, text="Dashboard", width=20,
              command=show_dashboard).pack(pady=5)
    tk.Button(sidebar, text="View Movies", width=20,
              command=show_movies).pack(pady=5)
    tk.Button(sidebar, text="Book Tickets", width=20,
              command=show_book_tickets).pack(pady=5)
    tk.Button(sidebar, text="My Bookings", width=20,
              command=show_my_bookings).pack(pady=5)
    tk.Button(sidebar, text="Logout", width=20, bg="red",
              fg="white", command=logout).pack(pady=40)

    show_dashboard()

    dashboard.mainloop()
