from flask import Flask, jsonify, request, json

app = Flask(__name__)


todos = [{ "label": "My first task", "done": False }, { "label": "My second task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
    
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data   
    decoded_object = json.loads(request_body)
    #leo de formato js a python con esta fx load, y se almacena en decoded objet.
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    #en postman /posicion que le dé, lo eliminará /0 el primero, /1, el 2do
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)