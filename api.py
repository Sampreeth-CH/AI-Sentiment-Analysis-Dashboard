from flask import render_template
from flask import Flask, request, jsonify
import joblib
import sqlite3

app = Flask(__name__)

model = joblib.load("models/sentiment_model.joblib")
vectorizer = joblib.load("models/tfidf_vectorizer.joblib")


def insert_review(review, label, score):

    conn = sqlite3.connect("customer_sentiment.db")
    cursor = conn.cursor()

    # CREATE TABLE IF NOT EXISTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        review_text TEXT,
        sentiment_label INTEGER,
        sentiment_score REAL
    )
    """)

    cursor.execute(
        "INSERT INTO reviews (review_text, sentiment_label, sentiment_score) VALUES (?, ?, ?)",
        (review, label, score)
    )

    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    review = data['review_text']

    review_vec = vectorizer.transform([review])

    prediction = model.predict(review_vec)[0]
    probability = model.predict_proba(review_vec)[0][prediction]

    insert_review(review, prediction, probability)

    return jsonify({
        "review": review,
        "sentiment": int(prediction),
        "score": float(probability)
    })

@app.route('/reviews', methods=['GET'])
def get_reviews():

    conn = sqlite3.connect("customer_sentiment.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT review_text, sentiment_label, sentiment_score
        FROM reviews
        ORDER BY rowid DESC
        LIMIT 50
    """)

    rows = cursor.fetchall()

    conn.close()

    reviews = []

    for row in rows:

        review_text = row[0]
        sentiment = row[1]
        score = row[2]

        # Convert review text if bytes
        if isinstance(review_text, bytes):
            review_text = review_text.decode("utf-8")

        # Convert sentiment if bytes
        if isinstance(sentiment, bytes):
            sentiment = int.from_bytes(sentiment, byteorder="little")

        # Convert score if bytes
        if isinstance(score, bytes):
            score = float(score.decode("utf-8"))

        reviews.append({
            "review": review_text,
            "sentiment": int(sentiment),
            "score": float(score)
        })

    return jsonify(reviews)


# @app.route('/analytics', methods=['GET'])
# def analytics():

#     conn = sqlite3.connect("customer_sentiment.db")
#     cursor = conn.cursor()

#     cursor.execute("SELECT COUNT(*) FROM reviews")
#     total = cursor.fetchone()[0]

#     cursor.execute("SELECT COUNT(*) FROM reviews WHERE sentiment_label=1")
#     positive = cursor.fetchone()[0]

#     cursor.execute("SELECT COUNT(*) FROM reviews WHERE sentiment_label=0")
#     negative = cursor.fetchone()[0]

#     conn.close()

#     return jsonify({
#         "total_reviews": total,
#         "positive_reviews": positive,
#         "negative_reviews": negative
#     })


if __name__ == "__main__":
    app.run(port=5000)