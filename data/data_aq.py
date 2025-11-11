# import requests
# import pandas as pd
# import time 
# from flask import Flask, jsonify, render_template_string

# # app = Flask(__name__)


# # # TMDB end points and headers

# # url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

# # headers = {
# #     "accept": "application/json",
# #     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NmUzN2JmZGJlN2E2NTZhZjNjNDYzN2I5Y2IxODM3MSIsIm5iZiI6MTc2Mjc4Mjk0My44MDcwMDAyLCJzdWIiOiI2OTExZWVkZmRmYTBkNzgwNzY4NzUzODQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.CuoovxwKq6LQRNR6ZAJ2Dv64xWgxauKWdb6t8wkrYLE"
# # }



# # def fetch_tmdb_data():

# #     response = requests.get(url, headers = headers)
# #     response.raise_for_status()

# #     return response.json()


# # @app.route("/")
# # def top_movies():
    
# #     data = fetch_tmdb_data()

# #     return jsonify(data)  #JSON output in browser

# # @app.route("/keys")
# # def data_keys():
   
# #     data = fetch_tmdb_data()
# #     return jsonify(list(data.keys()))


# # if __name__=="__main__":
# #     app.run(debug=True)



# # ---------------------------------------------------------------------------------------


# url = "https://api.themoviedb.org/3/movie/top_rated"

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NmUzN2JmZGJlN2E2NTZhZjNjNDYzN2I5Y2IxODM3MSIsIm5iZiI6MTc2Mjc4Mjk0My44MDcwMDAyLCJzdWIiOiI2OTExZWVkZmRmYTBkNzgwNzY4NzUzODQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.CuoovxwKq6LQRNR6ZAJ2Dv64xWgxauKWdb6t8wkrYLE"
#     }


# all_movies = []



# for i in range(1, 525):

#     time.sleep(0.2)
#     params = {"language": "en-US", 
#               "page": i}
    

#     response = requests.get(url, headers = headers, params = params)
#     time.sleep(0.4)


#     if response.status_code !=200:
#         print(f"Error on Page {i}: {response.status_code}")
#         continue
#     data = response.json()

#     time.sleep(0.2)

#     results = data.get("results", [])


#     for movie in results:
#         time.sleep(0.4)
#         all_movies.append(
#             {"Title": movie.get("title"), 
#              "Description": movie.get("overview"), 
#              "Genres": movie.get("genre_ids")}
#         )
#         time.sleep(0.2)
    
#     print(f"Fetched Page: {i}")
#     time.sleep(0.2)


#     df = pd.DataFrame(all_movies)


#     print(df.head())
#     time.sleep(0.3)

#     print(df.shape)

#     df.to_csv(r"D:\Programming - D\NLP Projects\TMDB movie Project\Code\data\movie_class.csv")



import requests
import pandas as pd
import time
import os

# TMDB endpoint and headers
url = "https://api.themoviedb.org/3/movie/top_rated"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NmUzN2JmZGJlN2E2NTZhZjNjNDYzN2I5Y2IxODM3MSIsIm5iZiI6MTc2Mjc4Mjk0My44MDcwMDAyLCJzdWIiOiI2OTExZWVkZmRmYTBkNzgwNzY4NzUzODQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.CuoovxwKq6LQRNR6ZAJ2Dv64xWgxauKWdb6t8wkrYLE"
}

save_path = r"D:\Programming - D\NLP Projects\TMDB movie Project\Code\data\movie_class.csv"
all_movies = []

# Resume from last saved file if it exists
if os.path.exists(save_path):
    df_existing = pd.read_csv(save_path)
    all_movies = df_existing.to_dict(orient="records")
    start_page = len(all_movies) // 20 + 1  # approx last page
    print(f"Resuming from page {start_page}...")
else:
    start_page = 1

# Loop through all 524 pages
for i in range(start_page, 525):
    params = {"language": "en-US", "page": i}

    # Retry logic
    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            break
        except requests.exceptions.RequestException as e:
            print(f"Error on Page {i}, attempt {attempt+1}: {e}")
            time.sleep(3)
    else:
        print(f"Skipping page {i} after 3 failed attempts.")
        continue

    results = data.get("results", [])
    for movie in results:
        all_movies.append({
            "Title": movie.get("title"),
            "Description": movie.get("overview"),
            "Genres": movie.get("genre_ids")
        })

    print(f"Fetched Page: {i}, Total Movies: {len(all_movies)}")

    # Periodic save every 25 pages
    if i % 25 == 0 or i == 524:
        df = pd.DataFrame(all_movies)
        df.to_csv(save_path, index=False)
        print(f"✅ Progress saved at page {i}")

    # Respect API rate limits
    time.sleep(0.5)

# Final save
df = pd.DataFrame(all_movies)
df.to_csv(save_path, index=False)
print("🎉 Completed successfully!")
print("Total movies fetched:", df.shape[0])






