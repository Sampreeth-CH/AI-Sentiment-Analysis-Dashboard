import sqlite3

def setup_database():

    conn = sqlite3.connect("customer_sentiment.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        review_text TEXT,
        sentiment_label INTEGER,
        sentiment_score REAL
    )
    """)

    conn.commit()
    conn.close()