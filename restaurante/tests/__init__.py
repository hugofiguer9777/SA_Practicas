import unittest
from app import app

class BaseTestClass(unittest.TestCase):
    def setUp(self):
        print("------ Inicio pruebas restaurante ------")
        self.app = app
        self.client = self.app.test_client()
        # Crea un contexto de aplicación
        with self.app.app_context():
            print("------ Contexto creado ------")

    def tearDown(self):
        print("------ Fin pruebas restaurante ------")

    @staticmethod
    def recibir_pedido(self):
        print("hola mundo")
        return self.client.post('/api/recibir_pedido', data=dict(
            id_pedido="1",
            producto="Pizza",
            cantidad="1"
        ))