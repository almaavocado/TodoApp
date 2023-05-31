from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = []

@app.route('/api/todo', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todo', methods=['POST'])
def add_todo():
    todo = request.get_json()
    todos.append(todo)
    return jsonify(todo), 201

if __name__ == '__main__':
    app.run(debug=True)
