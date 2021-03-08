from flask import Flask, request, jsonify, Response
import uuid
import requests
import ast
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def root():
    response = jsonify({ 'mensaje': 'API en Python con Flask'})
    return response


@app.route('/api/solicitar_pedido', methods=['POST'])
def recibir_pedido():
    # Recibiendo parametros del body
    id_pedido = str(uuid.uuid4())
    producto = request.json['producto']
    cantidad = request.json['cantidad']
    
    print("Cliente realizando pedido..")
    req = requests.post('http://localhost:5050/esb/recibir_pedido', json={ "id_pedido": id_pedido, "producto": producto, "cantidad": cantidad })

    # Enviando respuesta de la api
    response = jsonify({ 'id_pedido': id_pedido, 'producto': producto, 'cantidad': cantidad, 'mensaje': 'Pedido enviado.'})
    return response

@app.route('/api/estado_pedido_restaurante', methods=['POST'])
def estado_pedido_restaurante():
    # Recibiendo parametros del body
    id_pedido = request.json['id_pedido']

    print("Cliente solicitando estado de pedido restaurante..")
    req = requests.post('http://localhost:5050/esb/estado_pedido_restaurante', json={ "id_pedido": id_pedido })
    # Enviando respuesta de la api
    res = ast.literal_eval(req.text)
    response = jsonify(ast.literal_eval(res)) # conviertiendo la respuesta a json
    return response

@app.route('/api/estado_pedido_repartidor', methods=['POST'])
def estado_pedido_repartidor():
    # Recibiendo parametros del body
    id_pedido = request.json['id_pedido']

    print("Cliente solicitando estado de pedido repartidor..")
    req = requests.post('http://localhost:5050/esb/estado_pedido_repartidor', json={ "id_pedido": id_pedido })
    # Enviando respuesta de la api
    res = ast.literal_eval(req.text)
    response = jsonify(ast.literal_eval(res)) # conviertiendo la respuesta a json
    return response


@app.errorhandler(404)
def error(error=None):
    response = jsonify({
        'mensaje': 'Recurso no encontrado: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
