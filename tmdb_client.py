import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YjAyZjQzYjk2OWVlNDA0MzlmZWRiNGVjYTg4MDY2MCIsInN1YiI6IjVlZjFmYWE4OWE4YThhMDAzNWIzM2JiNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6N3KWEo00EXD6NuRFb4qA0Jgk7s5KpJVhhvtv39jjhE"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"