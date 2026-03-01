
# Add Movie
from backend.database import get_connection

def add_movie(name, description, duration, genre):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO movies (name, description, duration, genre)
    VALUES (?, ?, ?, ?)
    """, (name, description, duration, genre))

    conn.commit()
    conn.close()

    return True

# Delete Movie

def get_all_movies():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()

    conn.close()
    return movies


def delete_movie(movie_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    conn.commit()
    conn.close()

    return True

# Add show

def add_show(movie_id, date, time, ticket_price):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO shows (movie_id, date, time, ticket_price)
    VALUES (?, ?, ?, ?)
    """, (movie_id, date, time, ticket_price))

    conn.commit()
    conn.close()

    return True

# View Booking

def get_all_bookings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT bookings.id, movies.name, shows.date, shows.time
    FROM bookings
    JOIN shows ON bookings.show_id = shows.id
    JOIN movies ON shows.movie_id = movies.id
    """)

    data = cursor.fetchall()
    conn.close()
    return data

# View Revenue

def get_total_revenue():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT SUM(shows.ticket_price)
    FROM bookings
    JOIN shows ON bookings.show_id = shows.id
    """)

    result = cursor.fetchone()
    conn.close()

    if result[0]:
        return result[0]
    else:
        return 0