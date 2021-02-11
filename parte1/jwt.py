#from flask import Flask, request, jsonify, Response
import base64

def main():

    secret = "MiSecretDePruebaParaLaPractica#2"
    secret_encoder = codificar(secret)
    payload = ""
    header = """{"alg":"HS256","typ":"JWT"}"""
    header_encoder = codificar(header)

    while(True):
        # Menu de la aplicacion
        print("Practica #2 - 201503840")
        print("1. Generar token JWT")
        print("2. Validar token JWT")
        print("3. Salir.")

        entrada = int(input(">>"))

        if entrada == 1:
            nombre = input("Nombre: ")
            carnet = input("Carnet: ")
            payload = """{}"name":"{}","carnet":"{}"{}""".format("{", nombre, carnet, "}")
            payload_encoder = codificar(payload)
            jwt_text = "{}.{}.{}".format(header_encoder, payload_encoder, secret_encoder)
            print("Codigo JWT: " + jwt_text)

        elif entrada == 2:
            print("\n")

        elif entrada == 3:
            print("Saliendo...\n")
            break
    
def codificar(text):
    # Encoding the text into bytes
    b = text.encode("UTF-8")
    # Base64 Encode the bytes
    e = base64.b64encode(b)
    # Decoding the Base64 bytes to string
    s1 = e.decode("UTF-8")
    return s1

def decodificar(text):
    # Encoding the Base64 encoded string into bytes
    b1 = s1.encode("UTF-8")
    # Decoding the Base64 bytes
    d = base64.b64decode(b1)
    # Decoding the bytes to string
    s2 = d.decode("UTF-8")
    return s2

if __name__ == "__main__":
    main()