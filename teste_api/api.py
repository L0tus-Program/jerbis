from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import jerbis

app = Flask(__name__)
CORS(app)  # Quando subir pra VPS, configurar domínios que podem acessar


@app.route("/message_typebot", methods=["POST"])
def default():
    data = request.get_json()
    message = data['message']
    history = data['history']
    response = jerbis.chat_api_typebot(message,history)

    
    return jsonify({"response": response}),200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
