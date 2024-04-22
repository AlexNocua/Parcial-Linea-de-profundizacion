class Operario:
    def __init__(self, nombre, correo, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    def formato_doc(self):
        return {
            'nombre': self.nombre,
            'correo': self.correo,
            'password': self.contraseña
        }
