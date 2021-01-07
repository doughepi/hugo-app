
from flask import Flask

app = Flask(__name__)

BOOKS = [{'id': 1, 'title': 'Moby Dick'}, {'id': 2, 'title': "I can't think of another title"}]

with os.open('/mnt/hugo-storage/books.txt', 'w') as fp:
    json.dump(BOOKS, fp)

@app.route('/health')
def health():
    return {'health': 'ok'}

@app.route('/books')
def books():
    return {'results': BOOKS}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
