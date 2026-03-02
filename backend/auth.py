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
        print("REGISTER ERROR:", E)
        return False

    finally:
        conn.close()


# User Login

from backend.database import get_connection

def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()

    print("Trying login with:", email, password)  

    cursor.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (email, password)
    )

    user = cursor.fetchone()
    print("User found:", user)   

    conn.close()
    return user
 # Reset password
    
def reset_password(email, new_password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(""" UPDATE users SET password = ? WHERE email = ? """, (new_password, email))

    conn.commit()

    updated = cursor.rowcount
    conn.close()

    if updated:
        return True
    else:
        return False
    
# login admin
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
