#from flask import Flask, request, jsonify, Response
import requests

def main():

    url = "http://www.dneonline.com/calculator.asmx?WSDL"
    headers = {'content-type': 'application/soap+xml'}

    while(True):
        # Menu de la aplicacion
        print("Practica #2 - 201503840")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        entrada = int(input(">>"))

        if entrada == 1: # suma
            # Ingresando valores de entrada
            val1 = input("Valor 1: ")
            val2 = input("Valor 2: ")
            # Cuerpo de la peticion soap
            body = """<?xml version="1.0" encoding="utf-8"?>
                    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
                    <soap12:Body>
                        <Add xmlns="http://tempuri.org/">
                            <intA>{}</intA>
                            <intB>{}</intB>
                        </Add>
                    </soap12:Body>
                    </soap12:Envelope>""".format(val1, val2)
            # Realizando POST
            response = requests.post(url, data=body, headers=headers)
            print("Response:\n" + str(response.content))
            print("\n")

        elif entrada == 2: # resta
            # Ingresando valores de entrada
            val1 = input("Valor 1: ")
            val2 = input("Valor 2: ")
            # Cuerpo de la peticion soap
            body = """<?xml version="1.0" encoding="utf-8"?>
                    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
                    <soap12:Body>
                        <Subtract xmlns="http://tempuri.org/">
                            <intA>{}</intA>
                            <intB>{}</intB>
                        </Subtract>
                    </soap12:Body>
                    </soap12:Envelope>""".format(val1, val2)
            # Realizando POST
            response = requests.post(url, data=body, headers=headers)
            print("Response:\n" + str(response.content))
            print("\n")

        elif entrada == 3: # multiplicacion
            # Ingresando valores de entrada
            val1 = input("Valor 1: ")
            val2 = input("Valor 2: ")
            # Cuerpo de la peticion soap
            body = """<?xml version="1.0" encoding="utf-8"?>
                        <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
                        <soap12:Body>
                            <Multiply xmlns="http://tempuri.org/">
                                <intA>{}</intA>
                                <intB>{}</intB>
                            </Multiply>
                        </soap12:Body>
                        </soap12:Envelope>""".format(val1, val2)
            # Realizando POST
            response = requests.post(url, data=body, headers=headers)
            print("Response:\n" + str(response.content))
            print("\n")

        elif entrada == 4: # division
            # Ingresando valores de entrada
            val1 = input("Valor 1: ")
            val2 = input("Valor 2: ")
            # Cuerpo de la peticion soap
            body = """<?xml version="1.0" encoding="utf-8"?>
                    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
                    <soap12:Body>
                        <Divide xmlns="http://tempuri.org/">
                            <intA>{}</intA>
                            <intB>{}</intB>
                        </Divide>
                    </soap12:Body>
                    </soap12:Envelope>""".format(val1, val2)
            # Realizando POST
            response = requests.post(url, data=body, headers=headers)
            print("Response:\n" + str(response.content))
            print("\n")

        elif entrada == 5:
            print("Saliendo...\n")
            break

if __name__ == "__main__":
    main()