from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(df):

    vectorizer = TfidfVectorizer(
        max_features=50000,
        ngram_range=(1,2),   # unigram + bigram
        stop_words='english'
    )

    X = vectorizer.fit_transform(df['cleaned_text'])

    return X, vectorizer