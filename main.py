from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

def fetch_data():
    df = pd.read_csv("data.csv")
    return df

def filter_empty_skills(df):
    df = df[df["skills"].apply(len) > 0]
    df.reset_index(drop=True, inplace=True)
    return df


def calculate_similarity(df):
    vectorizer = TfidfVectorizer()
    skills_matrix = vectorizer.fit_transform(df["skills_str"])
    similarity_matrix = cosine_similarity(skills_matrix)
    return similarity_matrix


def recommend_users(user_id, df, similarity_matrix, top_n=5):
    try:
        user_id = int(user_id)
        user_idx = df.index[df["id"] == user_id].tolist()[0]
        user_similarity = similarity_matrix[user_idx]
        similarity_scores = list(enumerate(user_similarity))
        similarity_scores = [pair for pair in similarity_scores if pair[0] != user_idx]
        sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        similar_users_idx = [idx for idx, _ in sorted_scores[:top_n]]
        similar_users = df.iloc[similar_users_idx][["id", "skills"]].to_dict('records')
        return similar_users
    except IndexError:
        return f"User ID {user_id} not found in the dataset."

def preprocess_skills(df):
    df["skills_str"] = df["skills"].astype(str)
    return df

# Initialize data and similarity matrix at startup
df = fetch_data()
df = preprocess_skills(df)
df = filter_empty_skills(df)
similarity_matrix = calculate_similarity(df)


@app.route('/')
def index():
    return "Welcome to the API"

@app.route('/recommend', methods=['GET'])
def get_recommendations():
    user_id = request.args.get('user_id')
    top_n = request.args.get('top_n', default=3, type=int)
    
    if not user_id:
        return jsonify({"error": "user_id parameter is required"}), 400
        
    similar_users = recommend_users(user_id, df, similarity_matrix, top_n=top_n)
    
    return jsonify({
        "user_id": user_id,
        "recommended_users": similar_users
    })

if __name__ == '__main__':
    app.run(debug=True)
