from Estudiante import Estudiante
from Profesor import Profesor
from Persona import Persona

estudiante1 = Estudiante("María", 20, "González", "maria.gonzalez@email.com", [85, 90, 78, 84.33], 84.33, "Ingeniería Informática")
estudiante2 = Estudiante("Juan", 22, "Pérez", "juan.perez@email.com", [76, 82, 88, 81], 81, "Ingeniería Civil")
profesor1 = Profesor("Carlos", 45, "Rodríguez", "carlos.rodriguez@email.com", "Departamento de Informática")
profesor2 = Profesor("Ana", 38, "López", "ana.lopez@email.com", "Departamento de Matemáticas")
estudiante1.imprimir_detalles()
estudiante2.imprimir_detalles()
profesor1.imprimir_detalles()
profesor2.imprimir_detalles()