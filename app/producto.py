class Producto:
    def __init__(self, n_producto, v_producto, c_producto):
        self.n_producto = n_producto
        self.v_producto = v_producto
        self.c_producto = c_producto

    def formato_doc(self):
        return {
            'nombre_producto': self.n_producto,
            'valor_producto': self.v_producto,
            'cantidad_producto': self.c_producto
        }
