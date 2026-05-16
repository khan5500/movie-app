from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Global Database
movies_database = [
    {
        "id": 1,
        "title": "Khuda Aur Muhabbat Season 3",
        "category": "Urdu Drama",
        "download_url": "https://google.com/complete_episode_1.mp4"
    },
    {
        "id": 2,
        "title": "Saraiki Shadi Funny Show",
        "category": "Saraiki Comedy",
        "download_url": "https://google.com/saraiki_funny_full.mp4"
    },
    {
        "id": 3,
        "title": "New Indian Action Movie 2026",
        "category": "Indian Movie",
        "download_url": "https://google.com/indian_movie_hd.mp4"
    }
]

# ہوم پیج پر اب ہمارا خوبصورت ڈیزائن نظر آئے گا
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_movie():
    query = request.args.get('name', '').lower()
    results = [m for m in movies_database if query in m['title'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

