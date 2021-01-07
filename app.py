
from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
    return {'health': 'ok'}

@app.route('/books')
def books():
    return {'results': [{'id': 1, 'title': 'Moby Dick'}, {'id': 2, 'title': "I can't think of another title"}]}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
