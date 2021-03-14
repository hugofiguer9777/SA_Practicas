from . import BaseTestClass

class cliente_tests(BaseTestClass):
    def test_index(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'{"mensaje":"API en Python con Flask"}\n', res.data)

    def recibir_pedido(self):
        self.recibir_pedido_restaurante(self)
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Prueba', res.data)

    def estado_pedido(self):
        res = self.client.post('/api/estado_pedido', data=dict(
            id_pedido="1"
        ))
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Prueba estado pedido', res.data)

    def marcar_entregado(self):
        res = self.client.post('/api/marcar_entregado', data=dict(
            id_pedido="1"
        ))
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Prueba entregado', res.data)