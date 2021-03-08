from flask import Flask, request, jsonify, Response
#from bson import json_util
#from bson.objectid import ObjectId
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

pedidos = {}

@app.route('/', methods=['GET'])
def root():
    response = jsonify({ 'mensaje': 'API en Python con Flask'})
    return response


@app.route('/api/recibir_pedido_restaurante', methods=['POST'])
def recibir_pedido():
    # Recibiendo parametros del body
    id_pedido = request.json['id_pedido']
    producto = request.json['producto']
    cantidad = request.json['cantidad']
    pedido_nuevo = { "producto": producto, "cantidad": cantidad, "estado": "En camino"}
    pedidos[id_pedido] = pedido_nuevo
    print("Pedido en camino: ", pedido_nuevo)

    # Enviando respuesta de la api
    response = jsonify({ 'id_pedido': id_pedido, 'producto': producto, 'cantidad': cantidad, 'mensaje': 'Pedido recibido y en camino.'})
    return response

@app.route('/api/estado_pedido', methods=['POST'])
def estado_pedido():
    # Recibiendo parametros del body
    id_pedido = request.json['id_pedido']

    pedido = pedidos[id_pedido]
    print("El estado del pedido ", id_pedido, " es: ", pedido['estado'])

    # Enviando respuesta de la api
    response = jsonify({ 'id_pedido': id_pedido, "producto": pedido['producto'], "estado": pedido['estado'] })
    return response

@app.route('/api/marcar_entregado', methods=['PUT'])
def marcar_entregado():
    # Recibiendo parametros del body
    id_pedido = request.json['id_pedido']

    pedido = pedidos[id_pedido]
    pedido['estado'] = "Entregado"
    pedidos[id_pedido] = pedido
    print("El pedido ", id_pedido, " a sido entregado con exito.")

    # Enviando respuesta de la api
    response = jsonify({ 'id_pedido': id_pedido, "producto": pedido['producto'], "estado": pedido['estado'] })
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
    app.run(host="0.0.0.0", port=5001, debug=True)