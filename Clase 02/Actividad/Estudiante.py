from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, apellido, correo, notas, promedio, carrera, direccion=""):
        super().__init__(nombre, edad, apellido, correo, direccion)
        self.notas = notas
        self.promedio = promedio
        self.carrera = carrera

    def obtener_detalles(self):
        super().obtener_detalles()
 
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"\n\tNombre: {self.nombre}\n\tEdad: {self.edad}\n\tApellido: {self.apellido}\n\tCorreo: {self.correo}\n\tDireccion: {self.direccion}")
        print(f"\n\tNotas: {self.notas}\n\tPromedio: {self.promedio}\n\tCarrera: {self.carrera}")