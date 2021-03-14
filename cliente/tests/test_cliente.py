from . import BaseTestClass

class cliente_tests(BaseTestClass):
    def test_index(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'{"mensaje":"API en Python con Flask"}\n', res.data)

    def solicitar_pedido(self):
        self.solicitar_pedido_cliente(self)
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Prueba', res.data)
    
    def estado_pedido_restaurante(self):
        res = self.client.post('/api/estado_pedido_restaurante', data=dict(
            id_pedido="1"
        ))
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Prueba estado pedido restaurante', res.data)
    
    def estado_pedido_repartidor(self):
        res = self.client.post('/api/estado_pedido_repartidor', data=dict(
            id_pedido="1"
        ))
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Prueba estado pedido repartidor', res.data)
