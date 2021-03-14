import unittest
from app import app

class BaseTestClass(unittest.TestCase):
    def setUp(self):
        print("------ Inicio pruebas cliente ------")
        self.app = app
        self.client = self.app.test_client()
        # Crea un contexto de aplicación
        with self.app.app_context():
            print("------ Contexto creado ------")

    def tearDown(self):
        print("------ Fin pruebas cliente ------")

    @staticmethod
    def solicitar_pedido_cliente(self):
        print("hola mundo")
        return self.client.post('/api/solicitar_pedido', data=dict(
            producto="Pizza",
            cantidad="1"
        ))