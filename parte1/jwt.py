#from flask import Flask, request, jsonify, Response
import base64
import hashlib
import hmac

def main():

    secret = "MiSecretDePruebaParaLaPractica#2"
    secret_encoder = ""
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
            payload = """{}"name":"{}","carnet":"{}"{}""".format("{", nombre, carnet, "}") # concatena el payload
            payload_encoder = codificar(payload) # codifica a b64 el payload

            # codificamos con sh256 el secret
            digest = hmac.new(secret.encode('UTF-8'), "{}.{}".format(header_encoder, payload_encoder).encode('UTF-8'), hashlib.sha256)
            secret_encoder = digest.hexdigest()
            byte_array = bytearray.fromhex(secret_encoder)
            base64_val = base64.b64encode(byte_array).decode("UTF-8")
            # concatenamos todo el token jwt
            jwt_text = "{}.{}.{}".format(header_encoder, payload_encoder, base64_val)
            print("Codigo JWT: " + jwt_text)

        elif entrada == 2:
            jwt_key = input("JWT: ")
            split = jwt_key.split('.')
            header_decoder = decodificar(split[0])
            payload_dencoder = decodificar(split[1])

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
    b1 = text.encode("UTF-8")
    # Decoding the Base64 bytes
    d = base64.b64decode(b1)
    # Decoding the bytes to string
    s2 = d.decode("UTF-8")
    return s2

if __name__ == "__main__":
    main()