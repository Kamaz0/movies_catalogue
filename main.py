from flask import Flask, render_template
import tmdb_client
from flask import request

app = Flask(__name__)

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    # movies = tmdb_client.get_popular_movies()["results"][:8]
    options = ["now_playing", "upcoming", "popular", "top_rated"]
    if selected_list not in options:
        selected_list = "popular"
    movies = tmdb_client.get_movies(how_many=8,list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, options=options)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movies/<movie_id>")
# def movie_details(movie_id):
#     return render_template("movie_details.html", movie=get_popular_movies)
# def movie_details(movie_id):
# 	movie = tmdb_client.get_single_movie(movie_id)
# 	return render_template("movie_details.html", movie=movie)
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)[:8]
    return render_template("movie_details.html", movie=details, cast=cast)