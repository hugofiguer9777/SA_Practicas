from . import BaseTestClass

class cliente_tests(BaseTestClass):
    def test_index(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'{"mensaje":"API en Python con Flask"}\n', res.data)

    def solicitar_pedido(self):
        self.recibir_pedido(self)
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Prueba', res.data)

    def estado_pedido(self):
        res = self.client.post('/api/estado_pedido', data=dict(
            id_pedido="1"
        ))
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Prueba estado pedido', res.data)
    
    def avisar_repartidor(self):
        res = self.client.post('/api/avisar_repartidor', data=dict(
            id_repartidor="1"
        ))
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Prueba aviso repartidor', res.data)