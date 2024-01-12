from flask import Flask, request, jsonify, abort
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Quando subir pra VPS, configurar domínios que podem acessar


@app.route("/", methods=["POST"])
def default():
    data = request.get_data(as_text= True)
    
    return "bombou"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
