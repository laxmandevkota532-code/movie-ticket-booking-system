# print("Movie Ticket Booking System Started")
# from backend.models import create_tables

# if __name__ == "__main__":
#     create_tables()
#     print("Database and users table created successfully!")

# from backend.models import create_tables
# from backend.auth import register_user

# if __name__ == "__main__":
#     create_tables()

#     # TEST REGISTER
#     success = register_user("Laxman", "laxman@test.com", "1234")

#     if success:
#         print("User registered successfully!")
#     else:
#         print("User already exists or error occurred.")

# from backend.models import create_tables
# from backend.auth import register_user, login_user

# if __name__ == "__main__":
#     create_tables()   

#     # Test login
#     success = login_user("laxman@test.com", "1234")

#     if success:
#         print("Login successful!")
#     else:
#         print("Invalid email or password.")


# from backend.models import create_tables
# from frontend.signup import open_signup

# if __name__ == "__main__":
#     create_tables()
#     open_signup()

# from backend.models import create_tables
# from frontend.login import open_login

# if __name__ == "__main__":
#     create_tables()
#     open_login()

# from backend.database import get_connection

# conn = get_connection()
# cursor = conn.cursor()
# cursor.execute("INSERT OR IGNORE INTO admins (name, email, password) VALUES (?, ?, ?)",
#                ("Admin", "admin@test.com", "admin123"))
# conn.commit()
# conn.close()

from backend.models import create_tables
from frontend.login import open_login
from backend.database import get_connection


if __name__ == "__main__":
    create_tables()

    # Insert default admin (runs safely every time)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO admins (name, email, password) VALUES (?, ?, ?)",
        ("Admin", "admin@test.com", "admin123")
    )
    conn.commit()
    conn.close()

    open_login()