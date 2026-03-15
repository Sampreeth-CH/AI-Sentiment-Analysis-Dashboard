import joblib
import os

def save_model(model, vectorizer):

    # Create models folder if it doesn't exist
    os.makedirs("models", exist_ok=True)

    # Save trained model
    joblib.dump(model, "models/sentiment_model.joblib")

    # Save TF-IDF vectorizer
    joblib.dump(vectorizer, "models/tfidf_vectorizer.joblib")

    print("Model and vectorizer saved successfully in models folder.")