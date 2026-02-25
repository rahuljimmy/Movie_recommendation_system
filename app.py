import streamlit as st
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Movie Recommender", layout="wide")

# ---------------- FETCH POSTER ---------------- #
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    if pd.isna(movie_id):
        return "https://via.placeholder.com/500x750?text=No+ID"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": "bb8b6caa63e15d5221c86ea89686657c",  # 🔴 Replace with your TMDB API key
        "language": "en-US"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"

    except:
        return "https://via.placeholder.com/500x750?text=Error"


# ---------------- LOAD DATA ---------------- #
@st.cache_data
def load_data():
    df = pd.read_csv("final_movies.csv")  # 🔴 Your dataset file name
    return df

movies_df = load_data()

# ---------------- VECTORIZE ---------------- #
@st.cache_resource
def create_similarity():
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies_df['tags'])
    similarity_matrix = cosine_similarity(vectors)
    return similarity_matrix

similarity = create_similarity()


# ---------------- RECOMMEND FUNCTION ---------------- #
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_indices = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_indices:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# ---------------- STREAMLIT UI ---------------- #
st.header("Movie Recommendation System 🎬")

selected_movie_name = st.selectbox(
    "Select a movie",
    movies_df['title'].values
)

if st.button("Recommend similar movies"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])





# bb8b6caa63e15d5221c86ea89686657c

# https://api.themoviedb.org/3/movie/movie_id?language=en-US

