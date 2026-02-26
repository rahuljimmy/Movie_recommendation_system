# 🎬 Movie Recommendation System using Machine Learning & Natural Language Processing

## 📌 Project Overview
This project is a Content-Based Movie Recommendation System built using Machine Learning and Natural Language Processing (NLP).

The system recommends movies similar to a given movie based on textual features from the movie overview.

The application is deployed as an interactive web app using Streamlit Community Cloud.

---

## 🎯 Problem Statement
To build a content-based recommendation system that suggests similar movies using textual similarity techniques.

---

## 📂 Dataset
- TMDB 5000 Movie Dataset
- Initially contained 20+ columns
- After preprocessing, reduced to:
  - Movie ID
  - Title
  - Tags

---

## 🧹 Data Preprocessing
- Removed unnecessary columns
- Handled missing values
- Selected relevant features
- Cleaned textual data

---

## 🔤 Text Preprocessing Techniques
Applied the following NLP techniques on the Overview column:

- Lowercasing
- Removing punctuation
- Removing stopwords
- Tokenization
- Stemming

---

## 🧠 Feature Engineering
- Used Bag of Words (BoW) for text vectorization
- Converted textual data into numerical vectors

---

## 📊 Similarity Calculation
- Used Cosine Similarity to measure similarity between movie vectors
- Recommended top similar movies based on similarity scores

---

## 🛠 Tech Stack Used
- Python
- NumPy
- Pandas
- Scikit-learn
- NLTK
- Streamlit
- Git & GitHub

---

## 🚀 Deployment
The final recommendation system is deployed using Streamlit Community Cloud.

🔗 Live App: [https://movie-recommendation-system-3.streamlit.app]  
💻 GitHub Repository: [https://github.com/rahuljimmy]

---

## 📌 Key Learnings
- Hands-on experience with NLP preprocessing techniques
- Understanding of vectorization (Bag of Words)
- Practical implementation of cosine similarity
- Building and deploying an end-to-end recommendation system

---

## 📌 Disclaimer
This project is built for educational purposes.
