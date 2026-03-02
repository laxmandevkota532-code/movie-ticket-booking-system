from backend.database import get_connection


def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user


def update_user(user_id, name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(""" UPDATE users SET name = ?, email = ? WHERE id = ? """, (name, email, user_id))
    conn.commit()
    conn.close()


def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()