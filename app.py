import pickle
import streamlit as st
import requests

def fetch_poster(id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_ids = []
    for i in distances[1:6]:
        # fetch the movie poster
        id = movies.iloc[i[0]].id
        recommended_movie_ids.append(id)
        recommended_movie_posters.append(fetch_poster(id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters,recommended_movie_ids



st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,recommended_movie_ids = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    image_height = 200  # Adjust the height as needed
    with col1:
        st.markdown(f'<a href="https://www.themoviedb.org/movie/{recommended_movie_ids[0]}">'
                    f'<img src="{recommended_movie_posters[0]}" width="140" height="{image_height}" style="object-fit: cover;"></a>',
                    unsafe_allow_html=True)
        st.text(recommended_movie_names[0])
    with col2:
        st.markdown(f'<a href="https://www.themoviedb.org/movie/{recommended_movie_ids[1]}">'
                    f'<img src="{recommended_movie_posters[1]}" width="140" height="{image_height}" style="object-fit: cover;"></a>',
                    unsafe_allow_html=True)
        st.text(recommended_movie_names[1])
    with col3:
        st.markdown(f'<a href="https://www.themoviedb.org/movie/{recommended_movie_ids[2]}">'
                    f'<img src="{recommended_movie_posters[2]}" width="140" height="{image_height}" style="object-fit: cover;"></a>',
                    unsafe_allow_html=True)
        st.text(recommended_movie_names[2])
    with col4:
        st.markdown(f'<a href="https://www.themoviedb.org/movie/{recommended_movie_ids[3]}">'
                    f'<img src="{recommended_movie_posters[3]}" width="140" height="{image_height}" style="object-fit: cover;"></a>',
                    unsafe_allow_html=True)
        st.text(recommended_movie_names[3])
    with col5:
        st.markdown(f'<a href="https://www.themoviedb.org/movie/{recommended_movie_ids[4]}">'
                    f'<img src="{recommended_movie_posters[4]}" width="140" height="{image_height}" style="object-fit: cover;"></a>',
                    unsafe_allow_html=True)
        st.text(recommended_movie_names[4])