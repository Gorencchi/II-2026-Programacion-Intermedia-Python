from Usuario import Usuario
class administrador(Usuario):
    def __init__(self, username, password, correo, direccion="", apellido="", edad="", nombre=""):
        super().__init__(correo, username, password, direccion, apellido, edad, nombre)
        self.usuarios = []
    
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def eliminar_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
        