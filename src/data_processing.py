import pandas as pd
import re

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    df = df.sample(100000, random_state=42)

    # remove missing reviews
    df = df.dropna(subset=['review_text'])

    df = df.drop_duplicates()

    # combine title and review text
    df['review'] = df['review_title'] + " " + df['review_text']

    # convert labels
    df['sentiment'] = df['class_index'].map({
        2: 1,   # positive
        1: 0    # negative
    })

    return df


def clean_text(text):
    text = str(text)
    text = text.lower()
    text = text.strip()

    # Remove HTML
    text = re.sub(r'<.*?>', '', text)

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text


def apply_cleaning(df):
    df['cleaned_text'] = df['review_text'].apply(clean_text)
    return df