from Persona import Persona
class Profesor(Persona):
    def __init__(self, nombre, edad, apellido, correo, departamento, direccion=""):
        super().__init__(nombre, edad, apellido, correo, direccion)
        self.departamento = departamento

    def obtener_detalles(self):
        super().obtener_detalles()
        
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"\n\tNombre: {self.nombre}\n\tDepartamento: {self.departamento}\n\tEdad: {self.edad}\n\tCorreo: {self.correo}")