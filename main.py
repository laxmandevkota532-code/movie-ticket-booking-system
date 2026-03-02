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
        ("Admin", "admin@gmail.com", "admin123")
    )
    conn.commit()
    conn.close()

    open_login()