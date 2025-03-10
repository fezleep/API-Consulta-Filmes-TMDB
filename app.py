from flask import Flask, jsonify, request
import requests
app = Flask (__name__)

API_KEY = "b9c828e50b21ba4b3f5214b0ee0b34cd"

@app.route('/')
def index():
    return"Bem-Vindo a API de filmes!"
@app.route('/movies/search', methods=['GET'])
def search_movies():
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Título do filme não fornecido"}), 400
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Error ao buscar filmes"}), 500

if __name__ == '__main__':
    app.run(debug=True)