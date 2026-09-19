import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Clase Estudiante
# Representa a un estudiante y almacena sus datos.
# ============================================================
class Estudiante:
    def __init__(
        self,
        nombre: str,
        edad: int,
        estatura: float,
        horas_estudio: int,
        calificacion: float
    ):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.horas_estudio = horas_estudio
        self.calificacion = calificacion

    def mostrar_datos(self):
        """Muestra en pantalla los datos del estudiante."""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Estatura: {self.estatura}")
        print(f"Horas de estudio: {self.horas_estudio}")
        print(f"Calificación: {self.calificacion}")
