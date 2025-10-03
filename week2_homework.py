# week 2 practicum
# Combine GET from IMDb API and POST to JSONPlaceholder

import requests

# --- Step 1: GET movies from IMDb ---
print("=== GET Request to IMDb API ===")
url_get = "https://api.imdbapi.dev/titles?types=MOVIE&year=2025"
response_get = requests.get(url_get)

if response_get.status_code == 200:
    data = response_get.json()
    titles = data.get("titles", [])

    if titles:
        # Pick the first movie
        movie = titles[1]
        movie_title = movie.get("primaryTitle")
        movie_year = movie.get("startYear")
        print(f"Selected movie: {movie_title} ({movie_year})")
    else:
        print("No movies found.")
        exit()
else:
    print("Error:", response_get.status_code, response_get.text)
    exit()

# --- Step 2: POST movie data to JSONPlaceholder ---
print("\n=== POST Request to JSONPlaceholder ===")
url_post = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": movie_title,
    "body": f"A movie released in {movie_year}",
    "userId": 1
}

response_post = requests.post(url_post, json=payload)

print("Status Code:", response_post.status_code)
print("Response Body:", response_post.json())