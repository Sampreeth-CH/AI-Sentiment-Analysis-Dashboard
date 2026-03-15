# AI Sentiment Analysis Dashboard

An AI-powered sentiment analysis system that analyzes customer reviews and classifies them as **Positive** or **Negative** using Machine Learning.  
The project includes a **Flask REST API**, **machine learning model**, **database storage**, and an **interactive dashboard** for visualization.

---

# Project Overview

Customer reviews are a valuable source of feedback for businesses.  
This project builds an intelligent system that can automatically determine the sentiment of reviews and visualize the results in an analytics dashboard.

The system uses **Natural Language Processing (NLP)** and **Machine Learning** to classify reviews and provide insights through charts and statistics.

---

# Key Features

- Automatic sentiment classification of customer reviews
- Text preprocessing and cleaning pipeline
- TF-IDF feature extraction
- Logistic Regression Machine Learning model
- REST API built with Flask
- SQLite database for storing analyzed reviews
- Interactive dashboard with charts and statistics
- Real-time sentiment prediction

---

# Tech Stack

## Programming Language
- Python

## Machine Learning
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression

## Backend
- Flask
- Flask-CORS

## Database
- SQLite

## Frontend
- HTML
- CSS
- JavaScript
- Chart.js

## Data Processing
- Pandas
- NumPy

---

# Project Architecture

User Review  
↓  
Flask API  
↓  
Text Preprocessing  
↓  
TF-IDF Vectorization  
↓  
Machine Learning Model (Logistic Regression)  
↓  
Sentiment Prediction  
↓  
Database Storage  
↓  
Dashboard Visualization  

---

# Project Structure
```
ai-sentiment-analysis-dashboard
│
├── api.py
├── train_pipeline.py
├── requirements.txt
├── README.md
│
├── src
│ ├── data_processing.py
│ ├── preprocessing.py
│ ├── feature_extraction.py
│ ├── model_training.py
│ ├── evaluation.py
│ ├── save_model.py
│ └── database.py
│
├── templates
│ └── dashboard.html
│
├── models
│ ├── sentiment_model.pkl
│ └── vectorizer.pkl
│
└── data
```

---

# Dataset

The dataset used for training contains customer product reviews with sentiment labels.

Dataset Format:
class_index, review_title, review_text

Where:

- `1` → Negative Review  
- `2` → Positive Review  

The dataset is **not included in this repository due to size limitations**.

---

# Machine Learning Model

The project uses **Logistic Regression** for sentiment classification.

## Pipeline

1. Text Cleaning
2. Stopword Removal
3. Tokenization
4. TF-IDF Vectorization
5. Logistic Regression Classification

## Model Performance

- Accuracy: ~88%
- Precision: ~88%
- Recall: ~89%
- F1 Score: ~88%

---

# Dashboard Features

The dashboard provides real-time analytics including:

- Sentiment distribution chart
- Positive vs negative review counts
- Table of analyzed reviews
- Real-time prediction from user input
- Confidence score for each prediction

---

# How to Run the Project

## 1 Install Dependencies
pip install -r requirements.txt

## 2 Train the Model (Optional)
python train_pipeline.py

## 3 Start the API Server
python api.py

## 4 Open Dashboard
http://127.0.0.1:5000

---

# Example API Usage

## Predict Sentiment

POST request:
/predict

Example JSON request:
{ "review_text": "This product is amazing and works perfectly" }

Example response:
{ "sentiment": 1, "score": 0.91 }

---

# Future Improvements

- Deep learning based sentiment analysis
- Multi-class sentiment classification (positive, negative, neutral)
- Advanced NLP techniques
- Cloud deployment
- Enhanced analytics dashboard

---

# License

This project is created for educational and research purposes.

---

## 👤 Author

**Sampreeth CH**

- 🔗 LinkedIn: [Sampreeth CH](https://www.linkedin.com/in/sampreethch)
- 🐙 GitHub: [@Sampreeth-CH](https://github.com/Sampreeth-CH)
- 📧 Email: sampreethchsampreethch@gmail.com
- 🌐 Portfolio: *(Coming soon)*

Feel free to connect or reach out for collaboration, feedback, or just to say hi!
