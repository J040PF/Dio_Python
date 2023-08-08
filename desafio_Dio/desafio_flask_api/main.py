from flask import request, jsonify, Flask

json_file = [
  {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo",
    "pais": "Brasil"
  },
  {
    "nome": "Maria",
    "idade": 25,
    "cidade": "Rio de Janeiro",
    "pais": "Brasil"
  },
  {
    "nome": "John",
    "idade": 28,
    "cidade": "New York",
    "pais": "Estados Unidos"
  },
  {
    "nome": "Sophie",
    "idade": 22,
    "cidade": "Paris",
    "pais": "França"
  },
  {
    "nome": "Luis",
    "idade": 35,
    "cidade": "Lisboa",
    "pais": "Portugal"
  }
]

app = Flask(__name__)

@app.route('/index')
def home():
  return jsonify(json_file)

app.run()