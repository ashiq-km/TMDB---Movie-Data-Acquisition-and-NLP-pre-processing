import requests
import pandas as pd
import ast


url = "https://api.themoviedb.org/3/genre/movie/list"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NmUzN2JmZGJlN2E2NTZhZjNjNDYzN2I5Y2IxODM3MSIsIm5iZiI6MTc2Mjc4Mjk0My44MDcwMDAyLCJzdWIiOiI2OTExZWVkZmRmYTBkNzgwNzY4NzUzODQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.CuoovxwKq6LQRNR6ZAJ2Dv64xWgxauKWdb6t8wkrYLE"
}
params = {"language": "en-US"}

response = requests.get(url, headers=headers, params=params)
genre_data = response.json()

# Step 2: Build mapping dictionary
genre_map = {g["id"]: g["name"] for g in genre_data["genres"]}

# Step 3: Load your saved dataset

df = pd.read_csv("movie_class.csv")

# Step 4: Convert genre IDs to readable names
def map_genres(genre_list):
    try:
        # Convert string like "[18, 80]" → [18, 80]
        ids = ast.literal_eval(genre_list) if isinstance(genre_list, str) else genre_list
        return [genre_map.get(i, "Unknown") for i in ids]
    except Exception:
        return []

df["Genres"] = df["Genres"].apply(map_genres)

# Step 5: Save the cleaned version
df.to_csv("movies_with_genres.csv", index=False)

print("✅ Genres converted and file saved as 'movies_with_genres.csv'")
print(df.head())
