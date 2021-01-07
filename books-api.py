
import json

from flask import Flask
from pathlib import Path

app = Flask(__name__)

BOOKS = [{'id': 1, 'title': 'Moby Dick'}, {'id': 2, 'title': "I can't think of another title"}]

books_directory_path = Path('/mnt/hugo-storage')
books_file_path = books_directory_path / "books.txt"
books_directory_path.mkdir(parents=True, exist_ok=True)
with open(books_file_path, 'w') as fp:
    json.dump(BOOKS, fp)

@app.route('/health')
def health():
    return {'health': 'ok'}

@app.route('/books')
def books():
    return {'results': BOOKS}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
