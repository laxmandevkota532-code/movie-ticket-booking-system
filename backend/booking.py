from backend.database import get_connection

def get_shows_by_movie(movie_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, date, time, ticket_price
        FROM shows
        WHERE movie_id = ?
    """, (movie_id,))

    shows = cursor.fetchall()
    conn.close()
    return shows

def get_user_bookings(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT m.name, s.date, s.time, b.seat_number, b.booking_time
        FROM bookings b
        JOIN shows s ON b.show_id = s.id
        JOIN movies m ON s.movie_id = m.id
        WHERE b.user_id = ?
        ORDER BY b.booking_time DESC
    """, (user_id,))

    bookings = cursor.fetchall()
    conn.close()
    return bookings

def save_booking(user_id, show_id, seats):
    conn = get_connection()
    cursor = conn.cursor()

    from datetime import datetime
    booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO bookings (user_id, show_id, seat_number, booking_time)
        VALUES (?, ?, ?, ?)
    """, (user_id, show_id, seats, booking_time))

    conn.commit()
    conn.close()

