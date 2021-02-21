#from flask import Flask, request, jsonify, Response
import uuid
import requests

def main():

    while(True):
        print("Practica #3 - 201503840")
        print("1. Solicitar pedido.")
        print("2. Verificar estado del pedido en restaurante.")
        print("3. Verificar estado del pedido a repartidor.")
        print("4. Salir.")

        entrada = int(input(">>"))

        if entrada == 1:
            # Parametros de entrada
            producto = input("Producto: ")
            cantidad = int(input("Cantidad: "))
            id_pedido = str(uuid.uuid4())

            # Llamada al metodo de restaurante
            req = requests.post('http://localhost:5000/api/recibir_pedido', json={"id_pedido": id_pedido, "producto": producto, "cantidad": cantidad })
            print(req.text)
            print("\n")

        elif entrada == 2:
            # Parametros de entrada
            id_pedido = input("Id pedido: ")

            # Llamada al metodo de restaurante
            req = requests.post('http://localhost:5000/api/estado_pedido', json={"id_pedido": id_pedido })
            print(req.text)
            print("\n")
            
        elif entrada == 3:
            # Parametros de entrada
            id_pedido = input("Id pedido: ")

            # Llamada al metodo del repartidor
            req = requests.post('http://localhost:5001/api/estado_pedido', json={"id_pedido": id_pedido })
            print(req.text)

        elif entrada == 4:
            print("Saliendo...\n")
            break

if __name__ == "__main__":
    main()