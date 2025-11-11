# 🎬 NLP Movie Analysis Project

## 📖 Overview
This project focuses on **Natural Language Processing (NLP)** applied to movie data.  
The first stage — **Data Acquisition** — has been completed, where top-rated films were collected programmatically using APIs.

The subsequent stages will involve **data preprocessing, exploratory analysis, and NLP modeling** to uncover insights and build intelligent features such as genre classification or recommendation systems.

---

## 🧱 Project Structure

```

TMDB---Movie-Data-Acquisition-and-NLP-pre-processing/
│
├── data/
│   ├── data_aq.py               # Script for API data acquisition
│   ├── data_merging.py          # Script for merging datasets
│   ├── movie_class.csv          # Raw or intermediate dataset
│   └── movie_with_genres.csv    # Final dataset with genres
│
├── jsonify_data/
│   └── json_app.py              # Flask/JSONify test app for data verification
│
├── notebooks/
│   └── preprocessing.ipynb      # (Planned) notebook for NLP preprocessing
│
├── README.md                    # Project documentation (you’ll add this)
├── requirements.txt             # Python dependencies (recommended)
└── .gitignore                   # Optional but good to add (ignore cache, pyc, etc.)





```

## ⚙️ Data Acquisition

The movie data was collected using **API requests** (such as TMDB API)  
to extract metadata like:
- Title  
- Overview  
- Genre

The extracted data is stored as `movies_with_genres.csv`.

---

## 🧠 Next Steps
- Data preprocessing (cleaning, handling missing values, normalizing genres)
- Text preprocessing (tokenization, stopword removal, stemming/lemmatization)
- Feature extraction using NLP methods (TF-IDF, embeddings)
- Model training and evaluation (e.g., genre prediction, sentiment analysis)

---

## 💻 Technologies Used
- **Python 3.x**
- **pandas**, **NumPy**
- **requests**
- **Flask** *(for basic data visualization endpoints)*
- **VS Code** for development
- **Git & GitHub** for version control

---

## 🚀 Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/ashiq-km/TMDB---Movie-Data-Acquisition-and-NLP-pre-processing.git
   cd "TMDB---Movie-Data-Acquisition-and-NLP-pre-processing"


2. (Optional) Create a virtual environment:

3. Install dependencies:

   pip install -r requirements.txt


📊 Example Output

The movies_with_genres.csv contains structured movie metadata:

title	overview	genres	
Inception	A thief who steals corporate secrets...	Action, Sci-Fi	
The Dark Knight	When the menace known as the Joker...	Action, Drama	


You can also separately run the scripts to hit the API's and then see the magic for yourself!!

🧩 Author

Ashiq.K.M

ashiq.dev@outlook.com

@ashi4evr1/ @ashiq-km
