class Persona():
    def __init__(self, nombre, edad, apellido, correo, direccion=""):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.correo = correo
        self.direccion = direccion
        
    def obtener_detalles(self):
        print(f"\n\tNombre: {self.nombre}\n\tEdad: {self.edad}\n\tApellido: {self.apellido}\n\tCorreo: {self.correo}\n\tDireccion: {self.direccion}")
    def imprimir_detalles(self):
        print(f"\n\tNombre: {self.nombre}\n\tEdad: {self.edad}\n\tApellido: {self.apellido}\n\tCorreo: {self.correo}\n\tDireccion: {self.direccion}")