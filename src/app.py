from flask import Flask, jsonify, request

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


from flask import Flask
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
  # return '<h1>Hello!</h1>'
  json_text = jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    # print("Incoming request with the following body", request_body)
    if request_body.is_json:
      todo = request_body.get_json()
      return todo
    return 'Response for the POST todo'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)