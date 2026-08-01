class Usuario():
    def __init__(self, username, password, correo, direccion="", apellido="", edad="", nombre=""):
        self.username = username
        self.correo = correo
        self.direccion = direccion
        self.apellido = apellido
        self.edad = edad
        self.nombre = nombre
        
    def __str__(self):
        return f"Hola, mi username es {self.username}"
        