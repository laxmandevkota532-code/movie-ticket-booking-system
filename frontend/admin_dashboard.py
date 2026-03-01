import tkinter as tk
from backend.admin import add_movie
from backend.admin import add_movie, get_all_movies, delete_movie
from backend.admin import add_movie, get_all_movies, delete_movie, add_show
from backend.admin import add_movie, get_all_movies, delete_movie, add_show, get_all_bookings
from backend.admin import (add_movie, get_all_movies,
                           delete_movie, add_show, get_all_bookings, get_total_revenue)


def open_admin_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Admin Dashboard")
    dashboard.geometry("900x500")

    # Sidebar Frame
    sidebar = tk.Frame(dashboard, width=200, bg="#2c3e50")
    sidebar.pack(side="left", fill="y")

    # Main Content Frame
    main_content = tk.Frame(dashboard, bg="white")
    main_content.pack(side="right", expand=True, fill="both")

    # ----clear main content--
    def clear_main():
        for widget in main_content.winfo_children():
            widget.destroy()

    # --Add Movie Form

    def show_add_movie():
        clear_main()

        tk.Label(main_content, text="Add Movie", font=(
            "Arial", 16), bg="white").pack(pady=20)

        tk.Label(main_content, text="Movie Name", bg="white").pack()
        name_entry = tk.Entry(main_content)
        name_entry.pack()

        tk.Label(main_content, text="Description", bg="white").pack()
        desc_entry = tk.Entry(main_content)
        desc_entry.pack()

        tk.Label(main_content, text="Duration", bg="white").pack()
        duration_entry = tk.Entry(main_content)
        duration_entry.pack()

        tk.Label(main_content, text="Genre", bg="white").pack()
        genre_entry = tk.Entry(main_content)
        genre_entry.pack()

        # --Save movie--
        def save_movie():
            name = name_entry.get()
            desc = desc_entry.get()
            duration = duration_entry.get()
            genre = genre_entry.get()

            if not name or not desc or not duration or not genre:
                tk.Label(main_content, text="All fields are required!",
                         fg="red", bg="white").pack()
            else:
                add_movie(name, desc, duration, genre)
                tk.Label(main_content, text="Movie Added Successfully!",
                         fg="green", bg="white").pack()

                # ---clear fields---
                name_entry.delete(0, tk.END)
                desc_entry.delete(0, tk.END)
                duration_entry.delete(0, tk.END)
                genre_entry.delete(0, tk.END)
        tk.Button(main_content, text="Save Movie",
                  command=save_movie).pack(pady=15)

    # ---Delete Movie Section--
    def show_delete_movie():
        clear_main()

        tk.Label(main_content, text="Delete Movie",
                 font=("Arial", 16), bg="white").pack(pady=20)

        movies = get_all_movies()

        if not movies:
            tk.Label(main_content, text="No movies available.",
                     bg="white").pack()
            return

        for movie in movies:
            movie_id = movie[0]
            movie_name = movie[1]

            row_frame = tk.Frame(main_content, bg="white")
            row_frame.pack(fill="x", pady=5, padx=50)

            tk.Label(row_frame, text=movie_name,
                     bg="white", anchor="w").pack(side="left")

            def delete_action(mid=movie_id):
                delete_movie(mid)
                show_delete_movie()  # refresh list

            tk.Button(row_frame, text="Delete",
                      fg="white", bg="red",
                      command=delete_action).pack(side="right")
    # Sidebar Title
    tk.Label(sidebar, text="Admin Panel", bg="#2c3e50",
             fg="white", font=("Arial", 14)).pack(pady=20)

    # ---Add Show---

    def show_add_show():
        clear_main()

        tk.Label(main_content, text="Add Show",
                 font=("Arial", 16), bg="white").pack(pady=20)

        movies = get_all_movies()

        if not movies:
            tk.Label(main_content, text="No movies available. Add movie first.",
                     bg="white", fg="red").pack()
            return

        # ----Movie Dropdown---
        tk.Label(main_content, text="Select Movie", bg="white").pack()
        movie_var = tk.StringVar()
        movie_names = [movie[1] for movie in movies]
        movie_var.set(movie_names[0])

        movie_dropdown = tk.OptionMenu(main_content, movie_var, *movie_names)
        movie_dropdown.pack()

        # Date
        tk.Label(main_content, text="Show Date (YYYY-MM-DD)", bg="white").pack()
        date_entry = tk.Entry(main_content)
        date_entry.pack()

        # Time
        tk.Label(main_content, text="Show Time (HH:MM)", bg="white").pack()
        time_entry = tk.Entry(main_content)
        time_entry.pack()

        # Ticket Price
        tk.Label(main_content, text="Ticket Price", bg="white").pack()
        price_entry = tk.Entry(main_content)
        price_entry.pack()

        def save_show():
            selected_movie_name = movie_var.get()
            date = date_entry.get()
            time = time_entry.get()
            price = price_entry.get()

            if not date or not time or not price:
                tk.Label(main_content, text="All fields required!",
                         fg="red", bg="white").pack()
                return

            # ---Get movie_id from name
            movie_id = None
            for movie in movies:
                if movie[1] == selected_movie_name:
                    movie_id = movie[0]
                    break

            add_show(movie_id, date, time, float(price))

            tk.Label(main_content, text="Show Added Successfully!",
                     fg="green", bg="white").pack()

            date_entry.delete(0, tk.END)
            time_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)

        tk.Button(main_content, text="Save Show",
                  command=save_show).pack(pady=15)

    # ---View Bookings Section----

    def show_view_bookings():
        clear_main()

        tk.Label(main_content, text="All Bookings",
                 font=("Arial", 16), bg="white").pack(pady=20)

        bookings = get_all_bookings()

        if not bookings:
            tk.Label(main_content, text="No bookings yet.",
                     bg="white", fg="red").pack()
            return

        # Table Header
        header_frame = tk.Frame(main_content, bg="white")
        header_frame.pack(fill="x", padx=40)

        tk.Label(header_frame, text="Booking ID",
                 width=15, bg="white", anchor="w").pack(side="left")
        tk.Label(header_frame, text="Movie",
                 width=20, bg="white", anchor="w").pack(side="left")
        tk.Label(header_frame, text="Date",
                 width=15, bg="white", anchor="w").pack(side="left")
        tk.Label(header_frame, text="Time",
                 width=10, bg="white", anchor="w").pack(side="left")

        # Booking Rows
        for booking in bookings:
            row = tk.Frame(main_content, bg="white")
            row.pack(fill="x", padx=40, pady=2)

            tk.Label(row, text=booking[0],
                     width=15, bg="white", anchor="w").pack(side="left")
            tk.Label(row, text=booking[1],
                     width=20, bg="white", anchor="w").pack(side="left")
            tk.Label(row, text=booking[2],
                     width=15, bg="white", anchor="w").pack(side="left")
            tk.Label(row, text=booking[3],
                     width=10, bg="white", anchor="w").pack(side="left")

    # View Revenue Section

    def show_view_revenue():
        clear_main()

        tk.Label(main_content, text="Total Revenue",
                 font=("Arial", 16), bg="white").pack(pady=30)

        total = get_total_revenue()

        tk.Label(main_content,
                 text=f"Rs. {total}",
                 font=("Arial", 20),
                 fg="green",
                 bg="white").pack(pady=10)
    # Sidebar Buttons
    tk.Button(sidebar, text="Add Movie", width=20,
              command=show_add_movie).pack(pady=10)
    tk.Button(sidebar, text="Delete Movie", width=20,
              command=show_delete_movie).pack(pady=10)
    tk.Button(sidebar, text="Add Show", width=20,
              command=show_add_show).pack(pady=10)
    tk.Button(sidebar, text="View Bookings", width=20,
              command=show_view_bookings).pack(pady=10)
    tk.Button(sidebar, text="View Revenue", width=20,
              command=show_view_revenue).pack(pady=10)

    dashboard.mainloop()
