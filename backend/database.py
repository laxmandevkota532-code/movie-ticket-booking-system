import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "Cinebook.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

