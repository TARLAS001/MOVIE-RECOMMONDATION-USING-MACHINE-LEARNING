'''
Author: Bappy Ahmed
Email: entbappy73@gmail.com
Date: 2021-Nov-15
Updated by: Malhar Nikam
Enhanced: TARLAS001
'''

import pickle
import streamlit as st
import requests
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def fetch_poster(movie_id):
    """Fetches the movie poster URL from TMDB API."""
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    try:
        data = requests.get(url, timeout=5)
        data.raise_for_status()
        data = data.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
    except requests.exceptions.RequestException as e:
        st.warning(f"Could not fetch poster: {e}")
    return "https://placehold.co/500x750/333/FFFFFF?text=No+Poster"


def recommend(movie, num_recommendations=5):
    """
    Recommends similar movies based on the selected movie.
    
    Args:
        movie (str): Movie title to get recommendations for
        num_recommendations (int): Number of recommendations to return (default: 5)
    
    Returns:
        tuple: (names, posters, years, ratings)
    """
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error("Movie not found in the dataset. Please select another one.")
        return [], [], [], []
        
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_years = []
    recommended_movie_ratings = []

    for i in distances[1:num_recommendations+1]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_years.append(movies.iloc[i[0]].year)
        recommended_movie_ratings.append(movies.iloc[i[0]].vote_average)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_years, recommended_movie_ratings


def get_similarity_score(movie1, movie2):
    """Calculate similarity score between two movies."""
    try:
        idx1 = movies[movies['title'] == movie1].index[0]
        idx2 = movies[movies['title'] == movie2].index[0]
        return similarity[idx1][idx2]
    except:
        return 0


st.set_page_config(layout="wide", page_title="Movie Recommender")
st.header('🎬 Movie Recommender System Using Machine Learning')

# Load the data files
try:
    movies_dict = pickle.load(open('artifacts/movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model files not found. Please run the data processing notebook first.")
    st.stop()


# Sidebar for settings
st.sidebar.header("Settings")
num_recommendations = st.sidebar.slider("Number of recommendations", 1, 10, 5)
show_similarity_score = st.sidebar.checkbox("Show similarity scores", False)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

with col2:
    search_button = st.button('🔍 Find Recommendations', use_container_width=True)

if search_button:
    with st.spinner('Finding recommendations...'):
        recommended_movie_names, recommended_movie_posters, recommended_movie_years, recommended_movie_ratings = recommend(
            selected_movie, 
            num_recommendations
        )
    
    if recommended_movie_names:
        st.success(f"Found {len(recommended_movie_names)} recommendations!")
        
        cols = st.columns(num_recommendations)
        for i, col in enumerate(cols):
            with col:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
                
                year = recommended_movie_years[i]
                if pd.notna(year):
                    st.caption(f"Year: {int(year)}")
                else:
                    st.caption("Year: N/A")
                
                rating = recommended_movie_ratings[i]
                st.caption(f"Rating: {rating:.1f} ⭐")
                
                if show_similarity_score:
                    score = get_similarity_score(selected_movie, recommended_movie_names[i])
                    st.caption(f"Similarity: {score:.2%}")
