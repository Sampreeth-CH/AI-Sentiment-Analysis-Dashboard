from src.data_processing import load_dataset, apply_cleaning
from src.preprocessing import apply_preprocessing
from src.feature_extraction import vectorize_text
from src.model_training import train_model
from src.evaluation import evaluate_model
from src.save_model import save_model
from src.database import setup_database

dataset_path = "data/amazon_reviews.csv"

df = load_dataset(dataset_path)

df['review_text'] = df['review_title'] + " " + df['review_text']

df = apply_cleaning(df)

df = apply_preprocessing(df)

X, vectorizer = vectorize_text(df)

y = df['class_index'].map({
    2: 1,   # positive
    1: 0    # negative
})

model, X_test, y_test = train_model(X, y)

evaluate_model(model, X_test, y_test)

save_model(model, vectorizer)

setup_database()