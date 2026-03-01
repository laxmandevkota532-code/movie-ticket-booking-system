from backend.database import get_connection

# Register user

def register_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
        """, (name, email, password))

        conn.commit()
        return True

    except Exception as e:
        return False

    finally:
        conn.close()


# Login_User


# def login_user(email, password):
#     conn = get_connection()
#     cursor = conn.cursor()

#     # Check admin first
#     cursor.execute("""
#     SELECT * FROM admins
#     WHERE email = ? AND password = ?
#     """, (email, password))

#     admin = cursor.fetchone()

#     if admin:
#         conn.close()
#         return "admin"

#     # Check normal user
#     cursor.execute("""
#     SELECT * FROM users
#     WHERE email = ? AND password = ?
#     """, (email, password))

#     user = cursor.fetchone()
#     conn.close()

#     if user:
#         return "user"
#     else:
#         return None

# def login_user(email, password):
#     conn = get_connection()
#     cursor = conn.cursor()

#     # Check admin first
#     cursor.execute("""
#     SELECT * FROM admins
#     WHERE email = ? AND password = ?
#     """, (email, password))

#     admin = cursor.fetchone()

#     if admin:
#         conn.close()
#         return "admin"

#     # Check normal user
#     cursor.execute("""
#     SELECT * FROM users
#     WHERE email = ? AND password = ?
#     """, (email, password))

#     user = cursor.fetchone()
#     conn.close()

#     if user:
#         return "user"
#     else:
#         return None

from backend.database import get_connection

def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (email, password)
    )

    user = cursor.fetchone()
    conn.close()

    return user
    
def reset_password(email, new_password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users
    SET password = ?
    WHERE email = ?
    """, (new_password, email))

    conn.commit()

    updated = cursor.rowcount
    conn.close()

    if updated:
        return True
    else:
        return False
    
def login_admin(email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM admins WHERE email = ? AND password = ?",
        (email, password)
    )

    admin = cursor.fetchone()
    conn.close()

    return admin
