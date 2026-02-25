
import streamlit as st
import pickle
import pandas as pd
import requests


@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    if pd.isna(movie_id):
        return "https://via.placeholder.com/500x750?text=No+ID"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": "bb8b6caa63e15d5221c86ea89686657c",
        "language": "en-US"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        return (
            "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
            if data.get("poster_path")
            else "https://via.placeholder.com/500x750?text=No+Poster"
        )

    except requests.exceptions.RequestException as e:
        print(e)
        return "https://via.placeholder.com/500x750?text=Error"



def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_indices = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_indices:
        movie_id = movies_df.iloc[i[0]].movie_id

        recommended_movies.append(movies_df.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movies_df = pickle.load(open('movies.pkl','rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))


st.header('Movie Recommendation System 🎬')

selected_movie_name = st.selectbox('Select a movie', movies_list)

if st.button('Recommend similar movies'):
    names,posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])





# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bb8b6caa63e15d5221c86ea89686657c&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']




# bb8b6caa63e15d5221c86ea89686657c

# https://api.themoviedb.org/3/movie/movie_id?language=en-US
