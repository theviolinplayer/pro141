from flask import Flask, jsonify, request
import pandas as pd

articles_data = pd.read_csv('articles.csv')
all_articles = articles_data[['url', 'title', 'text', 'lang', 'total_events']]
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

def assign_val():
    m_data = {
        "url": all_articles.iloc[0, 0],
        "title": all_articles.iloc[0, 1],
        "text": all_articles.iloc[0, 2] or "N/A",
        "lang": all_articles.iloc[0, 3],
        "total_events": all_articles.iloc[0, 4]
    }
    return m_data

@app.route("/get-article")
def get_arcle():
    article = assign_val()
    return jsonify(article)

@app.route("/liked-article")
def liked_arcle():
    article = assign_val()
    liked_articles.append(article)
    all_articles.drop(index=0, inplace=True)
    all_articles.reset_index(drop=True, inplace=True)
    return jsonify({"message": "Article added to liked articles", "article": article})

@app.route("/unliked-article")
def unliked_arcle():
    article = assign_val()
    not_liked_articles.append(article)
    all_articles.drop(index=0, inplace=True)
    all_articles.reset_index(drop=True, inplace=True)
    return jsonify({"message": "Article added to not liked articles", "article": article})

if __name__ == "__main__":
    app.run()
