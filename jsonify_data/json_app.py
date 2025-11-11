import requests
from flask import Flask, jsonify




url = "https://api.themoviedb.org/3/genre/movie/list"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NmUzN2JmZGJlN2E2NTZhZjNjNDYzN2I5Y2IxODM3MSIsIm5iZiI6MTc2Mjc4Mjk0My44MDcwMDAyLCJzdWIiOiI2OTExZWVkZmRmYTBkNzgwNzY4NzUzODQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.CuoovxwKq6LQRNR6ZAJ2Dv64xWgxauKWdb6t8wkrYLE"
}

params = {"language": "en-US"}


app = Flask(__name__)


def data_fetch():
    for attempt in range(3):

        try:

            response = requests.get(url, headers = headers, params = params, timeout=10)
            response.raise_for_status()
            return response.json()
            
        
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")  



@app.route("/")
def home():
    data = data_fetch()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug = True)

