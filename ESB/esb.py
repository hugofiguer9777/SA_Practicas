from flask import Flask, request, jsonify, Response
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def root():
    response = jsonify({ 'mensaje': 'ESB en Python con Flask'})
    return response


@app.route('/esb/recibir_pedido', methods=['POST'])
def recibir_pedido():
    # Recibiendo parametros del body
    id_pedido = request.json['id_pedido']
    producto = request.json['producto']
    cantidad = request.json['cantidad']
    
    print("ESB> Pedido de cliente recibido, redirigiendo al restaurante...")
    req = requests.post('http://localhost:5000/api/recibir_pedido', json={ "id_pedido": id_pedido, "producto": producto, "cantidad": cantidad })

    # Enviando respuesta de la api
    response = jsonify({ 'id_pedido': id_pedido, 'producto': producto, 'cantidad': cantidad, 'mensaje': 'Pedido redirigido.'})
    return response

@app.route('/esb/estado_pedido_restaurante', methods=['POST'])
def estado_pedido_restaurante():
    # Recibiendo parametros del body
    id_pedido = request.json['id_pedido']
    
    print("ESB> Estado de pedido, redirigiendo al restaurante...")
    req = requests.post('http://localhost:5000/api/estado_pedido', json={ "id_pedido": id_pedido })

    # Enviando respuesta de la api
    response = jsonify(req.text)
    return response

@app.route('/esb/estado_pedido_repartidor', methods=['POST'])
def estado_pedido_repartidor():
    # Recibiendo parametros del body
    id_pedido = request.json['id_pedido']
    
    print("ESB> Estado de pedido, redirigiendo al restaurante...")
    req = requests.post('http://localhost:5001/api/estado_pedido', json={ "id_pedido": id_pedido })

    # Enviando respuesta de la api
    response = jsonify(req.text)
    return response

@app.route('/esb/avisar_repartidor', methods=['POST'])
def avisar_repartidor():
    # Recibiendo parametros del body
    id_pedido = request.json['id_pedido']
    producto = request.json['producto']
    cantidad = request.json['cantidad']
    
    print("ESB> Pedido de restaurante recibido, redirigiendo al repartidor...")
    req = requests.post('http://localhost:5001/api/recibir_pedido_restaurante', json={ "id_pedido": id_pedido, "producto": producto, "cantidad": cantidad })

    # Enviando respuesta de la api
    response = jsonify({ 'id_pedido': id_pedido, 'producto': producto, 'cantidad': cantidad, 'mensaje': 'Pedido redirigido.'})
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
    app.run(host="0.0.0.0", port=5050, debug=True)